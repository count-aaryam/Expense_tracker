import json 
from tabulate import tabulate

def re_index(data):
    for i in range(0,len(data)):
        data[i]["ID"]=i+1

def print_list():
    with open("expenses.json","r") as file:
        data=json.load(file)
    print(tabulate(data,tablefmt="grid",headers="keys"))
    return 


def add_expense(desc,amt):
    with open("expenses.json","r") as file:
        data=json.load(file)
    amount=amt+"$"
    obj={
    "ID":0,
    "Date":"2024-08-21",
    "Description":desc,
    "Amount":amount
    }
    data.append(obj)
    re_index(data)
    with open("expenses.json","w") as file:
        json.dump(data,file)
    print_list()
    return
    
def report_summary():
    with open("expenses.json","r") as file:
        data=json.load(file)
    expenses=0
    for row in data :
        amount=int(row["Amount"][:len(row["Amount"])-1])
        expenses+=amount
    print(f"Total expenses: ${expenses}")

def delete_spend_rec(id):
    with open("expenses.json","r") as file:
        data=json.load(file)
    for i,row in enumerate(data):
        if row["ID"]==id:
            data.pop(i)
    re_index(data)
    with open("expenses.json","w") as file:
        json.dump(data,file)
    print_list()
    return 

