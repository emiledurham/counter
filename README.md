# Customer Service Ticket Counter

A counter built using Django, Bootstrap and Plotly that allows customer service agents to keep track of their tickets.
- The front page displays three counters and starts each new day off at zero.
- You can add and subtract tickets by clicking 🔼 or 🔽
- The tally of each tickets' value for the day is summed in the brackets at the bottom of the table.
- The total sum of all tallies for the day is in the top right corner

![alt text](https://github.com/emiledurham/djword/blob/main/Screen%20Shot%202021-04-07%20at%2015.05.54.png)

- The total number of tickets is stored in a database and rendered as a graph to the dashboard tab.
It will update as you click the 🔼 or 🔽 buttons on the home page.

![alt text](https://github.com/emiledurham/djword/blob/main/Screen%20Shot%202021-04-07%20at%2015.05.25.png)

Create virtual environment:
- `python3 -m venv venv`

Install requirements into venv:
- `pip3 install -r requirements.txt`

Run Django:
- `cd djword`
- `python3 manage.py runserver`