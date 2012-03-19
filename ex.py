import os

timezone = 'Asia/Chongqing'
os.environ['TZ'] = timezone

import datetime

time = datetime.datetime.now()
print "current time is %s" %time
