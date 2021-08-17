# -*- coding: utf-8 -*-
import jwt
import datetime

from loguru import logger

from pegase3_api.global_variables import *
from pegase3_api.global_variables import config


def execute_and_format_query(query: str, cursor, debug=False, fetchone=False) -> list or None:
    if debug:
        logger.debug(query)
    cursor.execute(query)
    columns = [desc[0] for desc in cursor.description]
    rows = []
    if fetchone:
        row = cursor.fetchone()
        return dict(zip(columns, row)) if row else None
    else:
        for row in cursor.fetchall():
            data = dict(zip(columns, row))
            rows.append(data)
        return rows


def create_fields(table: str, headers: dict) -> dict:
    if 'Fields' in headers.keys():
        fields = headers['Fields'].split(',')
        for field in fields:
            if field not in config['tables_fields'][table]:
                return {"status": "error", "code": 404, "message": f"Field <{field}> not found.", "token": create_token(jwt.decode(headers['Token'], 'WEB_SERVICE_API', algorithms='HS256')['user'])}
    else:
        fields = config['tables_fields'][table]

    for m in config['mandatory_fields'][table]:
        if m not in fields:
            fields.append(m)

    return {"status": "ok", "code": 200, "data": fields}


def check_headers(headers: dict, route_name: str) -> dict:
    for mandatory_header in config['mandatory_headers'][route_name]:
        if mandatory_header not in headers.keys():
            return {"status": "error", "code": 402, "message": f"Required field <{mandatory_header}> is not specified.", "token": create_token(jwt.decode(headers['Token'], 'WEB_SERVICE_API', algorithms='HS256')['user'])}
    for key in headers.keys():
        if len(headers[key]) == 0:
            return {"status": "error", "code": 402, "message": f"Required field <{key}> is empty.", "token": create_token(jwt.decode(headers['Token'], 'WEB_SERVICE_API', algorithms='HS256')['user'])}
    return {"status": "ok", "code": 200, "message": f"All the required field are specified.", "token": create_token(jwt.decode(headers['Token'], 'WEB_SERVICE_API', algorithms='HS256')['user'])}


def date_to_timestamp(data: dict or list) -> dict or list:
    if type(data) == dict:
        for key in data.keys():
            t = type(data[key])
            if t == datetime.datetime:
                if data[key] >= datetime.datetime(day=1, month=1, year=1970):
                    data[key] = datetime.datetime.timestamp(data[key])
            elif t == dict or t == list:
                data[key] = date_to_timestamp(data[key])
    elif type(data) == list:
        for d in data:
            t = type(d)
            if t == datetime.datetime and d >= datetime.datetime(day=1, month=1, year=1970):
                d = datetime.datetime.timestamp(d)
            elif t == dict or t == list:
                d = date_to_timestamp(d)
    return data


def verify_token(token):
    try:
        jwt.decode(token, 'WEB_SERVICE_API', algorithms='HS256')
    except jwt.exceptions.InvalidSignatureError or jwt.exceptions.InvalidTokenError:
        return {'status': 'error', 'message': 'Token is not valid.', 'code': 401}
    except jwt.exceptions.ExpiredSignatureError:
        return {'status': 'error', 'message': 'Token has expired.', 'code': 498}
    query = f'''SELECT * FROM blacklist'''
    blacklist = execute_and_format_query(query=query, cursor=cursor_mysql)
    for blacklisted_token in blacklist:
        if blacklisted_token['bl_token'] == token:
            return {'status': 'error', 'message': 'Token is not valid.', 'code': 401}
    return ''


def create_token(user: str):
    token = jwt.encode({'user': user, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=config['token']['duration'])}, 'WEB_SERVICE_API')
    return token


def token_to_blacklist(token):
    decoded_token = jwt.decode(token, 'WEB_SERVICE_API', algorithms='HS256')
    query = f'''
    INSERT INTO blacklist (bl_token, bl_expiring_date, bl_user)
    VALUES ('{token}', '{datetime.datetime.fromtimestamp(decoded_token['exp'])}', '{decoded_token['user']}')
    '''
    cursor_mysql.execute(query=query)
    connect_mysql.commit()
    clear_expired_token_from_blacklist()


def clear_expired_token_from_blacklist():
    query = f'''
    DELETE FROM blacklist 
    WHERE bl_expiring_date < NOW()
    '''
    cursor_mysql.execute(query=query)
    connect_mysql.commit()
