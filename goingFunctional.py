#func_sum(list) -> int
#Sums a list of numbers
def func_sum(y):
    if y:
        x = y.pop()
        return x + func_sum(y)
    return 0

#func_factorial(int) -> int
#product of all positive integers less than or equal to n
def func_factorial(n):
    if n > 1:
        return n * func_factorial(n - 1)
    return 1

def main():
    
    print(func_sum([1,2,4]))
    print(func_factorial(5))

if __name__ == "__main__":
    main()
