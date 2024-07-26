def fibonacci(n):
    fibo_sequence = [0,1]
    while len(fibo_sequence) < n:
        fibo_sequence.append(fibo_sequence[-1] + fibo_sequence[-2])
    return fibo_sequence[:n]

n = int(input("How many terms do you want to calculate?"))
fibo_sequence = fibonacci(n)
total = sum(fibo_sequence)

print(f"Fibonacci Series : {fibo_sequence}")
print(f"Total : {total}")