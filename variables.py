#Data Types:7
#Numbers:Integer,eg.10,Float,eg.10.05,Complex,eg.10j,Boolian,eg.T/F. True/False
x=10
print(type(x))
x=10.05
print(type(x))
x=10j
print(type(x))
numb=10 > 8
print(type(numb))
#String:denoted by single of double quote: cannot edit string value
x="My name is Sougata Biswas"
print(type(x))
print(len(x))#longth of the string
print(x[0])#0th object in string
#x[1]="b"
print(x[2:4])
print(x[2:11])
print(x[2:7])
print(x.upper())
print(x.lower())
print(x[-1])
print(x[-7:-2])#from front side starts from 0 and from back side starts from -1. When fetching objects from strings, it excludes the extreme values.
#List:ordered,changable,collection of arrays,icludes different data types,duplicate entries
x=[10,20,30,40,50,'Ten',"Twenty","Thirty","Forty","Fifty",10,20,30,40,50,'Ten',"Twenty","Thirty","Forty","Fifty",10,20,30,40,50,'Ten',"Twenty","Thirty","Forty","Fifty"]
print(x)
print(x[2:4])
print(x[2:11])
print(x[2:7])
#print(x.upper())
#print(x.lower())
print(x[-1])
print(x[-7:-2])
x=[10,20,30,40,50,'Ten',"Twenty","Thirty","Forty","Fifty"]
x.append(1000)
print(x)
x.insert(7,1111)
print(x)
x.reverse()
print(x)
#Dictionary:Unordered,changable,different data types,no duplicate entries
mydic ={1:'Sandhya',2:'Rohit',5:'Binit',8:'Kapalkundali',7:'Rajnandini'}
print(mydic)
print(mydic[7])
print(mydic.get(8))
mydic[2]='Bhola'
print(mydic.get(2))
#Tuple:ordered,unchanged,duplicate entries,many types
mytuple=(2,4,6,8,10,"dui","chaar","chay","aat","dash",11,11,11,11,"egaaro","egaaro","egaaro","egaaro")
print(mytuple)
print(mytuple[2])
print(mytuple.count(11))
#Set:unordered,no duplicate
myset ={2,4,6,8,10,"dui","chaar","chay","aat","dash",11,11,11,11,"egaaro","egaaro","egaaro","egaaro"}
print(myset)
#Range
myrange=range(10)
print(myrange)
print(list(range(10)))