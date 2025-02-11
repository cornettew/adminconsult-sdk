from adminconsult.api.clientcredentials import ClientCredentials
from .local_json import get_cred_json
from .hashicorp_vault import get_cred_hvac

def get_cred() -> ClientCredentials:

    admin_cred = get_cred_json(client='tst')
    return admin_cred
