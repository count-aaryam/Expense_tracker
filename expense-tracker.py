import sys
import utils

commands={
    "add":4,
    "list":2,
    "delete":3,
    "summary":2
}

list_operations=("add","list","summary","delete")

args=sys.argv

if len(args)==1:
    utils.print_task_list()
else:
    cmd=args[1]

    if cmd not in commands:
        print("Unknown Command")
        exit()

    required_len=commands[cmd]

    if len(args)<required_len:
        print("Not enough arguements for the operation")
        exit()

    if cmd=="add":
        desc=args[2]
        cost=args[3]
        utils.add_expense(desc,cost)
    if cmd=="delete":
        id=int(args[2])
        utils.delete_spend_rec(id)
    if cmd=="summary":
        utils.report_summary()
    if cmd=="list":
        utils.print_list()