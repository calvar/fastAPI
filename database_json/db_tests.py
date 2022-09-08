import json

#Load database
In = open("simple_data.json")
db = json.load(In)
In.close()

new_data = [
    {"C1": 10, "C2": "b", "C3": 2.3},
    {"C1": 8, "C2": "b", "C3": 2.5}
]

for rec in new_data:
    for col in db:
        db[col][str(len(db[col]))] = rec[col]
        #print(db[col][str(len(db[col])-1)])
        #print(rec[col])
        #print()


print(db)
