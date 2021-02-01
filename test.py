import requests

url = "http://localhost:8000/task"

for i in range(10000):
    res = requests.post(url,json={
    "task_name": "test_task"+str(i),
    "priority": 2,
    "description": "test_description"+str(i),
    "due_date": "2021-02-03T21:34:30.783608"
    })


url = "http://localhost:8000/user"

for i in range(100):
    res = requests.post(url,json={
    "user_name": "test_user"+str(i),

    })

