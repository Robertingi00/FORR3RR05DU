import csv

import csv

input = []

with open('memoizationInput.csv', mode='r') as csv_file:
    spamreader = csv.reader(csv_file, delimiter=' ', quotechar='|')
    for row in spamreader:
        input.append([int(i) for i in row])


for i in range(len(input)-2, -1, -1):
    for ii in range(len(input[i])):
        if(input[i+1][ii] > input[i+1][ii+1]):
            input[i][ii] += input[i+1][ii]
        else:
            input[i][ii] += input[i+1][ii+1]


print(input[0][0])