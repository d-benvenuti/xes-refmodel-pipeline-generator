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
    list.append(i[1])
    print(i)
#save the attributes at log level
pipelineID = list[0].get('Pipeline ID')
pipelineName = list[0].get('Pipeline Name') 
pipelineCommunicationMedium = list[0].get('Pipeline Communication Medium')
#for j in list:
    #print(j)
  