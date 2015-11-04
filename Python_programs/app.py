import jinja2

from flask import Flask
from flask import request
from flask import render_template

from numpy import exp
import json
import requests
import datetime

template0 = jinja2.Template("""
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Welcome</title>
</head>
<body style="background-color: #3366FF;">
    <h1 style="color: #FFFFFF;"><em>Welcome to Docks vs. Bicycles</em></h1>
    <h2 style="text-decoration: underline; color: #FFFFFF;">Description:</h2>
    <h3 style="color: #FFFFFF;">Here you can see the results of a predictive model that can help operations in <a style="color: #FFFFFF;" target="_blank" href="http://www.citibikenyc.com/">Citibike</a>, the bicycle sharing service in New York City, by predicting which docking stations are going to be empty or full and when.</h3>
    <img src="https://nameless-plateau-2699.herokuapp.com/static/Citibike.png" alt="Picture of a bicycle" style="width: 415px; height: 313px; float: left; margin-right: 50px;" />
    <h2 style="text-decoration: underline; color: #FFFFFF;">Optional User Actions:</h2>
    <h3 style="color: #FFFFFF;">Click &nbsp;<a style="color: #FFFFFF;" href="https://youtu.be/FecjHWi2K3I" target="_blank" title="Video summary">here</a> &nbsp;for the video summary.</h3>
    <h3 style="color: #FFFFFF;">Click &nbsp;<a style="color: #FFFFFF;" href="https://github.com/yshaham/docksvsbicycles" target="_blank" title="Analysis and Programs">here</a> &nbsp;for analysis and Python programs.</h3>
      <form action="." method="POST">
        <h3 style="color: #FFFFFF;">Click button for predictions: <input type="submit" name="myform1" value="Predictions"></h3>
      </form>
 </body>
</html>
""")

template = jinja2.Template("""
<!DOCTYPE html>
<html lang="en-US">
<head>
  <title>Model predictions</title>
</head>
<body>
 
    <p> Last update on {{updatetimejs}} </p>
    <h2>Legend:</h2>
    <p style="position:absolute;top:80px;left:70px;">Station will be empty/full within 1 hour </p>
    <p style="position:absolute;top:110px;left:70px;">Station will be empty/full within 2 hours</p>
    <p style="position:absolute;top:140px;left:70px;">Station will be empty/full within 3 hours</p>
    <p style="position:absolute;top:170px;left:70px;">Station will not become empty/full in the next 3 hours</p>
    <p style="position:absolute;top:200px;left:70px;">New stations - predictions will be available after more data is collected</p>
    <a style="position:absolute;top:103px;left:50px;background-color:#FF0000;height:7px;width:7px;"></a>
    <a style="position:absolute;top:133px;left:50px;background-color:#FF00FF;height:7px;width:7px;"></a>
    <a style="position:absolute;top:163px;left:50px;background-color:#0000FF;height:7px;width:7px;"></a>
    <a style="position:absolute;top:193px;left:50px;background-color:#00CC00;height:7px;width:7px;"></a>
    <a style="position:absolute;top:223px;left:50px;background-color:#666666;height:7px;width:7px;"></a>

    <img style="position:absolute;top:260px;left:40px;" src="https://nameless-plateau-2699.herokuapp.com/static/base_map.png" />

    <a> {{str_from_py2}} </a>

    <p><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/></p>     
    <p><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/></p>
    <p><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/></p>
    <p><br/><br/><br/><br/><br/><br/><br/><br/><br/></p>

    <div> {{str_from_py1}} </div>
    <form action="." method="POST">
        Click on button to return to welcome page: <input type="submit" name="myform1" value="Return">
    </form>
</body>

</html>
""")

app = Flask(__name__)

@app.route('/')
def my_form():
  return template0.render()

@app.route('/', methods=['POST'])
def my_form_post():

  button1 = request.form['myform1']
  if button1 == 'Predictions' :
    nrow = 651
    ncol = 719
#
# getting data
#
# Heroku
    page_url = 'http://www.citibikenyc.com/stations/json'
    response = requests.get(page_url)
    jsonDict = json.loads(response.text)
# Local
#    f2read = open('stations0.json')
#    jsonDict = json.loads(f2read.read())
#    f2read.close()
    f2read = open('static/p6wde_json.txt')
    jsonDwde = json.loads(f2read.read())
    f2read.close()
    f2read = open('static/p6wds_json.txt')
    jsonDwds = json.loads(f2read.read())
    f2read.close()
    f2read = open('static/p6wee_json.txt')
    jsonDwee = json.loads(f2read.read())
    f2read.close()
    f2read = open('static/p6wes_json.txt')
    jsonDwes = json.loads(f2read.read())
    f2read.close()
# Heroku
    page_url = 'http://api.openweathermap.org/data/2.5/forecast?id=5128581&appid=f1d4891438b01cf1b1da1d045fecc1e1'
    response = requests.get(page_url)
    jsonD4cast = json.loads(response.text)
    page_url = 'http://api.openweathermap.org/data/2.5/weather?id=5128581&appid=f1d4891438b01cf1b1da1d045fecc1e1'
    response = requests.get(page_url)
    jsonD4now = json.loads(response.text)
