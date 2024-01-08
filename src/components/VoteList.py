from datetime import datetime
import flet as ft
from typing import List

from typed_dict import VoteStructure


class VoteList:
    def __init__(self, vote_list: List[VoteStructure], story):
        self.vote_list: List[VoteStructure] = vote_list
        self.story = story

    def get_most_votes(self) -> VoteStructure:
        highest_vote: VoteStructure = {'count': 0, 'value': 0}
        for vote in self.vote_list:
            if highest_vote is None:
                highest_vote = vote
            else:
                if highest_vote['count'] < vote['count']:
                    highest_vote = vote
                elif highest_vote['count'] == vote['count'] and int(highest_vote['value']) < int(vote['value']):
                    highest_vote = vote
        return highest_vote

    def get_nr_of_votes(self) -> int:
        count = 0
        for vote in self.vote_list:
            count += vote['count']
        return count

    def get_colored_output(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        biggest = self.get_most_votes()
        colored_row = ft.Row(expand=True, spacing=5)
        for vote in self.vote_list:
            if vote['value'] == biggest['value']:
                colored_row.controls.append(ft.Text(str(vote), color='red'))
            else:
                colored_row.controls.append(ft.Text(str(vote)))
        res = ft.Row([ft.Text(f"IAC-{self.story} # {current_time} #"), colored_row])
        return res
