import csv

year, month, community = [], [], []
total_complaints_by_year, total_complaints_by_month, total_complaints_by_community = [], [], []
total_callers_by_year, total_callers_by_month, total_callers_by_community = [], [], []

with open("Aircraft_Noise_Complaint_Data.csv", "r") as file:
    datas = csv.reader(file, delimiter=",")
    next(datas)

    for line in datas:
        if line[0] not in year:
            year.append(line[0])

        if line[1] not in month:
            month.append(line[1])

        if line[2] not in community:
            community.append(line[2])

file.close()

with open("Aircraft_Noise_Complaint_Data.csv", "r") as file:
    datas = csv.reader(file, delimiter=",")
    next(datas)

    for i in range(len(year)):
        print(year[i])
        sum = 0
        for line in datas:
            if line[0] == year[i]:
                print(line[0])
                    #sum += int(line[3])

    #total_complaints_by_year.append(sum)



#year_int = list(map(int, year))
#print(total_complaints_by_year)

