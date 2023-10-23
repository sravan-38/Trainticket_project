import datetime #import time_module
import random 
train_list = {"Tirupati_Express":'1234',"Chennai_Express":'4567',"Sabhari_Express":'6789',"Vande_Bharat_Express":"7890"}
print(train_list)
name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
gender = input("Enter YOur Gender: ")
train = input("Enter Which train you are looking: ")
for k,v in train_list.items():
        print("train name",k,"train number:",v)
ticket_rate = {"Tirupati_Express":'230',"Chennai_Express":'350',"Sabhari_Express":'150',"Vande_Bharat_Express":"550"}
for t,r in ticket_rate.items():
        print("select_train:",t,"ticketrates:",r)
pas = int(input("Enter number of passengers: "))
if train in ticket_rate:
        print(("ticket_rate:",int(ticket_rate[train])))
        price = (int(ticket_rate[train])*pas)
        print(price)
user_date = int(input("Enter your reservation date: "))
date = datetime.datetime(2023,10,user_date)
print("your reservation date: ",date)
print("your ticket was reserved:",datetime.datetime.now())
seat = input("select_seattype:")
class Train():
        def __init__(self  ,train_num,select_seat,source,destination,seats,):
            self.train_num = train_num
            self.select_seat = select_seat
            self.source = source
            self.destination = destination
            self.seats = seats
        def display_info(self):
            print("Train number:",self.train_num)
            print("select seat:",self.select_seat)
            print("source:",self.source)
            print("Destination:",self.destination)
            print("Available seats:",self.seats)
            print()
tr = Train("12345","AC","vij","hyd",2)
print(25*"__","WELCOME TO IRCTC",25*"__")
print("Name:",name)
print("Age:",age)
print("Gender:",gender)
print("Trainname:",train)
print(50*"  ","PNRNO:",random.randint(11111,1000000))
print(40*"  ","reservationdate:",date)
tr.display_info()
print(40*"  ","number of passengers:",pas,"TOTALFARE",price)
print(45*"  ","TOTALFARE:",price)
print(25*"  ","HAPPY_JOURNEY",25*"--")