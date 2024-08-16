import csv
import datetime
from math import exp,pi,sqrt,log
from scipy.stats import norm
from matplotlib import pyplot

root2pi=1/sqrt(2*pi)
r=0.03
v=0.18
def bs_ce(s,k,t):
    d1=(log(s/k)+t*(v*v/2+r))/(v*sqrt(t))
    d2=d1-v*sqrt(t)
    n1=norm.cdf(d1)
    n2=norm.cdf(d2)

    c=n1*s-n2*k*exp(-r*t)
    return c
def normal(x):
    return exp(-0.5*x*x)*root2pi
def date_diff(date1,date2):
    dictionary={"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
    d1=datetime.date(int(date1[7:]),dictionary.get(date1[3:6]),int(date1[:2]))
    d2=datetime.date(int(date2[7:]),dictionary.get(date2[3:6]),int(date2[:2]))
    return abs(d2-d1).days
def read(file):
    data=[]
    handle=open(file,'r')
    rows=csv.reader(handle)
    for row in rows:
        if row[0]=='Symbol':
            headers=row
            continue
        if row[-1]!='-' and row[11]!='-' and int(row[11])>500:
            processed=[]
            t=date_diff(row[1],row[2])
            if t==0:
                continue
            k=float(row[4])
            s=float(row[-1])
            c=bs_ce(s,k,t/365)
            processed.append(t)
            processed.append(k)
            processed.append(s)
            processed.append([float(row[i]) for i in range(5,11)])
            processed.append(c)
# time , strike , underlying , prices , bs_calculated
            data.append(processed)
    handle.close()
    
    return data,headers
def analysis(data):
    stddev=0
    stddev_above=0
    stddev_below=0
    counter_above=0
    counter_below=0
    max_dev=0
    for row in data:
        
        if row[-1]>=row[3][2] and row[-1]<=row[3][1]:
            t=0
        else:
            t=(min(abs(row[-1]/row[3][1]-1),abs(row[-1]/row[3][2]-1)))**2
        if row[2]>row[1]:
            counter_above+=1
            stddev_above+=t
        else:
            counter_below+=1
            stddev_below+=t
        stddev+=t
        if t>max_dev:
            max_dev=t
        pyplot.scatter(row[0],t,color='green')
    stddev/=len(data)
    stddev=sqrt(stddev)
    try:
        stddev_above/=counter_above
        stddev_above=sqrt(stddev_above)
    except:
        stddev_above=None
    try:
        stddev_below/=counter_below
        stddev_below=sqrt(stddev_below)
    except:
        stddev_below=None
    pyplot.show()
    return stddev,stddev_above,stddev_below,max_dev

file_list=['NIFTY 15500 JAN-MAR.csv','NIFTY 15000 JAN-MAR.csv','NIFTY 14500 JAN-MAR.csv','NIFTY 14000 JAN-MAR.csv']
for i in file_list:
    data,headers=read(i)
    sd=analysis(data)
    print(i)
    print('All , OTM , ITM',sd[0],sd[1],sd[2])
    print('Max Deviation by factor of ',sd[3])
