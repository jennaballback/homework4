def myfunc2 (blackjack, black, jack):
    print(blackjack,black,jack)
    sum = blackjack+black+jack
    if blackjack == 11 or black == 11 or jack == 11 and sum > 21:
        sum1 = sum - 10
        print(sum1)
    elif sum <= 21:
        print(sum)
    elif sum > 21:
        print("Bust")
    else:
        print("Error")
print(myfunc2 (11,3,2))
print(myfunc2 (1,2,3))
print(myfunc2(10,9,9))