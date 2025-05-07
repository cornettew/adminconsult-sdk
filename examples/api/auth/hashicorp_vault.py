from os import getenv
from dotenv import load_dotenv
from adminconsult.api import ClientCredentialsHvac
import urllib3
load_dotenv('.env')

def get_cred_hvac(url: str = 'http://localhost:8200') -> ClientCredentialsHvac:

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    admin_cred = ClientCredentialsHvac(url=url, token=getenv('VAULT_TOKEN'), mount_point=getenv('VAULT_MOUNT'))
    
    return admin_cred
