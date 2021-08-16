# -*- coding: utf-8 -*-
import pyodbc
import jwt
import datetime

from loguru import logger
from traceback import format_exc
from flask import request, jsonify, make_response

from pegase3_api.routes_tools import *
from pegase3_api.global_variables import *
from pegase3_api.configuration_manager import *
from pegase3_api.query_manager import query_creator

app.config['SECRET_KEY'] = 'WEB_SERVICE_API'


@app.route('/signup')
def signup():
    headers = request.headers
    checked_headers = check_headers(headers=headers, route_name="signup")
    if checked_headers['status'] == 'error':
        return jsonify(checked_headers)

    if headers['Password'] != config['super_user']['password'] or headers['User-Name'] != config['super_user']['user-name']:
        return jsonify({'status': 'error', 'code': 401, 'message': 'Super user doesn\'t exists.'})

    for user in config['users']:
        logger.warning(user)
        if user['name'] == headers['New-User-Name']:
            return jsonify({'status': 'error', 'code': 400, 'message': 'User already exists.'})

    config['users'].append({'name': headers['New-User-Name'], 'password': headers['New-User-Password']})
    dump_configuration(config)
    return jsonify({'status': 'ok', 'code': 201, 'message': 'User created.'})


@app.route('/login')
def login():
    auth = request.headers
    checked_headers = check_headers(headers=auth, route_name="login")
    if checked_headers['status'] == 'error':
        return jsonify(checked_headers)

    if auth and auth['Password'] and auth['User-Name']:
        for user in config['users']:
            logger.warning(user)
            if user['password'] == auth['Password'] and user['name'] == auth['User-Name']:
                token = jwt.encode({'user': auth['User-Name'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)}, app.config['SECRET_KEY'])
                return jsonify({'status': 'ok', 'code': 200, 'token': token})
    return jsonify({'message': 'Password or User-Name not correct.', 'code': 401, 'status': 'error'})


def verify_token(token):
    try:
        jwt.decode(token, app.config['SECRET_KEY'], algorithms='HS256')
    except jwt.exceptions.InvalidSignatureError or jwt.exceptions.InvalidTokenError:
        return {'status': 'error', 'message': 'Token is not valid.', 'code': 401}
    except jwt.exceptions.ExpiredSignatureError:
        return {'status': 'error', 'message': 'Token has expired.', 'code': 498}  # METTRE DANS DOC
    return ''


@app.route('/company/info', methods=['GET'])
def company_info():
    logger.info('company_info')
    headers = request.headers
    checked_headers = check_headers(headers=headers, route_name="company/info")
    if checked_headers['status'] == 'error':
        return jsonify(checked_headers)

    token_verification = verify_token(headers['Token'])
    if len(token_verification) > 0:
        return jsonify(token_verification)

    fields = create_fields('Company', headers)
    if fields['status'] == 'error':
        return fields
    fields = fields['data']
    query = query_creator(fields=fields, table='SOCIETE', validity_date=True, extra=[f"CODSOCIETE = '{headers['Name-Company']}'"])
    info = execute_and_format_query(query=query, cursor=cursor_mysql)
    if len(info) == 0:
        return jsonify({"status": "error", "code": 404, "message": "Data not found."})
    info[0] = date_to_timestamp(info[0])
    return jsonify({"status": "ok", "code": 200, "data": info[0]})


@app.route('/company/holidays', methods=['GET'])
def company_holidays():
    logger.info('company_holidays')
    headers = request.headers
    checked_headers = check_headers(headers=headers, route_name="company/holidays")
    if checked_headers['status'] == 'error':
        return checked_headers

    token_verification = verify_token(headers['Token'])
    if len(token_verification) > 0:
        return jsonify(token_verification)

    fields = create_fields('Holidays', headers)
    extra = []
    if 'Starting-Date' in headers.keys():
        extra.append(f"""DATEJF >= {headers['Starting-Date']}\n""")
    else:
        extra.append(f"""DATEJF > \'1970-01-01\'\n""")
    if 'Ending-Date' in headers.keys():
        extra.append(f"""DATEJF <= {headers['Starting-Date']}\n""")
    query = query_creator(fields=fields['data'], table='JOURSFERIES_NAT', validity_date=False, extra=extra)
    info = execute_and_format_query(query=query, cursor=cursor_mysql)
    if len(info) == 0:
        return jsonify({"status": "error", "code": 404, "message": "Data not found."})

    info = date_to_timestamp(info)

    return jsonify({"status": "ok", "code": 200, "data": info})


