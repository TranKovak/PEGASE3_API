# -*- coding: utf-8 -*-
import json
import pickle


def dump_configuration(config: dict = None):
    if config is None:
        config = {"users": [{'name': 'user_test', 'password': 'password_test'}]}
    pickle.dump(config, open("./pegase3_api/users.p", "wb"))


def load_configuration():
    configuration = pickle.load(open("./pegase3_api/users.p", "rb"))
    return configuration


def load_json_configuration() -> dict:
    with open('config.json', 'r') as config_file:
        config_data = json.load(config_file)
        return config_data
