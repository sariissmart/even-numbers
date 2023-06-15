def is_even(x):
    return x % 2 == 0
    
numbers =  [0, 1 , 2 , 3 , 4 ,5 ,6 ,7 ,8 ,9 ,10]
for number in numbers:
    if is_even(number):
        print(number)
