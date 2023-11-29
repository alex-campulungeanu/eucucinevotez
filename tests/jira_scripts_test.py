from src.jira_scripts import create_cookie, refactor_response
from src.utils import generate_random


def test_create_cookie():
    fake_session = "123456"
    cookie = create_cookie(fake_session)
    assert cookie == {'JSESSIONID': fake_session}


def test_refactor_response():
    jira_vote_list = [
        {"value": 2, "count": 1, "assignable": 'true'},
        {"value": 1, "count": 2, "assignable": 'true'},
        {"value": 12, "count": 1, "assignable": 'true'},
        {"value": 9, "count": 3, "assignable": 'true'},
    ]

    refactored = refactor_response(jira_vote_list)
    assert refactored == [
        {"value": 2, "count": 1},
        {"value": 1, "count": 2},
        {"value": 12, "count": 1},
        {"value": 9, "count": 3},
    ]
