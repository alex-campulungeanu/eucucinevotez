from typing import List
from src.components.VoteList import VoteList
from typed_dict import VoteStructure


def test_highest():
    story = 1234
    vote_list: List[VoteStructure] = [
        {"value": 6, "count": 1},
        {"value": 3, "count": 6},
        {"value": 7, "count": 2},
        {"value": 10, "count": 2},
        {"value": 4, "count": 2},
    ]
    vl = VoteList(story=story, vote_list=vote_list)
    highest: VoteStructure = vl.get_most_votes()
    total_votes = vl.get_nr_of_votes()

    assert highest == {"value": 3, "count": 6}
    assert total_votes == 1 + 6 + 2 + 2 + 2
