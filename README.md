
<h1 align="center">
<br>
  "eu cu cine votez ?"
</h1>

<p align="center">GUI to vote on JIRA scrum poker</p>

<hr />
<br />


## 📚 Project Definition

JIRA scrum poker interface is laggy, so i needed a clean and fast interface to vote.


## 🛠️ Features

Technologies used:

- **Flet** # https://flet.dev/
- **Python**


## 🚀 Instalation
```sh
pip install -r requirements.txt
```

## 💻 Development
- create new virtual environment
- fill .env.local based on .env.example
- flet run src/gui.py -d

## TODO:
- [] sa fac colorat valoarea cu cele mai multe voturi
- [] sa fac colorat inputul cu story number dupa ce am votat
- [] de implementat un logger cu log pe fisier
- [] de reformatat raspunsul si afisat mai bine in chenar
- [x] check if story is  set when pressing start
- [x] button for clear votes
- [x] alerta inainte de START sa verific daca este completat cookie si story number
- [] add  session cookie from the GUI
- [] add issue parameter in the main.py call

```
[
    {
        "value": "1",
        "count": 1,
        "assignable": true
    },
    {
        "value": "2",
        "count": 1,
        "assignable": true
    },
    {
        "value": "3",
        "count": 3,
        "assignable": true
    }
]

votes_obj_arr = [
    { "value": "2", "count": 1, "assignable": 'true' },
    { "value": "1", "count": 1, "assignable": 'true' },
    { "value": "12", "count": 11, "assignable": 'true' },
    { "value": "9", "count": 11, "assignable": 'true' },
    { "value": "2", "count": 11, "assignable": 'true' },
    { "value": "5", "count": 7, "assignable": 'true' },
    { "value": "3", "count": 10, "assignable": 'true' },
    { "value": "7", "count": 11, "assignable": 'true' },
]
```