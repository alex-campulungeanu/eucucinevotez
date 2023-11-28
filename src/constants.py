import os
from dotenv import load_dotenv

load_dotenv()

ROOT_DIR = os.path.abspath(os.curdir)

MAX_RETRYS_REQUEST = 150
JIRA_SESSION_ID = os.getenv('JSESSIONID')
BASE_URL = os.getenv('BASE_URL')

LAST_VOTE_KEY_STORAGE = 'eucucinevotez.last_vote'
WAIT_SECONDS = 2
NR_OF_DEVELOPERS = os.getenv('NR_OF_DEVELOPERS', 10)
