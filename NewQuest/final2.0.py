def hundreds():
    store = []
    hund = 0
    count = 0
    while hund <= 0:
        try:
            store_name.append(int(input("How many hundreds does " + store[count] + " have?\n")))
            hund += 1
            count += 1
        except ValueError:
            print("This input is not valid. Please enter valid information.")
    return hund
hundreds()
