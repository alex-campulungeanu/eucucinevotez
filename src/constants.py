import os
from dotenv import load_dotenv

load_dotenv()

MAX_RETRYS_REQUEST = 30
JIRA_SESSION_ID = os.getenv('JSESSIONID')
BASE_URL = os.getenv('BASE_URL')