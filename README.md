
<h1 align="center">
![Voting](voting.jpg)
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

## Run
- make sur .env file has proper JSESSIONID filled
- ```venv\Scripts\activate.bat```
- ```scripts\start.bat```

## 🚀 Instalation
```sh
pip install -r requirements.txt
```

## 💻 Development
- create new virtual environment
- fill .env.local based on .env.example
- flet run src/gui.py -d

## Stuff
- user storage: C:\Users\<USER>\AppData\Roaming\Appveyor Systems Inc\Flet\

## TODO:
- [] de pus un item care sa seteze nr de developeri similar cu inputul pentru session cookie
- [] de pus un sunet cand voteaza un x nr de developeri
- [] de gasit o modalitate sa afisez ce story-uri sunt disponibile pentru vot
- [] sa fac colorat inputul cu story number dupa ce am votat
- [] de adaugat in modal care sa imi arate ce toate configuratiile (nr of developers, wait sleep etc.) # nu cred ca e chiar util, ma mai gandesc
- [x] adaugat un confirmation modal cand apas pe reset vote list
- [x] de gasit care este dimensiunea desktopului si sa pun pagina in coltul din dreapta sus pe baza dimensiunii
- [x] implementat pylint si ceva teste
- [x] sa afisez ultimele story-uri votate, de verificat daca exista un storage in flet sau sa folosesc un sqlite
- [x] sa oprest requestul la API dupa un numar de X(50) incercari
- [x] sa autopopulez inputul cu votul be baza celor mai multe voturi
- [x] de implementat un logger cu log pe fisier
- [x] de reformatat raspunsul si afisat mai bine in chenar
- [x] check if story is  set when pressing start
- [x] button for clear votes
- [x] alerta inainte de START sa verific daca este completat cookie si story number
- [x] sa fac colorat valoarea cu cele mai multe voturi
- [x] add  session cookie from the GUI
- [x] add issue parameter in the main.py call

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
