x = 2
print(x == 2)
print(x == 3)
print(x < 3)

name = "John"
age = 30

if name == "John" and age == 30:
    print(f"Your name is {name}, and you are {age} years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")


if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")


x = 3
if x == 2:
    print("x equals two!")
else: 
    print("x does not equal to two.")

x = [1,2,3]
y = [1,2,3]
print(x == y)
print(x is y)

for x in range(10):
    if(x % 2 == 0):
        continue
    print(x)
    
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]
# your code goes here
for number in numbers:
    if number == 237:
        break

    if (number % 2 != 0): 
        continue
        
    print(number)