import json
  
# Opening JSON file
f = open('data.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
while 1 == 1:
    for i in data['emp_details']:
        print(i)
  
# Closing file
f.close()