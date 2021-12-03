def largest_divisor(n):
    largest_div = 0
    if n % 2 == 0:
        return n /2
    
    for i in range(1,n):
        if n % i == 0:
            largest_div = i
            print(largest_div)

largest_divisor(21)
