import serial, sys
import matplotlib.pyplot as plt
from datetime import date
import time
import matplotlib.pyplot as plt

today = date.today()
t=time.localtime()
current_time=time.strftime("_H%H_M%M_S%S",t)
fn="SL_"+str(today)+current_time+".csv"
f=open(fn,'w',encoding="utf-8")
start = time.time()

#x=range(0, 100, 1)
#data=[0]*100
ser = serial.Serial(sys.argv[1],19200)
while True:
  try:
    ttime=time.time()-start
    if ttime<0.001:
      ttime=0.0
    st=time.strftime("%Y %b %d %H:%M:%S", time.localtime())
    ss=str(time.time()-int(time.time()))
    rttime=round(ttime,2)
    line = ser.readline()
    line2=line.strip().decode('utf-8')
    line=[str(val) for val in line2.split(",")]
#    print(line2)
#    print(line)
    str1=st+ss[1:5]+","+str(rttime)+","+str(line[0])+','+str(line[1])+','+str(line[2])+','+str(line[3])+','+str(line[4])+','+str(line[5])+','+str(line[6])+','+str(line[7])+"\n"
    f.write(str1)
    print(str1)
#    data.pop(-1)
#    data.insert(0,float(line2[0]))
#    plt.clf()
#    plt.ylim([-0.2,1.5])
#    plt.plot(x,data)
#    plt.pause(0.1)
  except KeyboardInterrupt:
    close(ser)
    close(f)
    print ('exiting')
    break
exit()
