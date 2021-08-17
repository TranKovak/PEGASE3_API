# -*- coding: utf-8 -*-
from loguru import logger

from flask import Blueprint, request, jsonify

from pegase3_api.routes_tools import *
from pegase3_api.global_variables import *

bp = Blueprint('authentification', __name__, url_prefix='/')


@bp.route('signup')
def signup():
    headers = request.headers
    checked_headers = check_headers(headers=headers, route_name="signup")
    if checked_headers['status'] == 'error':
        return jsonify(checked_headers), checked_headers['code']

    if headers['Password'] != config['super_user']['password'] or headers['User-Name'] != config['super_user']['user-name']:
        return jsonify({'status': 'error', 'code': 401, 'message': 'Super user doesn\'t exists.', "token": create_token(jwt.decode(headers['Token'], 'WEB_SERVICE_API', algorithms='HS256')['user'])}), 401

    for user in config_users['users']:
        logger.warning(user)
        if user['name'] == headers['New-User-Name']:
            return jsonify({'status': 'error', 'code': 400, 'message': 'User already exists.', "token": create_token(jwt.decode(headers['Token'], 'WEB_SERVICE_API', algorithms='HS256')['user'])}), 400

    config_users['users'].append({'name': headers['New-User-Name'], 'password': headers['New-User-Password']})
    dump_configuration(config_users)
    return jsonify({'status': 'success', 'code': 201, 'message': 'User created.', "token": create_token(jwt.decode(headers['Token'], 'WEB_SERVICE_API', algorithms='HS256')['user'])}), 201


@bp.route('login')
def login():
    auth = request.headers
    checked_headers = check_headers(headers=auth, route_name="login")
    if checked_headers['status'] == 'error':
        return jsonify(checked_headers), checked_headers['code']

    if auth and auth['Password'] and auth['User-Name']:
        for user in config_users['users']:
            logger.warning(user)
            if user['password'] == auth['Password'] and user['name'] == auth['User-Name']:
                token = create_token(user=auth['User-Name'])
                return jsonify({'status': 'success', 'code': 200, 'token': token, "token": create_token(jwt.decode(headers['Token'], 'WEB_SERVICE_API', algorithms='HS256')['user'])}), 200
    return jsonify({'message': 'Password or User-Name not correct.', 'code': 401, 'status': 'error', "token": create_token(jwt.decode(headers['Token'], 'WEB_SERVICE_API', algorithms='HS256')['user'])}), 401
