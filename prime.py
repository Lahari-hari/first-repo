number = 7

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(number, "is not a prime")
            break;
        else:
            print(number, "is prime")
            break;
            
else:          
    print("not a prime")
