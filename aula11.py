'''
1. Write a function called digit_sum that takes a positive integer n as input and
returns the sum of all that number’s digits. For example: digit_sum(1234) should
return 10 which is 1 + 2 + 3 + 4. (Assume that the number you are given will always
be positive.)
'''

def digit_sum(n):
    total = 0
    for i in range(0, len(n)):
        temp_i = int(n[i])
        total += temp_i
    return total


# print(digit_sum(str(1234)))

'''
2. Define a function factorial that takes an integer x as input.

Calculate and return the factorial of that number.
'''

def factorial(num):
    cont = num

    while cont <= num and cont > 1:
        cont -= 1
        print("Cont é %s" %(cont))
        num = num * cont
    
    return num

# print(factorial(3))

'''
3. Define a function called is_prime that takes a number x as input.

For each number n from 2 to x - 1, test if x is evenly divisible by n.

If it is, return False.

If none of them are, then return True.
'''

def is_prime(x):
    if x < 2:
        return False
    else:
        for i in (2, x-1):
            if x % i == 0:
                return False
        return True

# print(is_prime(5))
# print(is_prime(4))

''' 
4 - Define a function called reverse that takes a string textand returns that string in reverse. For example: reverse("abcd") should return "dcba".

You may not use reversed or [::-1] to help you with this.

You may get a string containing special characters (for example, !, @, or #).
'''

def reverse(s):
    word = ''
    # Precisa iterar intervalo <= 0 e o índice começa no 0, por isso len(s) - 1
    for i in range(len(s) -1, -1, -1):
        word += s[i]
    print(word)

# reverse('tati')