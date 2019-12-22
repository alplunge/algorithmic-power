# use recursion to implement a countdown counter


def countdown(x):
    if x == 0:
        print("time is up!")
        return
    else:
        print(x, "tick tock") 
        countdown(x-1)

countdown(5)
