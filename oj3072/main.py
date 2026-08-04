"""A-E-I-O-U"""
def main():
    """(A,a) is the same , output how much VOWEL"""
    string = input().lower()
    vowel = ["a" , "e" , "i" , "o" , "u"]
    x = 0
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    stop = len(string)
    for x in range(0,stop):
        check = string[x]
        if check in vowel[0]:
            a += 1
        elif check in vowel[1]:
            e += 1
        elif check in vowel[2]:
            i += 1
        elif check in vowel[3]:
            o += 1
        elif check in vowel[4]:
            u += 1
        x += 1
    if a >= 1:
        print(f"a : {a}")
    if e >= 1:
        print(f"e : {e}")
    if i >= 1:
        print(f"i : {i}")
    if o >= 1:
        print(f"o : {o}")
    if u >= 1:
        print(f"u : {u}")
main()
