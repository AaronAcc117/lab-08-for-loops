myData = {"effective top tube length": 515, "seat tube length": 500, "seat tube angle": 74.4, "head tube angle": 70.5, "stack": 513, "reach": 367, "standover height": 755}

# I concatenate 
for key, value in myData.items():
    print(f"key: {key}, value: {value}")

# Collects all keys into a separate list and then it prints
all_keys = list(myData.keys())
print("ALL KEYS:", all_keys)

#  gets the values into another list and prints
all_values = list(myData.values())
print("ALL VALUES:", all_values)