@app.route('/company/sections', methods=['GET'])
def company_sections():
    logger.info('company_sections')
    headers = request.headers
    checked_headers = check_headers(headers=headers, route_name="company/sections")
    if checked_headers['status'] == 'error':
        return checked_headers

    token_verification = verify_token(headers['Token'])
    if len(token_verification) > 0:
        return jsonify(token_verification)

    fields = create_fields('Sections', headers)
    if fields['status'] == 'error':
        return jsonify(fields)
    fields = fields['data']
    query = query_creator(fields=fields, table='RUBRIQUES', validity_date=True, extra=[f"IDSOCIETE = 0"])
    infos = execute_and_format_query(query=query, cursor=cursor_mysql)
    sections = dict()
    for i in infos:
        sections[i['CODRUBRIQUE']] = i
    query = query_creator(fields=fields, table='RUBRIQUES', validity_date=True, extra=[f"IDSOCIETE = {headers['Id-Company']}"])
    info = execute_and_format_query(query=query, cursor=cursor_mysql)
    for i in info:
        sections[i['CODRUBRIQUE']] = i
    if len(sections) == 0:
        return jsonify({"status": "error", "code": 404, "message": "Data not found."})
    sections = date_to_timestamp(sections)
    return jsonify({"status": "ok", "code": 200, "data": sections})


@app.route('/establishment/list', methods=['GET'])
def establishment_list():
    logger.info('establishment_list')
    headers = request.headers
    checked_headers = check_headers(headers=headers, route_name="establishment/list")
    if checked_headers['status'] == 'error':
        return checked_headers

    token_verification = verify_token(headers['Token'])
    if len(token_verification) > 0:
        return jsonify(token_verification)

    fields = config['list_fields']['Establishment']
    query = query_creator(fields=fields, table='ETABLISSEMENTS', validity_date=True, extra=[f"IDSOCIETE = {headers['Id-Company']}"])
    info = execute_and_format_query(query=query, cursor=cursor_mysql)
    if len(info) == 0:
        return jsonify({"status": "error", "code": 404, "message": "Data not found."})
    info = date_to_timestamp(info)
    return jsonify({"status": "ok", "code": 200, "data": info})


@app.route('/establishment/info', methods=['GET'])
def establishment_info():
    logger.info('establishment_info')
    headers = request.headers
    checked_headers = check_headers(headers=headers, route_name="establishment/info")
    if checked_headers['status'] == 'error':
        return checked_headers

    token_verification = verify_token(headers['Token'])
    if len(token_verification) > 0:
        return jsonify(token_verification)

    fields = create_fields('Establishment', headers)
    if fields['status'] == 'error':
        return fields
    fields = fields['data']
    establishments_id = headers['Id-Establishments'].split(',')
    query = query_creator(fields=fields, table='ETABLISSEMENTS', validity_date=True, extra=[f"IDSOCIETE = {headers['Id-Company']}",
                                                                                            f"CODETAB in ({', '.join(establishments_id)})"])
    info = execute_and_format_query(query=query, cursor=cursor_mysql)
    if len(info) == 0:
        return jsonify({"status": "error", "code": 404, "message": "Data not found."})
    info = date_to_timestamp(info)
    return jsonify({"status": "ok", "code": 200, "data": info})


@app.route('/employee/list', methods=['GET'])
def employee_list():
    logger.info('employee_list')
    headers = request.headers
    checked_headers = check_headers(headers=headers, route_name="employee/list")
    if checked_headers['status'] == 'error':
        return checked_headers

    token_verification = verify_token(headers['Token'])
    if len(token_verification) > 0:
        return jsonify(token_verification)

    fields = config['list_fields']['Employee']
    if 'Id-Establishments' in headers.keys():
        establishments_id = headers['Id-Establishments'].split(',')
        query = query_creator(fields=fields, table='SALARIES', validity_date=True, extra=[f"IDSOCIETE = {headers['Id-Company']}",
                                                                                          f"""CODETAB in ('{"', '".join(establishments_id)}')"""])
    else:
        query = query_creator(fields=fields, table='SALARIES', validity_date=True, extra=[f"IDSOCIETE = {headers['Id-Company']}"])
    info = execute_and_format_query(query=query, cursor=cursor_mysql)
    if len(info) == 0:
        return jsonify({"status": "error", "code": 404, "message": "Data not found."})
    info = date_to_timestamp(info)
    return jsonify({"status": "ok", "code": 200, "data": info})


@app.route('/employee/info', methods=['GET'])
def employee_info():
    logger.info('employee_info')
    headers = request.headers
    checked_headers = check_headers(headers=headers, route_name="employee/info")
    if checked_headers['status'] == 'error':
        return checked_headers

    token_verification = verify_token(headers['Token'])
    if len(token_verification) > 0:
        return jsonify(token_verification)

    fields = create_fields('Employee', headers)
    if fields['status'] == 'error':
        return fields
    fields = fields['data']
    extra = [f"IDSOCIETE = {headers['Id-Company']}",
             f"""CODSALARIE in ('{"', '".join(headers['Id-Employees'].split(','))}')"""]
    if 'Id-Establishments' in headers.keys():
        extra.append(f"""CODETAB in ('{"', '".join(headers['Id-Establishments'].split(','))}')""")
    query = query_creator(fields=fields, table='SALARIES', validity_date=True, extra=extra)
    info = execute_and_format_query(query=query, cursor=cursor_mysql)
    if len(info) == 0:
        return jsonify({"status": "error", "code": 404, "message": "Data not found."})
    info = date_to_timestamp(info)
    return jsonify({"status": "ok", "code": 200, "data": info})


