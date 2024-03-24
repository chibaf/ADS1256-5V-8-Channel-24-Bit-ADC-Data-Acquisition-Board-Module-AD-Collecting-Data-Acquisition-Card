import serial, sys
import matplotlib.pyplot as plt

x=range(0, 100, 1)
data=[0]*100
ser = serial.Serial(sys.argv[1],19200)
while True:
  try:
    line = ser.readline()
    line2=line.strip().decode('utf-8')
    print(line2)
    data.pop(-1)
    data.insert(0,float(line2[0]))
    plt.clf()
    plt.ylim([-0.2,1.5])
    plt.plot(x,data)
    plt.pause(0.1)
  except KeyboardInterrupt:
    print ('exiting')
    break
exit()
