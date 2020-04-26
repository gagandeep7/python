import datetime
import pytz
dtnow=dt=datetime.datetime.today()
dt=datetime.datetime(2020,8,3,1,20,55,100000)
dtpy=datetime.datetime.now()#datetime now is used as it can be change time zone
print(dtpy)
dtm=dtpy.astimezone(pytz.timezone('Europe/Madrid'))#change time zone
print(dtm)
dts=dtm.strftime('%B %d,%Y')#convert datetime to string format
print(f"madrid time zone is :{dtm.hour}",f"india time zone is {dtnow.hour}")
print(f"it is in simple format :::{dts}")
bday="March 05,2019"
bday=datetime.datetime.strptime(bday,'%B %d,%Y')#covert string to datetime
print(bday)
till_bday=bday-dtnow
print(f"no of days till birthday:{till_bday.days}","AND",f"no of seconds till birthday:{till_bday.seconds}")
