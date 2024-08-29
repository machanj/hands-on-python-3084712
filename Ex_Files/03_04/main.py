import csv
import json
from pprint import pprint

## EINSTEIN = {
##     "birthplace": "Germany",
##     "name": "Albert",
##     "surname": "Einstein",
##     "born": "1879-03-14",
##     "category": "physics",
##    "motivation": "for his services to Theoretical Physics...",
## }

#einstein_json = json.dumps(EINSTEIN)
#back_to_dict = json.loads(einstein_json)
#print(einstein_json)
#pprint(back_to_dict)

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


# 1. you can access parts of strings the same way you do lists
#      hey[2] == "y"
# 2. You can add to a list using
#      my_list.append("something")

laureates_filtered = []
# LinkedIn learner code here

for lareate in laureates:
    if lareate['surname'][0] == "M":
        laureates_filtered.append(laureate)

with open("laureates.json", "w") as f:
    json.dump(laureates_filtered, f, indent=2)

## modified_back_to_dict = json.loads(laureates_json)
## pprint(modified_back_to_dict)