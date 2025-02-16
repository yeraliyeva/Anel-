import datetime
#1  subtract five days from current date
now = datetime.datetime.today()
ago = now-datetime.timedelta(days = 5)
print(ago.strftime("%Y-%m-%d"))

#2 print yesterday, today, tomorrow
yes= date.today()-timedelta(1)
tod=date.today()
tom=date.today()+timedelta(1)
print(yes, " ", tod, " ", tom)
#3
from datetime import datetime
dt=datetime.now()
dt_drop=dt.replace(microsecond=0)
print(dt_drop)
#4
rt=date.today()
rt2=date.today()-timedelta(6)
res=rt-rt2
sec=res.total_seconds()
print(sec)



