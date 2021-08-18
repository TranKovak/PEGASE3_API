# -*- coding: utf-8 -*-
from loguru import logger

from flask import Blueprint, request, jsonify, current_app

from pegase3_api.routes_tools import *
from pegase3_api.global_variables import *
from pegase3_api.query_manager import query_creator

bp = Blueprint('employee', __name__, url_prefix='/employee')


@bp.route('/list', methods=['GET'])
def employee_list():
    logger.info('employee_list')
    headers = request.headers
    checked_headers = check_headers(headers=headers, route_name="employee/list")
    if checked_headers['status'] == 'error':
        return jsonify(checked_headers), checked_headers['code']

    token_verification = verify_token(headers['Token'])
    if len(token_verification) > 0:
        return jsonify(token_verification), token_verification["code"]

    fields = config['list_fields']['Employee']
    if 'Id-Establishments' in headers.keys():
        establishments_id = headers['Id-Establishments'].split(',')
        query = query_creator(fields=fields, table='SALARIES', validity_date=True, extra=[f"IDSOCIETE = {headers['Id-Company']}",
                                                                                          f"""CODETAB in ('{"', '".join(establishments_id)}')"""])
    else:
        query = query_creator(fields=fields, table='SALARIES', validity_date=True, extra=[f"IDSOCIETE = {headers['Id-Company']}"])
    info = execute_and_format_query(query=query, cursor=cursor_mysql)
    if len(info) == 0:
        return jsonify({"status": "error", "code": 404, "message": "Data not found.", "token": create_token(jwt.decode(headers['Token'], current_app.config['SECRET_KEY'], algorithms='HS256')['user'], headers['Token'])}), 404
    info = date_to_timestamp(info)
    return jsonify({"status": "success", "code": 200, "data": info, "token": create_token(jwt.decode(headers['Token'], current_app.config['SECRET_KEY'], algorithms='HS256')['user'], headers['Token'])}), 200


@bp.route('/info', methods=['GET'])
def employee_info():
    logger.info('employee_info')
    headers = request.headers
    checked_headers = check_headers(headers=headers, route_name="employee/info")
    if checked_headers['status'] == 'error':
        return jsonify(checked_headers), checked_headers['code']

    token_verification = verify_token(headers['Token'])
    if len(token_verification) > 0:
        return jsonify(token_verification), token_verification["code"]

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
        return jsonify({"status": "error", "code": 404, "message": "Data not found.", "token": create_token(jwt.decode(headers['Token'], current_app.config['SECRET_KEY'], algorithms='HS256')['user'], headers['Token'])}), 404
    info = date_to_timestamp(info)
    return jsonify({"status": "success", "code": 200, "data": info, "token": create_token(jwt.decode(headers['Token'], current_app.config['SECRET_KEY'], algorithms='HS256')['user'], headers['Token'])}), 200
