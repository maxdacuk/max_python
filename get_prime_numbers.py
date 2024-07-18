#Вивести список всіх простих чисел від 0 до n
def get_prime_numbers(n: int) -> list:
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# Приклад використання
n = 30
print(get_prime_numbers(n))


def squares_sum(l: list) -> int:
    t = 0
    for x in l:
        t += x**2
    return t
    
    
w = [2, 4, 5, 8]
r = squares_sum(w)
print(r)