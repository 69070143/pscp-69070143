"""Bill"""
def main():
    """include service charge and vat7%"""
    food_drink = int(input())
    service_charge = food_drink * 0.1
    if service_charge < 50:
        service_charge = 50
    elif service_charge > 1000:
        service_charge = 1000

    vat = (food_drink + service_charge) * 0.07
    total = food_drink + service_charge + vat
    print(f"{total:.2f}")

main()