# Local
#    f2read = open('openWeather/openWeather0.txt')
#    jsonD4cast = json.loads(f2read.read())
#    f2read.close()
#    f2read = open('openWeather/openWeather1.txt')
#    jsonD4now = json.loads(f2read.read())
#    f2read.close()
#
# data reading completed
#
    lastUpdate = jsonDict[u'executionTime']
    alist = jsonDict[u'stationBeanList']
    blist = []
    clist = []
    hlist = []
    vlist = []
    colist = []
    if datetime.date(int(lastUpdate[0:4]),int(lastUpdate[5:7]),int(lastUpdate[8:10])).weekday()<5 :
      De = jsonDwde
      Ds = jsonDwds
    else :
      De = jsonDwee
      Ds = jsonDwes
    hour = int(lastUpdate[11:13])
    ampm = lastUpdate[20:22]
    if ampm=='PM' :
      hour = hour + 12
    elif hour==12 :
      hour = 0
    qtr = 4.0*hour+float(int(lastUpdate[14:16])/15)
    print type(qtr)
    tyr = (datetime.date(int(lastUpdate[0:4]),int(lastUpdate[5:7]),int(lastUpdate[8:10]))-datetime.date(2014,4,1)).days+qtr/96.0
    tyr = tyr-365*int(tyr/365)
    t0 = jsonD4now['dt']
    t1 = jsonD4cast['list'][0]['dt']
    t2 = jsonD4cast['list'][1]['dt']
    T0 = jsonD4now['main']['temp']-273.15
    T1 = jsonD4cast['list'][0]['main']['temp']-273.15
    T2 = jsonD4cast['list'][1]['main']['temp']-273.15
    R0 = 0
    if 'rain' in jsonD4now :
      R0 = jsonD4now['rain']['3h']
    R1 = 0
    if 'rain' in jsonD4cast['list'][0] :
      R1 = jsonD4cast['list'][0]['rain']['3h']
    R2 = 0
    if 'rain' in jsonD4cast['list'][1] :
      R2 = jsonD4cast['list'][1]['rain']['3h']
    S0 = 0
    if 'snow' in jsonD4now :
      S0 = jsonD4now['snow']['3h']
    S1 = 0
    if 'snow' in jsonD4cast['list'][0] :
      S1 = jsonD4cast['list'][0]['snow']['3h']
    S2 = 0
    if 'snow' in jsonD4cast['list'][1] :
      S2 = jsonD4cast['list'][1]['snow']['3h']
