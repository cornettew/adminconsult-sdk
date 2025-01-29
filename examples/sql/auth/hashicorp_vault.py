from os import getenv
from dotenv import load_dotenv
from adminconsult.sql import ClientCredentialsHvac
load_dotenv('.env')

def get_cred_hvac(url: str = 'http://localhost:8200') -> ClientCredentialsHvac:

    admin_cred = ClientCredentialsHvac(url=url, token=getenv('VAULT_TOKEN'), mount_point='ward.cornette@rfn.fr')
    
    return admin_cred
