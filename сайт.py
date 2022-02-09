import requests
from pprint import pprint
response = requests.get(url='https://api.stackexchange.com/2.3/questions?fromdate=1644192000&todate=1644364800&order=desc&sort=activity&tagged=Python&site=stackoverflow')
questions = response.json()['items']
for question in questions:
    print(question['title'])