# -*- coding: utf-8 -*-
from loguru import logger


def query_creator(fields: list, table: str, validity_date: bool = False, limit: int = -1, offset: int = 0, extra: list = None):
    query = f'''
    SELECT {', '.join(fields)}
    FROM {table}
    {create_where_instructions(validity_date=validity_date, limit=limit, offset=offset, extra=extra)}
    '''
    logger.success(query)
    return query


def create_where_instructions(validity_date: bool = False, limit: int = -1, offset: int = 0, extra: list = None) -> str:
    if limit == -1 and offset == 0 and not validity_date and (extra is None or len(extra) == 0):
        return ''
    where_instructions = 'WHERE\n'
    if validity_date:
        if where_instructions == 'WHERE\n':
            where_instructions += 'DATDEBVALIDITE <= NOW() AND DATFINVALIDITE >= NOW()\n'
    for e in extra:
        if len(where_instructions) > 0 and where_instructions != 'WHERE\n':
            where_instructions += ' AND ' + e
        else:
            where_instructions += e
    if limit > 0:
        where_instructions += f'LIMIT {limit} '
        where_instructions += f'OFFSET {offset}'
    return where_instructions
