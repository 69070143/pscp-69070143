"""SurprisingVote"""
def main():
    """Are there หน้าม้า in our votes?"""
    total_score = float(input())
    highest = float(input())
    lowest = total_score - (highest * 2)

    if lowest < 0:
        lowest = 0
    if highest - lowest > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
