"""Season"""
def main():
    """what is the season now? , season change every month%3 == 0"""
    month = int(input())
    day = int(input())
    if month in range(1,4):
        if month == 3 and day >= 21:
            print("spring")
        else:
            print("winter")
    elif month in range(4,7):
        if month == 6 and day >= 21:
            print("summer")
        else:
            print("spring")
    elif month in range(7,10):
        if month == 9 and day >= 21:
            print("fall")
        else:
            print("summer")
    elif month in range(9,13):
        if month == 12 and day >= 21:
            print("winter")
        else:
            print("fall")

main()
