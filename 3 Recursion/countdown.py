# use recursion to implement a countdown counter


def countdown(x):
    if x == 0:
        return print("Done!")
    else:
        print(x, "...")
        countdown(x-1)


countdown(5)
