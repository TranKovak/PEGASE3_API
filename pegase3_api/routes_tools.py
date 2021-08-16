# -*- coding: utf-8 -*-
import datetime

from loguru import logger

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
                return {"status": "error", "code": 404, "message": f"Field <{field}> not found."}
    else:
        fields = config['tables_fields'][table]

    for m in config['mandatory_fields'][table]:
        if m not in fields:
            fields.append(m)

    return {"status": "ok", "code": 200, "data": fields}


def check_headers(headers: dict, route_name: str) -> dict:
    for mandatory_header in config['mandatory_headers'][route_name]:
        if mandatory_header not in headers.keys():
            return {"status": "error", "code": 402, "message": f"Required field <{mandatory_header}> is not specified."}
    for key in headers.keys():
        if len(headers[key]) == 0:
            return {"status": "error", "code": 402, "message": f"Required field <{key}> is empty."}
    return {"status": "ok", "code": 200, "message": f"All the required field are specified."}


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
