from win32api import GetSystemMetrics
import flet as ft
import time
import os
import dotenv
from dotenv import load_dotenv
from playsound import playsound

from jira_scripts import fetch_votes, set_vote
from logger_service import logger
from constants import (
    JIRA_SESSION_ID,
    MAX_RETRYS_REQUEST,
    LAST_VOTE_KEY_STORAGE,
    WAIT_SECONDS,
    NR_OF_DEVELOPERS,
    ROOT_DIR,
    NR_OF_DEVELOPERS_OFFSET,
)
from components.VoteList import VoteList

dotenv_file = dotenv.find_dotenv()
load_dotenv(dotenv_file)

milking_jira = False
retrys_jira = 0


def main(page: ft.Page):
    # TODO: see if i create a module for this
    screen_0 = GetSystemMetrics(0)
    # screen_1 = GetSystemMetrics(1)
    page.title = "Eu cu cine votez ?"
    page.window_width = 900
    page.window_height = 800
    page.window_left = screen_0 - page.window_width
    page.window_top = 0

    session_cookie_input = ft.TextField(hint_text="JIRA session cookie", width=400)
    session_cookie_input.value = JIRA_SESSION_ID
    story_nr_input = ft.TextField(hint_text="Story number", width=200)
    vote_input = ft.TextField(hint_text="SP", width=100)
    vote_list = ft.ListView(expand=True, spacing=10, padding=10)
    last_vote = ft.Text(page.client_storage.get(LAST_VOTE_KEY_STORAGE), color="green")

    def refresh_cookie(e):
        logger.info(JIRA_SESSION_ID)
        cookie_input = session_cookie_input.value or ""
        if cookie_input == "":
            page.show_snack_bar(
                ft.SnackBar(
                    ft.Text(f"You need to fille something in the input before refresh!"), open=True, bgcolor='red'
                )
            )
        else:
            os.environ['JSESSIONID'] = cookie_input
            dotenv.set_key(
                dotenv_path=dotenv_file, key_to_set="JSESSIONID", value_to_set=cookie_input, quote_mode="never"
            )
            session_cookie_input.value = cookie_input
            page.update()

    def fill_vote_list():
        global milking_jira
        global retrys_jira
        if milking_jira:
            if story_nr_input.value != '' and session_cookie_input.value != '':
                status, votes = fetch_votes(story_nr_input.value, session_cookie_input.value)
                retrys_jira = retrys_jira + 1
                if retrys_jira == MAX_RETRYS_REQUEST:
                    milking_jira = False
                    page.show_snack_bar(
                        ft.SnackBar(
                            ft.Text(
                                f"Stoping the api calls after {MAX_RETRYS_REQUEST} retrys for {story_nr_input.value}!"
                            ),
                            open=True,
                            bgcolor='red',
                        )
                    )
                    logger.error(f"Stoping the api calls after {MAX_RETRYS_REQUEST} retrys for {story_nr_input.value}!")
                if not status:
                    logger.error(f'Vote fetching failed for {story_nr_input.value} !')
                    page.show_snack_bar(
                        ft.SnackBar(ft.Text("Error when calling fetch votes API !"), open=True, bgcolor='red')
                    )
                vl = VoteList(vote_list=votes, story=story_nr_input.value)
                biggest_vote = vl.get_most_votes()
                current_nr_of_votes = vl.get_nr_of_votes()
                logger.info(f"{current_nr_of_votes=}")
                if current_nr_of_votes >= int(NR_OF_DEVELOPERS) - NR_OF_DEVELOPERS_OFFSET:
                    # try to play the sound only once
                    """ if vote_input.value == '':
                        try:
                            playsound(f'{ROOT_DIR}/assets/slm.mp3')
                        except:
                            pass """
                    vote_input.value = str(biggest_vote['value'])
                    logger.info(
                        f"Filling the vote input with: {biggest_vote['value']} / already voted: {current_nr_of_votes} from nr of developers present: {NR_OF_DEVELOPERS}"
                    )
                vote_list.controls.insert(0, vl.get_colored_output())
                logger.info(f'votes \n {votes}')
                page.update()
                time.sleep(WAIT_SECONDS)
                fill_vote_list()
            else:
                page.show_snack_bar(ft.SnackBar(ft.Text("Fill the story number first !"), open=True, bgcolor='red'))
                logger.error(f'Not all input values where given for fetching votes for {story_nr_input.value}')
                milking_jira = False
                votes = []

    def give_vote(e):
        if story_nr_input.value != '' and vote_input.value != '' and session_cookie_input.value != '':
            res = set_vote(story_nr_input.value, vote_input.value, session_cookie_input.value)
            if res:
                vote_input.value = ''
                vote_input.update()
                page.client_storage.set(LAST_VOTE_KEY_STORAGE, story_nr_input.value)
                last_vote_stored = page.client_storage.get(LAST_VOTE_KEY_STORAGE)
                last_vote.value = last_vote_stored
                last_vote.update()
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
                ft.SnackBar(
                    ft.Text(f"Story number or SP not filled for {story_nr_input.value} !"), open=True, bgcolor='red'
                )
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

    def close_dlg_clear_last_vote(e):
        clear_last_vote_dlg_modal.open = False
        page.update()

    def clear_last_vote(e):
        page.client_storage.remove(LAST_VOTE_KEY_STORAGE)
        last_vote.value = '-'
        last_vote.update()
        clear_last_vote_dlg_modal.open = False
        page.update()

    def open_dlg_clear_last_vote(e):
        page.dialog = clear_last_vote_dlg_modal
        clear_last_vote_dlg_modal.open = True
        page.update()

    clear_last_vote_dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you really want to clear last vote?"),
        actions=[
            ft.TextButton("No", on_click=close_dlg_clear_last_vote),
            ft.TextButton("Yes", on_click=clear_last_vote),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    page.add(ft.Row([session_cookie_input, ft.ElevatedButton("Refresh", on_click=refresh_cookie)]))

    def clear_vote_input(e):
        vote_input.value = ''
        vote_input.update()

    page.add(
        ft.Row(
            [
                story_nr_input,
                ft.ElevatedButton("START", on_click=start_milk_jira, color='green'),
                ft.ElevatedButton("STOP", on_click=stop_milk_jira, color='red'),
                ft.ElevatedButton("CLEAR", on_click=clear_vote_list),
                # ft.ElevatedButton("print position", on_click=lambda x: print(page.window_left,  page.window_top)),
            ]
        )
    )

    page.add(
        ft.Row(
            [
                vote_input,
                ft.ElevatedButton("VOTE", on_click=give_vote, color='green'),
                ft.ElevatedButton("CLEAR vote input", on_click=clear_vote_input),
                ft.ElevatedButton("CLEAR last vote saved", on_click=open_dlg_clear_last_vote, color='red'),
            ]
        )
    )

    page.add(ft.Row([ft.Text("Last vote: "), last_vote]))

    vote_container = ft.Container(
        content=vote_list,
        height=330,
        bgcolor=ft.colors.LIGHT_BLUE_100,
        border=ft.border.all(2, ft.colors.LIGHT_BLUE_500),
        border_radius=10,
    )
    page.add(vote_container)


ft.app(target=main)
