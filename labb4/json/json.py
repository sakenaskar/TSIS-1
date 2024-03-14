print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")

import json


with open('C:/Users/Мирас/Desktop/KBTU/1 курс, 2 семестр/pp2/tsis4/json/sample-data.json', 'r') as file:
    data = json.load(file)

for obj in data['imdata']:
    print(obj['l1PhysIf']['attributes']['dn'], "                              inherit   9150 ")