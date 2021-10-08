class User:
    name = ''
    email = ''
    password = ''
    login = False

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def login(self):
        email = input("Enter your email: ")
        password = input("Enter password: ")
        if email == self.email and password == self.password:
            login = True
            print("Login Successfully")
        else:
            print("login Failed !")
    def logout(self):
        login = False
        print("Logged out!")
    def isLoggedin(self):
        if self.login:
            return True
        else:
            return False
    def profile(self):
        if self.isLoggedin():
            print(self.name, self.email)
        else:
            print("User is not Logged in!")

user1 = User("M-R Maheen", "m@gmail.com", "1")

user1.login()
user1.profile()

hello = input()







''' constructor,,,,,,,,
class testClass:
    def __init__(self):
        print("I am a constructor")
    def fun_one(self):
        print("I am function one")
    def fun_two(self):
         print("I am another function Two")
ob = testClass()
ob.fun_one()'''

'''class User:
    name = ''
    email = ''
    password = ''
    login = False

    def login(self):
        email = input("Enter your email: ")
        password = input("Enter password: ")
        if email == self.email and password == self.password:
            login = True
            print("Login Successfully")
        else:
            print("login Failed !")
    def logout(self):
        login = False
        print("Logged out!")
    def isLoggedin(self):
        if self.login:
            return True
        else:
            return False
    def profile(self):
        if self.isLoggedin():
            print(self.name, self.email)
        else:
            print("User is not Logged in!")

user1 = User()
user1.name = "M-R Maheen"
user1.email = "m@gmail.com"
user1.password = "1"

user1.login()
user1.profile()

hello = input()'''




''' class 10 dauflt func: global & local variables,,,,,
var = 10

def simpleFunction():
    loc = var
    loc = loc + 1
    print(var)



simpleFunction()'''


'''dauflt parameters ,,,
    def wishCard(name, wish="Happy Birthday to "):
    print(wish, name)


wishCard("GM Sanzid Ahmed Srabon", "Happy Friendship day")
'''


'''def simpleFunction(num1, num2=10):
    print(num1, "-", num2)

simpleFunction(2)'''
# class 9 environment setting,,,,,,,,,,,,,,,,,,
'''#class 8 (function paramer pass),,,,,,,,,,,,
def Sum(num1, num2, num3):
    _sum = num1 + num2 + num3
    print(_sum)
Sum(20, 60, 2)'''


'''class 7 (simple function).....................
def simpleFunction():
    print("say hello to function")
    a, b = 15, 30
    sum  = a + b
    print(sum)

simpleFunction()
simpleFunction()'''






'''class 6 (while & for loop),,,,,,,,,,,,,,,,,,,,,,
 for loop......................

data = [5, 6, 7, 89, 77, 66, 77, 88, 99, 77, 00, text]

for x in data:
    print(x)'''

''' while loop..................
data = [5, 6, 7, 89, 77, 66, 77, 88, 99]
i = 1
while i<=8:
    print(data[i])
    i+=1'''


''' class 5 while loop condition
i = 1
while i<=30:
    if i%2 == 1:
        print(i)

    i+=1'''

'''i = 1
while i<=10:
    print("I love myself", i)
    i = i + 1
    i+=1 concating loop'''
# while condition:
# code
# condition

''' class 4  use if + else + elif/ else if
age = 20

if(age >= 35):
    print("Congratualations!!")
    print("You are an adult Man.")
    print(" Now,you can enjoys it.!!")

else:
    print("Sorry!")
    print("You are not an adult")
    print("you can't enjoys it, SORRY 'you are a Teenager!'")'''



''' (class 3) concatination & variables math oprations
x,y,e = (100, 3000,5555)

print(x)
print(y)'''

'''text = " Fifty and Fifty makes "

math = 25 + 25
math1 = 25 + 25

result = str(math + math1)

print(text + result)'''

'''myVar = "  I love you "

name = "Hassan"

fun = " mahamud "

print(myVar + name + fun)'''


''' class 2  (+),(-),(*),(/)
english = 93
bangla = 85
math = 99
economic = 25

total = english+bangla+math+economic

print("Your total subject mark is",total)'''