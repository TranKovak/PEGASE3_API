# -*- coding: utf-8 -*-
from loguru import logger
from sqlalchemy import types

import json
import pickle


def dump_configuration(config: dict = None):
    companies = ["617", "754"]
    if config is None:
        configuration = {"fields": {"SOCIETE": ["IDSOCIETE", "CODSOCIETE", "NOMSOCIETE", "ADR1", "ADR2", "ADR3", "ADRCPOST", "ADRBDIST", "NUMSIREN", "NAF", "CODETABPRINCIPAL", "DATFINVALIDITE", "DATDEBVALIDITE"],
                                    "ETABLISSEMENTS": ["IDSOCIETE", "CODETAB", "NOMETAB", "ADR1", "ADR2", "ADR3", "ADRCPOST", "ADRBDIST", "NIC", "NAF", "NOMRESP", "QUALITERESP", "NOMSIGNATAIRE", "QUALITESIGNATAIRE", "DATFINVALIDITE", "DATDEBVALIDITE"],
                                    "SALARIES": ["IDSOCIETE", "NOM", "PRENOM", "ADR1", "ADR2", "ADR3", "ADRCPOST", "ADRBDIST", "NUMSECU", "EMPLOI", "CODSALARIE", "DATANCIENNETE", "DATFINVALIDITE", "DATDEBVALIDITE"],
                                    "BULLETINS": ["IDSOCIETE", "CODETAB", "CODSALARIE", "CODEXERCICE", "CODPERIODE", "DATDEBUTPAIE", "DATFINPAIE", "DATREMISEPAIE"],
                                    "BULLETINSDETAIL": ["IDSOCIETE", "CODETAB", "CODSALARIE", "CODEXERCICE", "CODPERIODE", "CODBULLETIN", "CODRUBRIQUE", "NOM"],
                                    "RUBRIQUES": ["IDSOCIETE", "CODRUBRIQUE", "CODPROFIL", "NOM", "ZONEBULLETIN", "DATFINVALIDITE", "DATDEBVALIDITE"],
                                    "JOURSFERIES_NAT": ["DATEJF"]},
                         "dtypes": {"SOCIETE": {"IDSOCIETE": types.Integer, "NOMSOCIETE": types.VARCHAR(length=50), "ADR1": types.VARCHAR(length=32), "ADR2": types.VARCHAR(length=32), "ADR3": types.VARCHAR(length=32), "ADRCPOST": types.VARCHAR(length=5), "ADRBDIST": types.VARCHAR(length=26), "NUMSIREN": types.VARCHAR(length=9), "NAF": types.VARCHAR(length=5), "CODETABPRINCIPAL": types.VARCHAR(length=5), "DATFINVALIDITE": types.DateTime, "DATDEBVALIDITE": types.DateTime},
                                    "ETABLISSEMENTS": {"IDSOCIETE": types.Integer, "CODETAB": types.VARCHAR(length=5), "NOMETAB": types.VARCHAR(length=50), "ADR1": types.VARCHAR(length=32), "ADR2": types.VARCHAR(length=32), "ADR3": types.VARCHAR(length=32), "ADRCPOST": types.VARCHAR(length=5), "ADRBDIST": types.VARCHAR(length=26), "NIC": types.VARCHAR(length=5), "NAF": types.VARCHAR(length=5), "NOMRESP": types.VARCHAR(length=30), "QUALITERESP": types.VARCHAR(length=30), "NOMSIGNATAIRE": types.VARCHAR(length=30), "QUALITESIGNATAIRE": types.VARCHAR(length=30), "DATFINVALIDITE": types.DateTime, "DATDEBVALIDITE": types.DateTime},
                                    "SALARIES": {"IDSOCIETE": types.Integer, "NOM": types.VARCHAR(length=50), "PRENOM": types.VARCHAR(length=25), "ADR1": types.VARCHAR(length=100), "ADR2": types.VARCHAR(length=100), "ADR3": types.VARCHAR(length=100), "ADRCPOST": types.VARCHAR(length=5), "ADRBDIST": types.VARCHAR(length=26), "NUMSECU": types.VARCHAR(length=15), "EMPLOI": types.VARCHAR(length=25), "CODSALARIE": types.VARCHAR(length=10), "DATANCIENNETE": types.DateTime, "DATFINVALIDITE": types.DateTime, "DATDEBVALIDITE": types.DateTime},
                                    "BULLETINS": {"IDSOCIETE": types.Integer, "CODETAB": types.VARCHAR(length=5), "CODSALARIE": types.VARCHAR(length=10), "CODEXERCICE": types.VARCHAR(length=4), "CODPERIODE": types.VARCHAR(length=2), "DATDEBUTPAIE": types.DateTime, "DATFINPAIE": types.DateTime, "DATREMISEPAIE": types.DateTime},
                                    "BULLETINSDETAIL": {"IDSOCIETE": types.Integer, "CODETAB": types.VARCHAR(length=5), "CODSALARIE": types.VARCHAR(length=10), "CODEXERCICE": types.VARCHAR(length=4), "CODPERIODE": types.VARCHAR(length=2), "CODBULLETIN": types.SMALLINT, "CODRUBRIQUE": types.VARCHAR(length=6), "NOM": types.VARCHAR(length=50)},
                                    "RUBRIQUES": {"IDSOCIETE": types.Integer, "CODRUBRIQUE": types.VARCHAR(length=6), "CODPROFIL": types.VARCHAR(length=5), "NOM": types.VARCHAR(length=50), "ZONEBULLETIN": types.SMALLINT},
                                    "JOURSFERIES_NAT": {"DATEJF": types.DateTime}
                                    },
                         "companies": ["617", "754"]
                         }
        pickle.dump(configuration, open("./configuration.p", "wb"))
    else:
        pickle.dump(config, open("./configuration.p", "wb"))


def load_configuration():
    configuration = pickle.load(open("./configuration.p", "rb"))
    return configuration
