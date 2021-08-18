# -*- coding: utf-8 -*-

from pegase3_api.global_variables import *

from pegase3_api.blueprints import report
from pegase3_api.blueprints import company
from pegase3_api.blueprints import employee
from pegase3_api.blueprints import establishment
from pegase3_api.blueprints import authentification

app = Flask(__name__, static_folder='static')

if __name__ == '__main__':
    logger.debug('main')

    app.config['SECRET_KEY'] = 'WEB_SERVICE_API'
    app.config['CLIENT_REPORT'] = "./"
    app.register_blueprint(report.bp)
    app.register_blueprint(company.bp)
    app.register_blueprint(employee.bp)
    app.register_blueprint(establishment.bp)
    app.register_blueprint(authentification.bp)

    app.run()
