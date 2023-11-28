# Generar la serie de Fibonacci hasta el término 50
n = 50
fibonacci_series = [0, 1]
while fibonacci_series[-1] + fibonacci_series[-2] <= n:
    fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])
print("Serie de Fibonacci entre 0 y 50:")
print(fibonacci_series)