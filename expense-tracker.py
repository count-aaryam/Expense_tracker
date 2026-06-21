from tabulate import tabulate 
import json

with open("expenses.json","r") as file:
    data=json.load(file)

print(tabulate(data,tablefmt="grid",headers="keys"))

for row in data:
    amount=int(row["Amount"][:len(row["Amount"])-1])
    print(amount)