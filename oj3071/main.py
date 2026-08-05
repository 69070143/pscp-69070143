"""จำนวน x ในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""
def main():
    """A < B , output x"""
    A = int(input())
    B = int(input())
    d = int(input())
    r = int(input())
    i = A
    count = 0
    for i in range(A,B+1):
        if i % d == r:
            count += 1
        i += 1
    print(count)
main()
