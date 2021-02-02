# # O(n) space and time
def fizzBuzz():
    for n in range(1,101):
        if(n%3==0 and n%5 !=0):
            print("Fizz")
        elif(n%5==0 and n%3!=0):
            print("Buzz")
        elif(n%5==0 and n%3 ==0):
            print("FizzBuzz")
        else:
            print(n)


fizzBuzz()

# # ----------------------------------------------------------------------------

def primes(n):
    # O(n^2) Time | O(n) Space
    primes =[]
    nonPrimes=[]
    for num in range(1,n+1): 
        count=0
        for i in range(1,num+1):
            if(num%i==0):
                count+=1       
        if(count>2):
            nonPrimes.append(num)
            # print(num, "Is not a prime Number")      
        else:
            primes.append(num)
    print(primes)
          
n = input("Enter a Number: ")

primes(n)

# ----------------------------------------------------------------------------

import math        
# A function to print all prime factors of  
# a given number n 
def primeFactors(n): 
      
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        print 2, 
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            print i, 
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        print n 
          
# Driver Program to test above function 
  
n = 12
primeFactors(n) 

# # ----------------------------------------------------------------------------

def mySort(list):
    n = len(list)   
    for i in range(n): 
        for j in range(0, n-i-1): 
            if list[j] > list[j+1] : 
                list[j], list[j+1] = list[j+1], list[j] 
    print(list)            

        
  

array=[1,4,3,5,2]

mySort(array)

# # ----------------------------------------------------------------------------

def readFile():
    encryptor=10
    alphabet="abcdefghijklmnopqrstuvwxyz"
    file=open("demoFile.txt","r")
    encrypted = open("file.txt","w")
    for line in file:
        for letter in line: 
            if(letter==" "):
                encrypted.write(" ")
            elif (alphabet.index(letter.lower())): 
                encrypted.write(alphabet[(alphabet.index(letter.lower())+encryptor)%26])
           
def unScrambleA():
    encryptor=10
    alphabet="abcdefghijklmnopqrstuvwxyz"
    encrypted = open("file.txt","r")
    for line in encrypted:
        for letter in line:
            if(letter==" "):
                print(" ")
            else:
                print(alphabet[(alphabet.index(letter.lower())-encryptor)%26]) 

    
readFile()
unScrambleA()

# # ----------------------------------------------------------------------------

def unscramble():
    encryptor=10
    alphabet="abcdefghijklmnopqrstuvwxyz"
    
    words=open("wordList.txt","r")
    encrypted = open("file.txt","w")
    words.readline
    for lines in words:
        for letters in lines:
            letters.lower()
            if(letters in alphabet):
                encrypted.write(alphabet[(alphabet.index(letters.lower())+encryptor)%26])
                
            

           
    # print(letters)
    # for word in words:
    #     if letters in word:
    #         print(word)


unscramble()


# # ----------------------------------------------------------------------------
import string
def storyGame():
    alive=True
    win=False
    choice=""
    print("Welcome to the dungeon your life depends on the choices made from here forth")
    while(alive==True or win==False or choice!= 'q'):
        choice = raw_input("Make a choice to go left(l) or right(r):")
        
        if(choice=='l'):
            print("You have made it to a magical spring where you encounter an fairy")
            win=True
            break
        elif(choice=='r'):
            print("You encounter an ogore")
            alive=False
            break
        elif(choice=='q'):
            break
        else:
            print("Please enter a tunnel to the left or to the right")
        
    if(alive==False):
        print("YOU DIED BY THE OGRE!!!")
    elif(win==True):
        print("THE FAIRY GRANTED YOUR WISH AND LET YOU FREE")
    elif(choice=='q'):
        print("You have quit the trial")


storyGame()