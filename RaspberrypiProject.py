import random
import time
import datetime
import winsound
import os
from colorama import init, Fore, Back, Style

frequency = 2250  
duration = 2000
BedNumber = 4
oxygen_th = 95
temperature_th = 38
heartbeat_th = 130
pressure_th = 9
NoIssue = True

class HospitalBed: #a class for generate number
    def __init__(self): 
        self.oxygen = random.randint(90,100)
        self.temperature = random.randint(37,41)
        self.heartbeat = random.randint(50,150)
        self.pressure = random.randint(6,20)

def PrintData(list_HospitalBed): #print data
    BedCount = 1
    print("      OX TP HB PR")
    for obj in list_HospitalBed:
        print("Bed"+ str(BedCount) + ": ", end="") #for show bed number
        if obj.oxygen <= oxygen_th:
            print(Fore.RED + str(obj.oxygen) + Style.RESET_ALL, end=" ")
            NoIssue = False
        else:
            print(obj.oxygen, end=" ")
        if obj.temperature >= temperature_th:
            print(Fore.RED + str(obj.temperature) + Style.RESET_ALL, end=" " )
            NoIssue = False
        else: 
            print(obj.temperature, end=" ")
        if obj.heartbeat >= heartbeat_th:    
            print(Fore.RED+ str(obj.heartbeat) + Style.RESET_ALL, end=" ")
            NoIssue = False
        else:
            print(obj.heartbeat, end=" ")
        if obj.pressure <=9:
            print(Fore.RED + str(obj.pressure)  + Style.RESET_ALL)
            NoIssue = False
        else:
            print(obj.pressure)
        BedCount = BedCount + 1    

    if not NoIssue:
        winsound.Beep(frequency, duration)

def DataSimulator(list_HospitalBed): #update data 
    for obj in list_HospitalBed:
        obj.oxygen = random.randint(90,100)
        obj.temperature = random.randint(37,41)
        obj.heartbeat = random.randint(50,150)
        obj.pressure = random.randint(6,20)

list_HospitalBed = []

for i in range(BedNumber): #fill the list
    list_HospitalBed.append(HospitalBed())

while True:
    
    DataSimulator(list_HospitalBed)
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear') #clear terminal 
    x =datetime.datetime.now()
    print(x.strftime("%Y-%m-%d %H:%M:%S"))
    PrintData(list_HospitalBed)  #print data

    def sum(a,b):
         return a + b
    


    print(sum(3,2))
