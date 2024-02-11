"""
El juego de fizzBuzz consiste en ir contando desde 1 hasta un número muy alto o que alguien se equivoque.
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
...
"""

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)

print("Fin del juego")

# otra forma + sencilla
for i in range(1, 51):
    res = ""
    if i % 3 == 0:
        res += "Fizz"
    if i % 5 == 0:
        res += "Buzz"
    if not res:
        res = str(i)
    print(res)
