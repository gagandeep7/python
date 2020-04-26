import os
os.chdir((''))
print(os.getcwd())
i=0

for f in os.listdir():
    fname,ext=os.path.splitext(f)
    name,num=fname.split('')
    num=num.strip().zfill
    name=name.strip()
    newn=f"{num} {name}"
    os.rename(f,newn)
