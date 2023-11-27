from typing import Tuple, List, Dict
import requests

from constants import BASE_URL
from logger_service import logger
from typed_dict import VoteStructure

# TODO: check if i can get session id flobaly from somewhere
def create_cookie(session_id: str) -> dict:
    cookies = {
        'JSESSIONID': session_id,
    }
    return cookies

def refactor_response(resp: list) -> List[VoteStructure]:
    reformatted = [{"value": item['value'], "count": item['count']} for item in resp]
    return reformatted

def fetch_votes(story_nr: str, session_id: str) -> Tuple[bool, List[VoteStructure]]:
    # from utils import generate_random
    # return True, refactor_response([
    #                 { "value": 2, "count": generate_random(1, 3), "assignable": 'true' },
    #                 { "value": 1, "count": generate_random(1, 3), "assignable": 'true' },
    #                 { "value": 12, "count": generate_random(1, 3), "assignable": 'true' },
    #                 { "value": 9, "count": generate_random(1, 3), "assignable": 'true' },
    #                 { "value": 11, "count": generate_random(1, 3), "assignable": 'true' },
    #                 # { "value": 5, "count": generate_random(1, 3), "assignable": 'true' },
    #                 # { "value": 3, "count": generate_random(1, 3), "assignable": 'true' },
    #                 # { "value": 7, "count": generate_random(1, 3), "assignable": 'true' },
    #             ])
    formatted_url = f'{BASE_URL}/IAC-{story_nr}'
    r = requests.get(formatted_url, cookies=create_cookie(session_id))
    if r.status_code == 200:
        res = r.json()
        bounded = res['boundedVotes']
        logger.debug(bounded)
        refactored = refactor_response(bounded)
        return True, refactored
    else:
        logger.error(f"Status code when fetching votes {r.status_code}")
        return False, []
    
def set_vote(story_nr: str, sp: str, session_id: str) -> bool:
    url = f'{BASE_URL}/IAC-{story_nr}/card/{sp}'
    logger.info(f'Voting for: {story_nr} with SP: {sp}')
    r = requests.post(url, cookies=create_cookie(session_id))
    if r.status_code == 200:
        return True
    else:
        return False
        