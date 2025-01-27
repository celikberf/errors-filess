#cihazlar arasında ortak veri taşıma 

import json

person_string = '{"name" : "Berf" , "languages" : ["python", "C#"]}'
person_dict = {'name' : 'Berf','languages' :['Python','C#']}

# JSON string to Dict

#result = json.loads(person_string) # dict' e cevirdik
#result = result['name']
#result = result['languages']

# with open("person.json") as f:
#     data = json.load(f) #  yüklemee işlemi
#     print(data['name'])

person_dict= {
    'name' : 'Berf',
    'languages' :['Python','C#']
}

# Dict to JSONstring
"""
result= json.dumps(person_dict) # person_dict'i çevirdik.
print(result)
print(type(result))
"""
"""
with open('person.json','w') as f: #bilgiyi prson.json dosyasına  gönderdik
    json.dump(person_dict,f)
"""

person_dict = json.loads(person_string)

result = json.dumps(person_dict, indent=4 , sort_keys=True) # okunabilirliği artan şeklinde yazdık

print(result)
print(person_dict)