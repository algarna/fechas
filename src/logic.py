a = 93
b = 27
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else: 
    print ("a is equal to b")



a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")


exists = "Moon" in "This text will describe facts and challenges with space travel"
print(exists)
exists = "Moon" in "This text will describe facts about the Moon"
print(exists)
 

mass_percentage = "1/6"
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth")
