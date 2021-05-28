import json

with open('task_7.txt', 'r') as file:
    statistic = []
    profit = {}
    average_profit = {}
    middle = []
    for line in file:
        name, form, earning, damage = line.split()
        res = int(earning) - int(damage)
        profit[name] = res
        if res >= 0:
            middle.append(res)
    average_profit['average_profit'] = sum(middle) / len(middle)
    statistic.append(profit)
    statistic.append(average_profit)
    print(statistic)

with open('task_7.json', 'a+') as json_file:
    json.dump(statistic, json_file)
