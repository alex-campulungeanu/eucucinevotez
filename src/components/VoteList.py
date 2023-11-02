from datetime import datetime
import flet as ft
from typing import List, Dict

class VoteList(ft.UserControl):
    def __init__(self, vote_list: List[Dict[str, str]], story):
        self.vote_list = vote_list
        self.story = story
    
    def get_highest(self):
        highest_vote = {}
        for vote in self.vote_list:
            if highest_vote == {}:
                highest_vote = vote
            else:
                if highest_vote['count'] < vote['count']:
                    highest_vote = vote
                elif highest_vote['count'] == vote['count'] and int(highest_vote['value']) < int(vote['value']):
                    highest_vote = vote
        return highest_vote
    
    def color(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        biggest = self.get_highest()
        colored_row = ft.Row(expand=True, spacing=5)
        for vote in self.vote_list:
            if vote['value'] == biggest['value']:
                colored_row.controls.append(ft.Text(vote, color='red'))
            else:
                colored_row.controls.append(ft.Text(vote))
        res = ft.Row(
            [
                ft.Text(f"IAC-{self.story} # {current_time} #"),
                colored_row
            ]
        )
        return res