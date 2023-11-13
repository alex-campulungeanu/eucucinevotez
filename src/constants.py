import os
from dotenv import load_dotenv

load_dotenv()

MAX_RETRYS_REQUEST = 80
JIRA_SESSION_ID = os.getenv('JSESSIONID')
BASE_URL = os.getenv('BASE_URL')

LAST_VOTE_KEY_STORAGE = 'eucucinevotez.last_vote'