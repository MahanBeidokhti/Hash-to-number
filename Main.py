import hashlib
import csv

dict1   = {}
dict12 = {}
dict2   = {}
dict22 = {}

for num in range (0,10000):
    dict1[num] = hashed = hashlib.sha256(str(num).encode()).hexdigest()
for rev in dict1.keys():
    dict12[dict1[rev]] = rev
with open('C:\Users\username\C:\example.CSV') as file:
    grades_list = file.readlines()
    for line in grades_list:
        dict2[line.split(',')[0]] = line.split(',')[1].strip()
    for i in dict2.keys() :
        dict22[dict2[i]] = i

for key in list(dict22.keys()):
    print("%7s's number is %4s !" %(dict22[key],dict12[key]))