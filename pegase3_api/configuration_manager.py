# -*- coding: utf-8 -*-
import pickle

from loguru import logger


def dump_configuration(config: dict = None):
    if config is None:
        configuration = {"tables_fields": {"Company": ['IDSOCIETE', 'NOMSOCIETE', 'ADR1', 'ADR2', 'ADR3', 'ADRCPOST', 'ADRBDIST', 'NUMSIREN', 'NAF', 'CODETABPRINCIPAL'],
                                           "Establishment": ['CODETAB', 'NOMETAB', 'ADR1', 'ADR2', 'ADR3', 'ADRCPOST', 'ADRBDIST', 'NIC', 'NAF', 'NOMRESP', 'QUALITERESP', 'NOMSIGNATAIRE', 'QUALITESIGNATAIRE'],
                                           "Employee": ['NOM', 'PRENOM', 'ADR1', 'ADR2', 'ADR3', 'ADRCPOST', 'ADRBDIST', 'NUMSECU', 'EMPLOI', 'CODSALARIE', 'DATANCIENNETE'],
                                           "Report": ['CODETAB', 'CODSALARIE', 'CODEXERCICE', 'CODPERIODE', 'DATDEBUTPAIE', 'DATFINPAIE', 'DATREMISEPAIE'],
                                           "Report details": ['CODETAB', 'CODSALARIE', 'CODEXERCICE', 'CODBULLETIN', 'CODPERIODE', 'CODRUBRIQUE', 'NOM'],  # MANQUE MONTANT
                                           "Sections": ['CODRUBRIQUE', 'CODPROFIL', 'NOM', 'ZONEBULLETIN'],
                                           "Holidays": ['DATEJF']},
                         "list_fields": {"Establishment": ['CODETAB', 'NOMETAB'],
                                         "Employee": ['NOM', 'PRENOM', 'CODSALARIE', 'CODETAB'],
                                         "Report": ['CODETAB', 'CODSALARIE', 'CODEXERCICE', 'CODPERIODE']},
                         "mandatory_fields": {"Company": [],
                                              "Establishment": [],
                                              "Employee": [],
                                              "Report": [],
                                              "Report details": ['CODSALARIE', 'CODEXERCICE', 'CODPERIODE'],
                                              "Sections": ['CODRUBRIQUE'],
                                              "Holidays": ['DATEJF']},
                         "mandatory_headers": {"signup": ['User-Name', 'Password', 'New-User-Name', 'New-User-Password'],
                                               "login": ['User-Name', 'Password'],
                                               "company/info": ['Name-Company', 'Token'],
                                               "company/holidays": ['Token', 'Id-Company'],
                                               "company/sections": ['Id-Company', 'Token'],
                                               "establishment/list": ['Id-Company', 'Token'],
                                               "establishment/info": ['Id-Company', 'Id-Establishments', 'Token'],
                                               "employee/list": ['Id-Company', 'Token'],
                                               "employee/info": ['Id-Company', 'Id-Employees', 'Token'],
                                               "report/list": ['Id-Company', 'Token'],
                                               "report/info": ['Id-Company', 'Token'],
                                               "report/details": ['Id-Company', 'Years', 'Months', 'Id-Employees', 'Token']},
                         "super_user": {"user-name": "SUPER USER",
                                        "password": "SUPER PASSWORD"},
                         "users": [],
                         }
        pickle.dump(configuration, open("./pegase3_api/configuration.p", "wb"))
    else:
        pickle.dump(config, open("./pegase3_api/configuration.p", "wb"))


def load_configuration():
    configuration = pickle.load(open("./pegase3_api/configuration.p", "rb"))

    logger.warning('CONFIG:')
    for config in configuration['users']:
        logger.info(config)
    # logger.info(configuration['tables_fields'])
    logger.warning("--------------------------\n")

    return configuration
