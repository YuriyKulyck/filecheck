import json

with open('bd.json', 'r', encoding="utf-8") as f:
    data = json.load(f)

numbers = len(data)

with open('task2.json', 'r', encoding="utf-8") as f:
    dota = json.load(f)

a = input("Ім'я:")
b = input("Прізвище:")

summa = 0
for man in data:
    summa += man['оцінка']

for i in dota:
    if a == i["імя"]:
        if b == i["Прізвище"]:
            print(i["оцінки"])




print(summa/numbers)