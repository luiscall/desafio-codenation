import json
import requests 
url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=TOKEN'
answer = {'answer': open('answer.json', 'rb')}
r = requests.post(url, files=answer) }
print(r.content)
