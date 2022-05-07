def driver(speed):
    if speed <= 70:
        print ("OK")

    else:
        points = (speed-70)//5
        if points <= 12:
            print(f"Point: {points}")
        else:
            print("License suspended")


driver(int(input("Enter speed: ")))