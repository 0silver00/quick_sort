import csv
import random

i=0; num=[]

for i in range(1000000):
    num.append(random.randrange(1000000))

f = open('output.csv', 'w', encoding='utf-8')

writer = csv.writer(f)
    
writer.writerow(num)

f.close()
