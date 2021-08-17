# -*- coding: utf-8 -*-
from loguru import logger

from flask import Blueprint, request, jsonify

from pegase3_api.routes_tools import *
from pegase3_api.global_variables import *
from pegase3_api.query_manager import query_creator

bp = Blueprint('report', __name__, url_prefix='/report')


@bp.route('/list', methods=['GET'])
def report_list():
    logger.info('report_list')
    headers = request.headers
    checked_headers = check_headers(headers=headers, route_name="report/list")
    if checked_headers['status'] == 'error':
        return jsonify(checked_headers), checked_headers['code']

    token_verification = verify_token(headers['Token'])
    if len(token_verification) > 0:
        return jsonify(token_verification), token_verification["code"]

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
        return jsonify({"status": "error", "code": 404, "message": "Data not found.", "token": create_token(jwt.decode(headers['Token'], 'WEB_SERVICE_API', algorithms='HS256')['user'])}), 404
    info = date_to_timestamp(info)
    return jsonify({"status": "success", "code": 200, "data": info, "token": create_token(jwt.decode(headers['Token'], 'WEB_SERVICE_API', algorithms='HS256')['user'])}), 200


@bp.route('/info', methods=['GET'])
def report_info():
    logger.info('report_info')
    headers = request.headers
    checked_headers = check_headers(headers=headers, route_name="report/info")
    if checked_headers['status'] == 'error':
        return jsonify(checked_headers), checked_headers['code']

    token_verification = verify_token(headers['Token'])
    if len(token_verification) > 0:
        return jsonify(token_verification), token_verification["code"]

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
        return jsonify({"status": "error", "code": 404, "message": "Data not found.", "token": create_token(jwt.decode(headers['Token'], 'WEB_SERVICE_API', algorithms='HS256')['user'])}), 404
    info = date_to_timestamp(info)
    return jsonify({"status": "success", "code": 200, "data": info, "token": create_token(jwt.decode(headers['Token'], 'WEB_SERVICE_API', algorithms='HS256')['user'])}), 200


@bp.route('/details', methods=['GET'])
def report_details():
    logger.info('report_info')
    headers = request.headers
    checked_headers = check_headers(headers=headers, route_name="report/details")
    if checked_headers['status'] == 'error':
        return jsonify(checked_headers), checked_headers['code']

    token_verification = verify_token(headers['Token'])
    if len(token_verification) > 0:
        return jsonify(token_verification), token_verification["code"]

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
        return jsonify({"status": "error", "code": 404, "message": "Data not found.", "token": create_token(jwt.decode(headers['Token'], 'WEB_SERVICE_API', algorithms='HS256')['user'])}), 404

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
    return jsonify({"status": "success", "code": 200, "data": data, "token": create_token(jwt.decode(headers['Token'], 'WEB_SERVICE_API', algorithms='HS256')['user'])}), 200