#
# interpolations to get parameters
# using the simplest methods to avoid heroku's moods about modules
# the calculation time is still very short
#
    tlist=[0.0,float(t1-t0),float(t2-t0)]
    ttarg=[1800.0,5400.0,9000.0]
    w=[[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]
    for j in range(3) :
      for k in range(2) :
        if ttarg[j] <= tlist[k+1] and ttarg[j] > tlist[k] :
          w[j][k]   = (tlist[k+1]-ttarg[j])/(tlist[k+1]-tlist[k])
          w[j][k+1] = (ttarg[j]  -tlist[k])/(tlist[k+1]-tlist[k])
    Rlist = [R0*0.25,R1*0.25,R2*0.25]
#
# weather data is amount in 3 hours and model uses 3/4 of an hour 
#
    Slist = [S0*0.25,S1*0.25,S2*0.25]
    Tlist = [T0     ,T1     ,T2     ]
    Rtarg = [0.0,0.0,0.0]
    Starg = [0.0,0.0,0.0]
    Ttarg = [0.0,0.0,0.0]
    qtrtarg = [qtr+2.0,qtr+6.0,qtr+10.0]
    for j in range(3) :
      for k in range(3) :
        Rtarg[j] = Rtarg[j]+w[j][k]*Rlist[k]
        Starg[j] = Starg[j]+w[j][k]*Slist[k]
        Ttarg[j] = Ttarg[j]+w[j][k]*Tlist[k]
      if qtrtarg[j]==95.0 :
        qtrtarg[j]=94.99
      elif qtrtarg[j] > 95.0 :
        qtrtarg[j] = qtrtarg[j] - 96.0
        if qtrtarg[j] < 0.0 :
          qtrtarg[j] = 0.0
      if Rtarg[j] >= 0.34 :
        Rtarg[j] = 0.3399
      if Starg[j] >= 2.8 :
        Starg = 2.799
      if Ttarg[j] >= 35.0 :
        Ttarg[j] = 34.99
      elif Ttarg[j] < -15.0 :
        Ttarg[j] = -15.0
      if tyr > 365.0 :
        tyr = 364.99
#
# calculating colors (according to the above Legend) and locations of stations for map
#
    for i in range(len(alist)) :
      stalon = alist[i][u'longitude']
      stalat = alist[i][u'latitude']
      hindxi = int(round(((-stalon-73.9494305)*46.0+(stalon+74.0936716)*609.0)/(74.0936716-73.9494305)))-3+40
      vindxi = int(round(((40.7968131-stalat)*523.0+(stalat-40.7001806)*27.0)/(40.7968131-40.7001806)))-3+260
      vlist.append(vindxi)
      hlist.append(hindxi)
      station = str(alist[i][u'id'])
      if not station in jsonDwes.keys() :
        colstr = '#666666'
      else :
        colstr = '#00CC00'
        linkliste = [0.0,0.0,0.0]
        linklists = [0.0,0.0,0.0]
        diffbike = [0.0,0.0,0.0]
        pelist = De[station]
        pslist = Ds[station]
        docks = alist[i]['totalDocks']
        bikes = alist[i]['availableBikes']
        for j in range(3) :
          k = int((Ttarg[j]+15.0)/5.0)
          linkliste[j] = linkliste[j] + ((-15.0+5.0*(k+1)-Ttarg[j])*pelist[k]+(Ttarg[j]+15.0-5.0*k)*pelist[k+1])/5.0
          linklists[j] = linklists[j] + ((-15.0+5.0*(k+1)-Ttarg[j])*pslist[k]+(Ttarg[j]+15.0-5.0*k)*pslist[k+1])/5.0
          k = int(qtrtarg[j]/5.0)
          linklists[j] = linklists[j] + ((5.0*(k+1)-qtrtarg[j])*pslist[k+11]+(qtrtarg[j]-5.0*k)*pslist[k+12])/5.0
          linklists[j] = linklists[j] + ((5.0*(k+1)-qtrtarg[j])*pslist[k+11]+(qtrtarg[j]-5.0*k)*pslist[k+12])/5.0
          k = int(tyr/36.5)
          linkliste[j] = linkliste[j] + ((36.5*(k+1)-tyr)*pelist[k+31]+(tyr-36.5*k)*pelist[k+32])/36.5
          linklists[j] = linklists[j] + ((36.5*(k+1)-tyr)*pslist[k+31]+(tyr-36.5*k)*pslist[k+32])/36.5
          k = int(Rtarg[j]/0.034)
          linkliste[j] = linkliste[j] + ((0.034*(k+1)-Rtarg[j])*pelist[k+42]+(Rtarg[j]-0.034*k)*pelist[k+43])/0.034
          linklists[j] = linklists[j] + ((0.034*(k+1)-Rtarg[j])*pslist[k+42]+(Rtarg[j]-0.034*k)*pslist[k+43])/0.034
          k = int(Starg[j]/0.28)
          linkliste[j] = linkliste[j] + ((0.28*(k+1)-Starg[j])*pelist[k+53]+(Starg[j]-0.28*k)*pelist[k+54])/0.28
          linklists[j] = linklists[j] + ((0.28*(k+1)-Starg[j])*pslist[k+53]+(Starg[j]-0.28*k)*pslist[k+54])/0.28
          linkliste[j] = linkliste[j] - 4.0 * pelist[3]
          linklists[j] = linklists[j] - 4.0 * pslist[3]
#
# model gives predictions per 15 minutes
#
          diffbike[j] = 4.0*(exp(linkliste[j])-exp(linklists[j]))
          docks = docks - diffbike[j]
          bikes = bikes + diffbike[j]
          if docks < 0 :
            if j==0 :
              colstr = '#FF0000'
              blist.append(('1 Hour',alist[i][u'stationName'],'Docks'))
            elif j==1 :
              colstr = '#FF00FF'
              blist.append(('2 Hour',alist[i][u'stationName'],'Docks'))
            else :
              colstr = '#0000FF'
              blist.append(('3 Hour',alist[i][u'stationName'],'Docks'))
            break
          if bikes < 0 :
            if j==0 :
              colstr = '#FF0000'
              blist.append(('1 Hour',alist[i][u'stationName'],'Bicycles'))
            elif j==1 :
              colstr = '#FF00FF'
              blist.append(('2 Hour',alist[i][u'stationName'],'Bicycles'))
            else :
              colstr = '#0000FF'
              blist.append(('3 Hour',alist[i][u'stationName'],'Bicycles'))
            break
      colist.append(colstr)
      if len(blist)>0 :
        print i,len(blist),len(colist),len(vlist),len(hlist),blist[len(blist)-1],colist[i]
#
# preparing table and plotting of stations for HTML
#
    str4js1 = '<table> <tr><th>Station Name</th><th>Response Time</th><th>To Fix Shortage of</tr>'
    blist = sorted(blist)
    for i in range(len(blist)) :
      str4js1 = str4js1 + '<tr><td>' + blist[i][1] + '</td><td>' + blist[i][0] + '</td><td>' + blist[i][2] + '</td></tr>'
    str4js1 = str4js1 + '</table>'
    stationsch = ''
    for i in range(len(colist)) :
      stationsch = stationsch+'<a style="position:absolute;top:'+str(vlist[i])+'px;left:'+str(hlist[i])+'px;background-color:'+str(colist[i])+';height:7px;width:7px"></a>'
    stationsch = stationsch
    return template.render(updatetimejs=lastUpdate,str_from_py1 = str4js1,str_from_py2=stationsch)
  else :
    return template0.render()

if __name__ == '__main__':
    app.run(host='0.0.0.0')

