from json import load
import os
from dotenv import load_dotenv

load_dotenv()

JIRA_SESSION_ID = os.getenv('JSESSIONID')
BASE_URL = os.getenv('BASE_URL')