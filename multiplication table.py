no_for_mulitplication = int(input("enter no. u want to multiple:"))

i = int(input("enter limit of multiplication:"))
j = 1

while j<= i:
    result = no_for_mulitplication * j
    print(f"{i} x {j} = {result}")
    j += 1
print ("thank you")