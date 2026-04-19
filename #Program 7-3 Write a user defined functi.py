#Program 7-3 Write a user defined function to add 2 numbers and display their sum.

#Program 7-3
#Function to add two numbers 
#The requirements are listed below:
      #1. We need to Accept 2 numbers from the User.
#2. Calculate their sum 
#3. Display the sum

#function defination
def addnum():
    fnum = int (input(" enter first number:"))
    snum = int (input(" enter second number : "))
    sum = fnum + snum
    print("The sum of ",fnum,"and",snum,"is",sum)
addnum()
                    