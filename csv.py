import webbrowser
import datetime
#import win32com.client as win32comclient
#--------------------------------------gets current date-------------------------------#
from dateutil.relativedelta import relativedelta
currentdate = datetime.datetime.now()
date_formated = currentdate.strftime("%m%d%Y")
#--------------------------------------gets current date-------------------------------#


#--------------------------------------calls api---------------------------------------#
meters = ['300001306', '350000381']

for i in meters:
    #webbrowser.open('http://io.ekmpush.com/readMeter?meters=' + i + '&ver=v4&key=NjUyMjA2ODE6R2JXZEluYWw&fmt=csv&cnt=10&timezone=America~Denver&since=1572552180250')
    webbrowser.open('https://summary.ekmmetering.com/summary?key=NjUyMjA2ODE6R2JXZEluYWw&meters=300001306&format=html&report=mo&limit=10&offset=0&timezone=America~Denver&start_date=201909011432&end_date=201910311432')  
#--------------------------------------calls api---------------------------------------#

