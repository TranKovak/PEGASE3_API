# -*- coding: utf-8 -*-
from loguru import logger

from flask import Blueprint, request, jsonify, current_app

from pegase3_api.routes_tools import *
from pegase3_api.global_variables import *
from pegase3_api.query_manager import query_creator

bp = Blueprint('establishment', __name__, url_prefix='/establishment')


@bp.route('/list', methods=['GET'])
def establishment_list():
    logger.info('establishment_list')
    headers = request.headers
    checked_headers = check_headers(headers=headers, route_name="establishment/list")
    if checked_headers['status'] == 'error':
        return jsonify(checked_headers), checked_headers['code']

    token_verification = verify_token(headers['Token'])
    if len(token_verification) > 0:
        return jsonify(token_verification), token_verification["code"]

    fields = config['list_fields']['Establishment']
    query = query_creator(fields=fields, table='ETABLISSEMENTS', validity_date=True, extra=[f"IDSOCIETE = {headers['Id-Company']}"])
    info = execute_and_format_query(query=query, cursor=cursor_mysql)
    if len(info) == 0:
        return jsonify({"status": "error", "code": 404, "message": "Data not found.", "token": create_token(jwt.decode(headers['Token'], current_app.config['SECRET_KEY'], algorithms='HS256')['user'])}), 404
    info = date_to_timestamp(info)
    return jsonify({"status": "success", "code": 200, "data": info, "token": create_token(jwt.decode(headers['Token'], current_app.config['SECRET_KEY'], algorithms='HS256')['user'])}), 200


@bp.route('/info', methods=['GET'])
def establishment_info():
    logger.info('establishment_info')
    headers = request.headers
    checked_headers = check_headers(headers=headers, route_name="establishment/info")
    if checked_headers['status'] == 'error':
        return jsonify(checked_headers), checked_headers['code']

    token_verification = verify_token(headers['Token'])
    if len(token_verification) > 0:
        return jsonify(token_verification), token_verification["code"]

    fields = create_fields('Establishment', headers)
    if fields['status'] == 'error':
        return fields
    fields = fields['data']
    establishments_id = headers['Id-Establishments'].split(',')
    query = query_creator(fields=fields, table='ETABLISSEMENTS', validity_date=True, extra=[f"IDSOCIETE = {headers['Id-Company']}",
                                                                                            f"CODETAB in ({', '.join(establishments_id)})"])
    info = execute_and_format_query(query=query, cursor=cursor_mysql)
    if len(info) == 0:
        return jsonify({"status": "error", "code": 404, "message": "Data not found.", "token": create_token(jwt.decode(headers['Token'], current_app.config['SECRET_KEY'], algorithms='HS256')['user'])}), 404
    info = date_to_timestamp(info)
    return jsonify({"status": "success", "code": 200, "data": info, "token": create_token(jwt.decode(headers['Token'], current_app.config['SECRET_KEY'], algorithms='HS256')['user'])}), 200
