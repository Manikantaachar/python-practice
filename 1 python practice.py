#age difference
boy_name = input("boy name: ")
boy_age = int(input('boy age: '))
girl_name = input("girl name: ") 
girl_age = int(input('girl age: '))
age_diff = boy_age-girl_age
print(f"{boy_name} loves {girl_name} age difference {age_diff}")

#juniur vs senior
name = input("what is youer name: ")
age = int(input("what is yopur age: "))
if age<=18:
    print("the person is junior citizen")
elif age>=60:
    print("the pertson is sernior citizen")
else:
    print("the pertson is citizen")

#string methods
message = "warning "
print(message*10)
print(message.upper())
print(message.lower())
print(message.strip()*10)
print(message.replace("warning","Error"))

#Accesing string character
name = "Manikanta Achar"
print(len(name))
print(name[2])
print(name[5])
print(name[2:12])
print(name[2:])
print(name[-3])
print(name[::2])
print(name[1:8:3])

s = "Manikanta \nis a good boy"
print(s)