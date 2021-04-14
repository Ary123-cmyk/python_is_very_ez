import random
num = random.randint(1,9)
for tryd in range(4):
    ans = input("guess the number: ")
    try:
        ans = int(ans)
    except:
        print("Bro thats not even a number.")
        continue
    if ans == num and tryd == 0:
        print("WOW! first try!")
        raise SystemExit
    elif ans == num and tryd == 1:
        print("Second try! not bad!")
        raise SystemExit
    elif ans == num:
        print('You won!')
        raise SystemExit
    else:
        if num > ans:
            if num - ans < 4:
                print("You were close!")
            elif num - ans < 7:
                print("not quite!")
            elif num - ans == 8:
                print("wow ur really bad")
        if num < ans:
            if ans - num < 4:
                print("You were close!")
            elif ans - num < 7:
                print("not quite!")
            elif ans - num == 8:
                print("wow ur really bad")
        continue
print('You lost!')