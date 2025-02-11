from adminconsult.sql.clientcredentials import ClientCredentials
from .hashicorp_vault import get_cred_hvac
from .local_json import get_cred_json

def get_cred() -> ClientCredentials:

    admin_cred = get_cred_hvac(url='https://nx-vault.val.rfn.local')
    # admin_cred = get_cred_json(client='tst')
    return admin_cred
