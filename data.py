import serial.tools.list_ports 
import datetime
ports = serial.tools.list_ports.comports()
print(ports)
serialInst = serial.Serial()
portList = []
for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

# select the required port
val = input("select the required Port")
print(val)
# portVar = ''
for x in range(0, len(portList)):
    if portList[x].startswith("COM"+str(val)):
        portVar = "COM"+str(val)
        print(portList[x])
serialInst.baudrate = 115200
serialInst.port = portVar
serialInst.open()
def Convert(string):
    li = list(string.split(" "))
    return li
data=[]
while True:
    if serialInst.in_waiting:
        file1 = open("newtry_ews.txt","a")
        # file2 = open("position2.txt","a")
        packet = serialInst.readline()
        # data.append(packet)
        packet_data = (packet.decode("utf").rstrip("\n"))
        # print(type(packet_data))
        str1 = packet_data
        list_data = Convert(str1)
        print(list_data[0])
        # print(type(list_data))
        file1.write(packet_data)
        # file1.write(packet_data)1
        # file2.write(packet_data)
        # if(datetime.datetime.strptime(list_data[0], '%Y/%m/%d')):
        #     file1.write(packet_data)
        # if(len(list_data[0])>20):
        #     file2.write(list_data[0])
        print(packet_data)
        file1.close()
        # file2.close()
        