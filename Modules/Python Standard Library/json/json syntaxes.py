import json

# true JSON data (don't use '' only "")
people_string = """
{
    "people": 
    [
        {
            "name": "John Smith",
            "phone": "9323-495-xx2",
            "emails": ["kbsawant@gmail.com", "kenrosenberg@gmail.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "564-789-1234",
            "emails": null,
            "has_license": true
        }
    ]
}
"""

# loading JSON string into a python dictionary
data = json.loads(people_string)
print(type(data))

for i in data['people']:
    del i['phone']

# loading a Python dict into a string
new_string = json.dumps(data, indent=2)

#_______Working with JSON files_________#

with open("states.json") as jay:
    data = json.load(jay)               # .load is used with file objects

    for state in data['states']:
        del state['area_codes']

with open('new_states.json', mode='w') as jay2:
    json.dump(data, jay2, indent=2)     # .dump is used to write to a JSON file