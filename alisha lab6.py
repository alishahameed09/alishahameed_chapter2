# question 1
import time
# (part a)
print("",time.strftime('%A %B %d %Y'))
# (part b)
print(time.strftime('%T  %p %Z on %x'))
# (part c)
print("I will meet you on ",time.strftime('%a %B %d at %x %p'))
print()
# question 2
forecast= "It will be a sunny day today"
# (part a)
print ("The number of occurences of string day is: ",forecast.count('day'))
# (part b)
print ("The index where substring sunny starts is:",forecast.index('sunny'))
# (part c)
print (forecast.replace('sunny','cloudy'))
# question 3
def even(n):
    global lst
    lst =[]
    for i in range(2,n):
       if i%2 or i%3:
           lst.append(i)
even(17)
print("The number divisible by 2 or 3 is:",lst)
# question 4
def mailaddress(name, profession, dept, institute, city, address):
    n = name
    pro = profession
    d = dept
    ins = institute
    ct = city
    adr=address
    print("{}, {}, {}, {}, {}, {}".format(n, pro, d, ins, ct, adr))
    print('Thanks')


mailaddress('Faisal', 'Asst. Prof', 'Computer Science','UIT', 'Karachi', 'Gulshan e Iqbal')



