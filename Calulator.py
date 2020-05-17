import math

def pythag(a, b):
    return math.sqrt((a ** 2) + (b ** 2))

def qaudratic(a, b, c):
    e = math.sqrt((b * b) + (4 * a * c))
    if e > 0:
        e1 = ((-b) + (e)) / (2 * a)
        e2 = ((-b) - (e)) / (2 * a)
    else:
        print("not good, stupid")
    return e1, e2

a, b, c = input("Enter a number for a, b, and c. If you don't have c enter None for it's place ").split(" ")

if c == "None":
    print(pythag(float(a), float(b)))
else:
    print(qaudratic(float(a), float(b), float(c)))
