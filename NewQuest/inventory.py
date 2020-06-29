##Items bag
import time
time.sleep(1)
items = ["Gold,\n" "Canteen,\n" "Dagger,\n" "Cloak,\n" "Jerky\n" ]
count = 0
while True:
    try:
        items_max = int(input("How many items do you want to put in your bag? "))
        if items_max > 10 or items_max < 0:
            raise ValueError #this will send it to the print message and back to the input option
        count = count + 1
        break
    except ValueError:
        print("\nINVALID!!. The number must be in the range of 1-10.\n\n:")
count = 0
while count < items_max:
    items.append(input("What would you like to add?\n"))
    time.sleep
    count = count + 1
print("")
print("Your Inventory:")
time.sleep(1)
count = 0
while count <= items_max:
    print(items [count])
    time.sleep (0.5)
    count = count + 1
