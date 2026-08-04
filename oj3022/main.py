"""Temperature"""
def main():
    """change temp from C , K , F , R"""
    temp = float(input())
    start_unit = input()
    final_unit = input()

# make temp to (celsius) for easy math
    if start_unit == "K":
        temp = temp - 273.15
    elif start_unit == "F":
        temp = (temp - 32)*(5 / 9)
    elif start_unit == "R":
        temp = (temp * (5 / 9)) - 273.15
# for answer that not (celsius)
    if final_unit == "K":
        ans = temp + 273.15
    elif final_unit == "F":
        ans = (temp * (9 / 5)) + 32
    elif final_unit == "R":
        ans = (temp + 273.15) * (9 / 5)
    else:
        ans = temp
    print(f"{ans:.2f}")
main()
