# cerință:
# dat fiind fișierul temperatures.csv
# scrieți o funcție
def average_temps(fpath):
    pass
# ce returnează un dicționar cu cheile orele
# și valorile mediile orare respective

with open('data/temperatures.csv') as f:
    for line in f:
        print(line)
        break


def average_temps(fpath):
    dict_temp = {}

    with open(fpath) as fp:
        for line in fp:
            line = line.removesuffix("\n")

            time, temp = line.split(',')
            hour = int(time[:2])
            temp = float(temp)

            if hour not in dict_temp:
                dict_temp[hour] = []

            dict_temp[hour].append(temp)
        
    avg_list = []
    for hour, values in dict_temp.items():
        avg = sum(values) / len(values)
        avg_list.append((hour, avg))

    return avg_list

print(average_temps("temperatures.csv"))



def average_temps(fpath: Path) -> dict:
    res = {}
    hour_avg_temp = {}
    
    with open(fpath) as f:
        for line in f:
            time, temp = line.split(',')
            hour = int(time[:2])
            temp = float(temp)

            if hour not in res:
                res[hour] = []

            res[hour].append(temp)
    
    for hour, temps in res.items():
        avg = sum(temps) / len(temps)
        hour_avg_temp[hour] = avg

    return hour_avg_temp


def average_temps(fpath):
    with open(fpath) as f:
        totals = {} # here we maintain the hourly temp sums
        counts = {} # here we maintain the hourly temp occurences

        for line in f:
            #luam line (hh:mm:ss,temp) si extragem temp pentru h
            #trebuie sa corelam temperatura adunata cu ora, folosing 
            #un dictionar (key:h, value:suma(de temepraturi))
            time, temp = line.split(",")
            hour = int(time[:2])
            temp = float(temp)

            # it this is a new, unhandled hour
            if hour not in totals:
                # we initilize the values we'll use for aggreggation
                totals[hour] = 0
                counts[hour] = 0

            totals[hour] += temp
            counts[hour] += 1


        #luam valoarea din primul dictionar si 
        # impartim la a doua valoare din celalt dictionar

        return {
            hour: totals[hour] / counts[hour]
            for hour in totals
        }


import csv

def average_temps(fpath):
    with open(fpath) as f:
        reader = csv.reader(f)

        totals = {} # here we maintain the hourly temp sums
        counts = {} # here we maintain the hourly temp occurences

        for time, temp in reader:
            hour = int(time[:2])
            temp = float(temp)

            # it this is a new, unhandled hour
            if hour not in totals:
                # we initilize the values we'll use for aggreggation
                totals[hour] = 0
                counts[hour] = 0

            totals[hour] += temp
            counts[hour] += 1


        #luam valoarea din primul dictionar si 
        # impartim la a doua valoare din celalt dictionar

        return {
            hour: totals[hour] / counts[hour]
            for hour in totals
        }
