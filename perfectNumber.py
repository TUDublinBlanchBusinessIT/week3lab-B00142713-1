#Abel Ikhaguebor
#17/02/2025
#perfectNumber.py

#A perfect number is one for which all the divisors of the number add up to the
#number itself. For example the divisors of 28 are 1,2,4,7,14 which added together gives 28
#write a function below called perfectNumber(x) which checks to see if x is a perfect number
def isPerfectNumber(n):
    divisors_list = []
    for i in range (1,n):
        if n % i == 0:
            divisors_list.append(i)
    return divisors_list

    
#The function should return True if the number is perfect and False if it is not

from divisors import divisors

#define the function header called perfectNumber expecting one argument


    #set a result variable to False by default
  

    #if the sum of all the divisors of the number is equal to the test number

        #set the result variable to be True
 

    #return the result variable
   

#uncomment the following line to test the perfectNumber function it should return True
        if (perfectNumber(8128)):
    return True
        else
    return False

print("8128 is a perfect number")

