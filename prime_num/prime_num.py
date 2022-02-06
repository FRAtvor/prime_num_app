import math

def prime_num_test(number):
    """
    tests if given number is prime number
    """
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif (number > 2) & (number % 2 == 0):  # even numbers, not prime numbers, saves loops
        return False
    
    max_divisior = math.floor(math.sqrt(number))
    for i in range(3, max_divisior+1, 2):      # <=1, 2, solved in if, max_div + 1 - exclusive behavior of range interval, step 2 - skip even numbers, solved in if statement 
        if number % i == 0:
            return False
    
    return True


def find_nearest_pn(number):
    """
    finds the nearest prime number, except given
    """
    step=1
    while True:
        if prime_num_test(number+step) == True:
            return number+step
        elif prime_num_test(number-step) == True:
            return number+step
        else:
            step += 1        

