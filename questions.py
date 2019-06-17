from helpers import helpers
import random
import urllib, json
import urllib.request

class questions:
    def __init__(self, category, difficulty):
        helpers.clearScreen()
        if difficulty == '1':
            newDiff = "easy"
        elif difficulty == '2':
            newDiff = "medium"
        elif difficulty == '3':
            newDiff = "hard"

        if category == '1':
            interval = random.randint(1,2)
            if interval == 1:
                randomCatNum = random.randint(50,57)
            else:
                while 1:
                    randomCatNum = random.randint(97,102)
                    if randomCatNum != 101:
                        break
            category = chr(randomCatNum)

        
        if category == '2':
            newCat = '9'
        if category == '3':
            newCat = '10'
        if category == '4':
            newCat = '11'
        if category == '5':
            newCat = '13'
        if category == '6':
            newCat = '14'
        if category == '7':
            newCat = '19'
        if category == '8':
            newCat = '22'
        if category == '9':
            newCat = '21'
        if category == 'a':
            newCat = '23'
        if category == 'b':
            newCat = '24'
        if category == 'c':
            newCat = '25'
        if category == 'd':
            newCat = '26'
        if category == 'f':
            newCat = '31'
        
        api = "https://opentdb.com/api.php?amount=10&category=" + newCat + "&difficulty=" + newDiff + "&type=multiple"
        with urllib.request.urlopen(api) as url:
            data = json.loads(url.read().decode())
        #print(data)
        for question in data['results']:
            print(question['question'])



