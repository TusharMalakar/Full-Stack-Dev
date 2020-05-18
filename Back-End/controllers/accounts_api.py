import security.cypher
from flask import Blueprint
import services.accounts_services as ac_service


account_api = Blueprint('account_api', __name__)


@account_api.route("/", methods=['GET'])
@security.cypher.requires_auth
def getallaccounts():
    return ac_service.getallaccounts()