import csv

def fine_cal(mon):
    main_list = {}
    final = {}
    main = []
    val = 0
    with open('Book1.csv', mode='r') as file:
        csvFile = csv.reader(file)
        next(csvFile)
        for lines in csvFile:
            main_list[lines[0]] = lines[1]
    val = 0
    for j, i in main_list.items():

        hour = int(i.split(':')[0]) - 9
        if hour < 1:
            hour = 0
        val += int(i.split(':')[1]) + (hour*60)
        if val != 0:
            final[j] = i

    fair = mon/val
    for key, value in final.items():
        hour = int(value.split(':')[0]) - 9
        imp = int(value.split(':')[1]) + (hour*60)
        main.append({key: [imp, fair*imp]})
    return main


print(fine_cal(300))