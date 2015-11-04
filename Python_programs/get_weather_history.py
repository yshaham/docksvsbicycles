import requests
import datetime

t0 = datetime.datetime.strptime('2014-03-31','%Y-%m-%d')
for i in range(0,549) :
  dt = datetime.timedelta(days=i)
  t1 = t0 + dt
  yrch = str(t1.year)
  moch = str(t1.month)
  if len(moch) == 1 :
    moch = '0' + moch
  daych = str(t1.day)
  if len(daych) == 1 :
    daych = '0' + daych
  page_url = 'http://www.wunderground.com/history/airport/KNYC/'+yrch+'/'+moch+'/'+daych+'/DailyHistory.html?req_city=New+York&req_state=NY&req_statename=New+York&reqdb.zip=10001&reqdb.magic=5&reqdb.wmo=99999&format=1'
  response = requests.get(page_url)
  print i,yrch,moch,daych,response.encoding, response.url
  ich = str(i)
  if len(ich) == 2 :
    ich = '0' + ich
  elif len(ich) == 1 :
    ich = '00' + ich
  f2write = open('weather_'+ich+'_'+yrch+'_'+moch+'_'+daych+'.txt','w')
  f2write.write(response.text.encode('utf-8'))
  f2write.close
print 'Done'

