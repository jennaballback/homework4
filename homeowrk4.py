def myfunc2 (blackjack, black, jack):
    print(blackjack,black,jack)
    sum = blackjack+black+jack
    if sum <= 21:
        print(sum)
    elif sum > 21:
        nsum = sum - 10
        print(nsum)
print(myfunc2 (1,3,2))