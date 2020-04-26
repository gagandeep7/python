import csv
html=''
names=[]
with open('city8.txt','r+') as country:
     csv_reader=csv.DictReader(country)#dict reader to use keynames in place of index
     for line in csv_reader:
        names.append(f"{line['City']}")# append only city key in every line
print(names)
html +=f'<p>this is list of name of cities</p>'#+=to extend html
html +=f'\n<ul>'
for name in names:
    html+=f'\t\n<li>{name}</li>'
html +=f'\n</ul>'
print(html)