# 4.2 Assign True or False to the variables small and green. Write some if/else statements to print which of these matches those choices: cherry, pea, watermelon, pumpkin.

small = True 
green = True 

if small and green:
    print ("pea")
elif small and not green:
    print("cherry")
elif not small and green:
    print("watermelon")
else:
    print("pumpkin")
