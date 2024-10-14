import os
from dotenv import load_dotenv
from adminconsult.api import ClientCredentialsJsonFile
load_dotenv('.env')

def get_cred_json(client: str = 'val') -> ClientCredentialsJsonFile:

    admin_cred = ClientCredentialsJsonFile(file_path=os.path.join(os.environ.get('credentials_dir'), 'adminconsult_api_{}.json'.format(client)))

    return admin_cred
