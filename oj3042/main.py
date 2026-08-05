"""หาร10ลงตัวมีอะไรบ้าง"""
def main():
    """main"""
    number = int(input())
    i = 0
    result = []
    for i in range(0,number+1):
        if not i % 10 :
            result.append(i)
        i += 10
    print(*result[::-1])
main()
