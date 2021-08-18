# -*- coding: utf-8 -*-
from loguru import logger

from flask import Blueprint, request, jsonify, current_app

from pegase3_api.routes_tools import *
from pegase3_api.global_variables import *
from pegase3_api.query_manager import query_creator

bp = Blueprint('company', __name__, url_prefix='/company')


@bp.route('/info', methods=['GET'])
def company_info():
    logger.info('company_info')
    headers = request.headers
    checked_headers = check_headers(headers=headers, route_name="company/info")
    if checked_headers['status'] == 'error':
        return jsonify(checked_headers), checked_headers['code']

    token_verification = verify_token(headers['Token'])
    if len(token_verification) > 0:
        return jsonify(token_verification), token_verification["code"]

    fields = create_fields('Company', headers)
    if fields['status'] == 'error':
        return fields
    fields = fields['data']
    query = query_creator(fields=fields, table='SOCIETE', validity_date=True, extra=[f"CODSOCIETE = '{headers['Name-Company']}'"])
    info = execute_and_format_query(query=query, cursor=cursor_mysql)
    if len(info) == 0:
        return jsonify({"status": "error", "code": 404, "message": "Data not found.", "token": create_token(jwt.decode(headers['Token'], current_app.config['SECRET_KEY'], algorithms='HS256')['user'], headers['Token'])}), 404
    info[0] = date_to_timestamp(info[0])
    return jsonify({"status": "success", "code": 200, "data": info[0], "token": create_token(jwt.decode(headers['Token'], 'WEB_SERVICE_API', algorithms='HS256')['user'], headers['Token'])}), 200


@bp.route('/holidays', methods=['GET'])
def company_holidays():
    logger.info('company_holidays')
    headers = request.headers
    checked_headers = check_headers(headers=headers, route_name="company/holidays")
    if checked_headers['status'] == 'error':
        return jsonify(checked_headers), checked_headers['code']

    token_verification = verify_token(headers['Token'])
    if len(token_verification) > 0:
        return jsonify(token_verification), token_verification["code"]

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
        return jsonify({"status": "error", "code": 404, "message": "Data not found.", "token": create_token(jwt.decode(headers['Token'], current_app.config['SECRET_KEY'], algorithms='HS256')['user'], headers['Token'])}), 404

    info = date_to_timestamp(info)

    return jsonify({"status": "success", "code": 200, "data": info, "token": create_token(jwt.decode(headers['Token'], current_app.config['SECRET_KEY'], algorithms='HS256')['user'], headers['Token'])}), 200


@bp.route('/sections', methods=['GET'])
def company_sections():
    logger.info('company_sections')
    headers = request.headers
    checked_headers = check_headers(headers=headers, route_name="company/sections")
    if checked_headers['status'] == 'error':
        return jsonify(checked_headers), checked_headers['code']

    token_verification = verify_token(headers['Token'])
    if len(token_verification) > 0:
        return jsonify(token_verification), token_verification["code"]

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
        return jsonify({"status": "error", "code": 404, "message": "Data not found.", "token": create_token(jwt.decode(headers['Token'], current_app.config['SECRET_KEY'], algorithms='HS256')['user'], headers['Token'])}), 404
    sections = date_to_timestamp(sections)
    return jsonify({"status": "success", "code": 200, "data": sections, "token": create_token(jwt.decode(headers['Token'], current_app.config['SECRET_KEY'], algorithms='HS256')['user'], headers['Token'])}), 200
