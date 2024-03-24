from read_ser_ads1256_class import ads1256
import serial, sys
import time

def record(array):
  line=""
  for i in range(0,len(array)-1):
    line=line+str(array[i])+","
  line=line+str(array[len(array)-1])+"\n"
  return(line)

ads=ads1256()
ser = serial.Serial(sys.argv[1],sys.argv[2])
file1=open(sys.argv[3],"w")

try:
  while True:
    data=ads.read_ads1256(ser)
    print(str(data))
    file1.write(record(data))
    time.sleep(0.1)
except KeyboardInterrupt:
  file1.close()

exit()