import csv
import pandas as pd
data=pd.read_csv('city8.txt')
with open('new7.csv','r+') as file:
    csv_reader=F=csv.DictReader(file)
    with open('new8.csv','w') as wf:
        field=['SNo','City','State','lat','long']
        csv_Write=csv.DictWriter(wf,fieldnames= field,delimiter=',')
        csv_Write.writeheader()


        for line in csv_reader:
            csv_Write.writerow(line)
print(data)


