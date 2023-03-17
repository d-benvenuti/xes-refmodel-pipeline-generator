import json
#open the file
f = open("new.json")
#decode the json
o = json.load(f)
#close the file
f.close()
#save the traces in a list
list = []
for i in o.items():
    list.append(i)
  