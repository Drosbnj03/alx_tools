def is_prime(number):
    if number == 0 or number == 1: 
        return False
    if number>0:
        for i in range(2,number):
            if (number%i)==0:
                return False
        return True
    else:
        return False

