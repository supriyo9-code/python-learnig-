import json
data = '{"var1":"supriyo","var2":45}'
print(data)

parsed = json.loads(data)
print((parsed))

data2 = {
     "owner_name": "Supriyo Mondal",
     "Cars": ['Lamborghini', 'bmw' 'audi'],
     "place": ("germany",2045),
     "isbad": False
}

jscomp =json.dumps(data2)
print(jscomp)