from tkinter.messagebox import NO
import requests
import os
import sys
import time

from dotenv import load_dotenv

load_dotenv()

##################
DEBUG = False
JIRA_SESSION_ID = os.getenv('JSESSIONID')
BASE_URL = os.getenv('BASE_URL')
NR_OF_DEVELOPERS = os.getenv('NR_OF_DEVELOPERS')

COOKIES = {'JSESSIONID': JIRA_SESSION_ID}
##################


# def get_url_to_vote(story_nr, sp):
#     formated = f'{BASE_URL}/IAC-{story_nr}/card/{sp}'
#     return formated

STORIES = []


def get_url_with_votes(story_nr: str):
    formated = f'{BASE_URL}/IAC-{story_nr}'
    return formated


if __name__ == '__main__':
    print(NR_OF_DEVELOPERS)
    if JIRA_SESSION_ID is None or NR_OF_DEVELOPERS is None:
        sys.exit('Session ID / Nr of developers is not stored / update .env file')

    story = input("Enter story number: ")
    url = get_url_with_votes(story)
    while True:
        time.sleep(1)
        r = requests.get(url, cookies=COOKIES)
        if r.status_code == 200:
            res = r.json()
            bounded = res['boundedVotes']
            print(bounded)
        else:
            sys.exit('Poker session not found / started')