@app.route('/report/list', methods=['GET'])
def report_list():
    logger.info('report_list')
    headers = request.headers
    checked_headers = check_headers(headers=headers, route_name="report/list")
    if checked_headers['status'] == 'error':
        return checked_headers

    token_verification = verify_token(headers['Token'])
    if len(token_verification) > 0:
        return jsonify(token_verification)

    fields = config['list_fields']['Report']

    extra = [f"IDSOCIETE = {headers['Id-Company']}"]
    if 'Id-Employees' in headers.keys():
        extra.append(f"""CODSALARIE in ('{"', '".join(headers['Id-Employees'].split(','))}')""")
    if 'Years' in headers.keys():
        extra.append(f"""CODEXERCICE in ('{"', '".join(headers['Years'].split(','))}')""")
    if 'Months' in headers.keys():
        extra.append(f"""CODPERIODE in ('{"', '".join(headers['Months'].split(','))}')""")
    if 'Id-Establishments' in headers.keys():
        extra.append(f"""CODETAB in ('{"', '".join(headers['Id-Establishments'].split(','))}')""")

    query = query_creator(fields=fields, table='BULLETINS', extra=extra)
    info = execute_and_format_query(query=query, cursor=cursor_mysql)
    if len(info) == 0:
        return jsonify({"status": "error", "code": 404, "message": "Data not found."})
    info = date_to_timestamp(info)
    return jsonify({"status": "ok", "code": 200, "data": info})


@app.route('/report/info', methods=['GET'])
def report_info():
    logger.info('report_info')
    headers = request.headers
    checked_headers = check_headers(headers=headers, route_name="report/info")
    if checked_headers['status'] == 'error':
        return checked_headers

    token_verification = verify_token(headers['Token'])
    if len(token_verification) > 0:
        return jsonify(token_verification)

    fields = create_fields('Report', headers)
    if fields['status'] == 'error':
        return fields
    fields = fields['data']

    extra = [f"IDSOCIETE = {headers['Id-Company']}"]
    if 'Id-Employees' in headers.keys():
        extra.append(f"""CODSALARIE in ('{"', '".join(headers['Id-Employees'].split(','))}')""")
    if 'Years' in headers.keys():
        extra.append(f"""CODEXERCICE in ('{"', '".join(headers['Years'].split(','))}')""")
    if 'Months' in headers.keys():
        extra.append(f"""CODPERIODE in ('{"', '".join(headers['Months'].split(','))}')""")
    if 'Id-Establishments' in headers.keys():
        extra.append(f"""CODETAB in ('{"', '".join(headers['Id-Establishments'].split(','))}')""")

    query = query_creator(fields=fields, table='BULLETINS', extra=extra)
    info = execute_and_format_query(query=query, cursor=cursor_mysql)
    if len(info) == 0:
        return jsonify({"status": "error", "code": 404, "message": "Data not found."})
    info = date_to_timestamp(info)
    return jsonify({"status": "ok", "code": 200, "data": info})


@app.route('/report/details', methods=['GET'])
def report_details():
    logger.info('report_info')
    headers = request.headers
    checked_headers = check_headers(headers=headers, route_name="report/details")
    if checked_headers['status'] == 'error':
        return checked_headers

    token_verification = verify_token(headers['Token'])
    if len(token_verification) > 0:
        return jsonify(token_verification)

    fields = create_fields('Report details', headers)
    if fields['status'] == 'error':
        return fields
    fields = fields['data']
    extra = [f"IDSOCIETE = {headers['Id-Company']}",
             f"""CODSALARIE in ('{"', '".join(headers['Id-Employees'].split(','))}')""",
             f"""CODEXERCICE in ('{"', '".join(headers['Years'].split(','))}')""",
             f"""CODPERIODE in ('{"', '".join(headers['Months'].split(','))}')"""]
    query = query_creator(fields=fields, table='BULLETINSDETAIL', extra=extra)
    info = execute_and_format_query(query=query, cursor=cursor_mysql)
    if len(info) == 0:
        return jsonify({"status": "error", "code": 404, "message": "Data not found."})

    data = dict()
    for i in info:
        if i['CODSALARIE'] not in data.keys():
            data[i['CODSALARIE']] = dict()
            data[i['CODSALARIE']][i['CODEXERCICE']] = dict()
            data[i['CODSALARIE']][i['CODEXERCICE']][i['CODPERIODE']] = list()
        elif i['CODEXERCICE'] not in data[i['CODSALARIE']].keys():
            data[i['CODSALARIE']][i['CODEXERCICE']] = dict()
            data[i['CODSALARIE']][i['CODEXERCICE']][i['CODPERIODE']] = list()
        elif i['CODPERIODE'] not in data[i['CODSALARIE']][i['CODEXERCICE']].keys():
            data[i['CODSALARIE']][i['CODEXERCICE']][i['CODPERIODE']] = list()
        data[i['CODSALARIE']][i['CODEXERCICE']][i['CODPERIODE']].append(i)
    data = date_to_timestamp(data)
    return jsonify({"status": "ok", "code": 200, "data": data})


if __name__ == '__main__':
    logger.debug('main')
    app.run()
