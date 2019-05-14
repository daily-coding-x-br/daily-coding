from time import sleep

def run_after_delay(n, f, args):
    sleep(n/1000)
    f(args)


if __name__ == "__main__":
    # read number of miliseconds
    n = int(input())
    f = lambda name: print("Hello "+name+"!")

    # run funtion five times
    for _ in range(5):
        run_after_delay(n, f, "World") 
