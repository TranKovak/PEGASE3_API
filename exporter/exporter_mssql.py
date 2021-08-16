# -*- coding: utf-8 -*-
import pyodbc
import pandas as pd

from loguru import logger
from sqlalchemy import create_engine, types

from exporter.configuration_manager import *

conn_p3 = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=10.11.5.3;DATABASE=Pegase3prod;UID=P3_READONLY;PWD=ENz49ilPK8GcJQfp5VRP')
dump_configuration()
configuration = load_configuration()
engine = create_engine('mysql://root:root@localhost:3310/pegase3')


def company_exporter(fields: list, dtypes: dict):
    query = f"""
    SELECT
        {', '.join(fields)}
    FROM
        SOCIETE
    WHERE
        DATDEBVALIDITE <= GETDATE() AND DATFINVALIDITE >= GETDATE()
    """
    mssql_exporter(query=query, table='societe', if_exists='replace', dtype=dtypes)


def employee_exporter(fields: list, dtypes: dict):
    query = f"""
    SELECT
        {', '.join(fields)}
    FROM
        SALARIES
    WHERE
        DATDEBVALIDITE <= GETDATE() AND DATFINVALIDITE >= GETDATE()
    """
    mssql_exporter(query=query, table='salaries', if_exists='replace', dtype=dtypes)


def establishment_exporter(fields: list, dtypes: dict):
    query = f"""
    SELECT
        {', '.join(fields)}
    FROM
        ETABLISSEMENTS
    WHERE
        DATDEBVALIDITE <= GETDATE() AND DATFINVALIDITE >= GETDATE()
    """
    mssql_exporter(query=query, table='etablissements', if_exists='replace', dtype=dtypes)


def report_exporter(fields: list, companies: list, dtypes: dict):
    query = f"""
    SELECT
        {', '.join(fields)}
    FROM
        BULLETINS
    WHERE
        IDSOCIETE in ({', '.join(companies)})
    """
    mssql_exporter(query=query, table='bulletins', if_exists='replace', dtype=dtypes)


def report_details_exporter(fields: list, companies: list, dtypes: dict):
    for company in companies:
        query = f"""
        SELECT
            {', '.join(fields)}
        FROM
            BULLETINSDETAIL
        WHERE
            IDSOCIETE = {company}
        """
        if companies.index(company) == 0:
            mssql_exporter(query=query, table='bulletinsdetail', if_exists='replace', dtype=dtypes)
        else:
            mssql_exporter(query=query, table='bulletinsdetail', if_exists='append', dtype=dtypes)


def sections_exporter(fields: list, companies: list, dtypes: dict):
    query = f"""
            SELECT
                {', '.join(fields)}
            FROM 
                RUBRIQUES
            WHERE
                IDSOCIETE = 0 or IDSOCIETE in ({', '.join(companies)})
            """
    mssql_exporter(query=query, table='rubriques', if_exists='replace', dtype=dtypes)


def holidays_exporter(fields: list, dtypes: dict):
    query = f"""
    SELECT
        {', '.join(fields)}
    FROM
        JOURSFERIES_NAT
    WHERE
        DATEJF > '1970-01-01'
    """
    mssql_exporter(query=query, table='joursferies_nat', if_exists='replace', dtype=dtypes)


def mssql_exporter(query, table, if_exists, dtype):
    logger.info(table)
    logger.success(query)
    logger.warning(if_exists)
    sql_query = pd.read_sql_query(query, conn_p3)
    df = pd.DataFrame(sql_query)
    df.to_csv(f'C:\\Users\\GMercadal\\Documents\\Moi\\web_service_api_rest\\exporter\\csv\\{table}.csv', index=False, sep=';')
    df = pd.read_csv(f'C:\\Users\\GMercadal\\Documents\\Moi\\web_service_api_rest\\exporter\\csv\\{table}.csv', sep=';', quotechar='\'', encoding='utf8')
    df.to_sql(name=table, con=engine, index=False, if_exists=if_exists, dtype=dtype)


if __name__ == '__main__':
    logger.debug('main')
    sections_exporter(configuration['fields']['RUBRIQUES'], configuration['companies'], configuration['dtypes']['RUBRIQUES'])
    company_exporter(configuration['fields']['SOCIETE'], configuration['dtypes']['SOCIETE'])
    employee_exporter(configuration['fields']['SALARIES'], configuration['dtypes']['SALARIES'])
    establishment_exporter(configuration['fields']['ETABLISSEMENTS'], configuration['dtypes']['ETABLISSEMENTS'])
    report_exporter(configuration['fields']['BULLETINS'], configuration['companies'], configuration['dtypes']['BULLETINS'])
    report_details_exporter(configuration['fields']['BULLETINSDETAIL'], configuration['companies'], configuration['dtypes']['BULLETINSDETAIL'])
    holidays_exporter(configuration['fields']['JOURSFERIES_NAT'], configuration['dtypes']['JOURSFERIES_NAT'])
