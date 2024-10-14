from os import getenv
from dotenv import load_dotenv
from adminconsult.api import ClientCredentialsHvac
load_dotenv('.env')

def get_cred_hvac(url: str = 'http://localhost:8200') -> ClientCredentialsHvac:

    admin_cred = ClientCredentialsHvac(url=url, token=getenv('VAULT_TOKEN'), mount_point='C004640')
    
    return admin_cred
