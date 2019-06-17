import urllib, json
import urllib.request


api = "https://opentdb.com/api.php?amount=10&category=" + "10" + "&difficulty=" + "hard" + "&type=multiple"
with urllib.request.urlopen(api) as url:
    data = json.loads(url.read().decode())
#print(data)
for question in data['results']:
    print(question['question'])