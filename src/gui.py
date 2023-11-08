import flet as ft
import os
import time
from dotenv import load_dotenv
from datetime import datetime

from scripts import fetch_votes, set_vote
from logger_service import logger
from constants import JIRA_SESSION_ID, MAX_RETRYS_REQUEST
from components.VoteList import VoteList

load_dotenv() 

milking_jira = False
retrys_jira = 0

def main(page: ft.Page):
    # TODO: see if i create a module for this
    page.title = "Eu cu cine votez ?"
    page.window_width = 800
    page.window_height = 600
    page.window_left = 1767
    page.window_top = 0
    
    session_cookie_input = ft.TextField(hint_text="JIRA session cookie", width=400)
    session_cookie_input.value = JIRA_SESSION_ID
    story_nr_input = ft.TextField(hint_text="Story number", width=200)
    vote_input = ft.TextField(hint_text="SP", width=100)
    vote_list = ft.ListView(expand=True, spacing=10, padding=10)
    
    def refresh_cookie(e):
        logger.info(JIRA_SESSION_ID)
        session_cookie_input.value = JIRA_SESSION_ID
        page.update()
    
    def fill_vote_list():
        # current_time = datetime.now().strftime("%H:%M:%S")
        global milking_jira
        global retrys_jira
        if milking_jira:
            if story_nr_input.value != '' and session_cookie_input.value != '':
                status, votes = fetch_votes(story_nr_input.value, session_cookie_input.value)
                retrys_jira = retrys_jira + 1
                if retrys_jira == MAX_RETRYS_REQUEST:
                    milking_jira = False
                    page.show_snack_bar(
                        ft.SnackBar(ft.Text(f"Stoping the api calls after {MAX_RETRYS_REQUEST} retrys for {story_nr_input.value}!"), open=True, bgcolor='red')
                    )
                    logger.error(f"Stoping the api calls after {MAX_RETRYS_REQUEST} retrys for {story_nr_input.value}!")
                if not status:
                    logger.error(f'Vote fetching failed for {story_nr_input.value} !')
                    page.show_snack_bar(
                        ft.SnackBar(ft.Text("Error when calling fetch votes API !"), open=True, bgcolor='red')
                    )
                vl = VoteList(vote_list=votes, story=story_nr_input.value)
                logger.info(vl.color())
                biggest_vote = vl.get_highest()
                vote_input.value = str(biggest_vote['value'])
                # vote_list.controls.insert(0, ft.Text(f"IAC-{story_nr_input.value} # {current_time} #  {votes}", color='red'))
                vote_list.controls.insert(0, vl.color())
                logger.info(f'votes {votes}')
                page.update()
                time.sleep(2)
                fill_vote_list()
            else:
                page.show_snack_bar(
                    ft.SnackBar(ft.Text("Fill the story number first !"), open=True, bgcolor='red')
                )
                logger.error(f'Not all input values where given for fetching votes for {story_nr_input.value}')
                milking_jira = False
                votes = []  
    
    def give_vote(e):
        if story_nr_input.value != '' and vote_input.value != '' and session_cookie_input.value != '':
            res = set_vote(story_nr_input.value, vote_input.value, session_cookie_input.value)
            if res:
                # story_nr_input.value = ''
                # story_nr_input.update()
                vote_input.value = ''
                vote_input.update()
                page.show_snack_bar(
                    ft.SnackBar(ft.Text(f"Vote for {story_nr_input.value} success"), open=True, bgcolor='green')
                )
                logger.info(f'Vote success for {story_nr_input.value}')
            else:
                page.show_snack_bar(
                    ft.SnackBar(ft.Text(f"Vote failed for {story_nr_input.value} !"), open=True, bgcolor='red')
                )
                logger.error(f"Vote failed for {story_nr_input.value} when calling API !")
        else:
            page.show_snack_bar(
                    ft.SnackBar(ft.Text(f"Story number or SP not filled for {story_nr_input.value} !"), open=True, bgcolor='red')
                )
            logger.info(f"Story number or SP not filled for {story_nr_input.value} !")
    
    def start_milk_jira(e):
        global milking_jira
        milking_jira = True
        fill_vote_list()
        
    def stop_milk_jira(e):
        global milking_jira
        milking_jira = False
        # fill_vote_list() # don't need this call

    def clear_vote_list(e):
        vote_list.clean()
        page.show_snack_bar(ft.SnackBar(ft.Text(f"Vote list cleared !"), open=True, bgcolor='lightgreen'))
        logger.info('Vote list cleared')

    page.add(
        ft.Row([
            session_cookie_input,
            ft.ElevatedButton("Refresh", on_click=refresh_cookie),
        ])
    )
    
    page.add(
        ft.Row([
            story_nr_input,
            ft.ElevatedButton("START", on_click=start_milk_jira, color='green'),
            ft.ElevatedButton("STOP", on_click=stop_milk_jira, color='red'),
            ft.ElevatedButton("CLEAR", on_click=clear_vote_list),
            # ft.ElevatedButton("print position", on_click=lambda x: print(page.window_left,  page.window_top)),
        ])
    )
    
    page.add(
        ft.Row([
            vote_input,
            ft.ElevatedButton("VOTE", on_click=give_vote, color='green'),
        ])
    )
    
    vote_container = ft.Container(
        content=vote_list, 
        height=330, 
        bgcolor=ft.colors.LIGHT_BLUE_100,
        border=ft.border.all(2, ft.colors.LIGHT_BLUE_500),
        border_radius=10)
    page.add(vote_container)
    
ft.app(target=main)