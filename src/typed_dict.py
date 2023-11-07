from typing import TypedDict

class VoteStructure(TypedDict, total=True):
    value: int
    count: int