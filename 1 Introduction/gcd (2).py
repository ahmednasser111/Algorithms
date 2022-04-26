def gcd(x, y):
    r = x % y
    if(r == 0):
        return y
    else:
        return gcd(y, r)


# try out the function with a few examples
print(gcd(60, 96))  # should be 12
print(gcd(20, 8))   # should be 4
