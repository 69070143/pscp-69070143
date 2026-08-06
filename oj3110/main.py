"""สงคราม...ส่งด่วน"""
def main():
    """ค่าส่งเท่าไหร่"""
    place = input().split()
    start = place[0]
    end = place[1]
    weight = float(input())
    price = 0

    if start == "BKK" and end == "CNX":
        price = (weight * 30) + 10
    elif start == "CNX" and end == "UBP":
        price = (weight * 40) + 15
    elif start == "UBP" and end == "BKK":
        price = (weight * 40) + 20
    elif start == "BKK" and end == "PKT":
        price = (weight * 50) + 25
    elif start == "PKT" and end == "CNX":
        price = (weight * 60) + 30
    elif start == "UBP" and end == "PKT":
        price = (weight * 70) + 40
    else:
        print("Error")

    if price > 0:
        print(f"{price:.2f}")

main()
