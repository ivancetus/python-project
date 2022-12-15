# https://www.youtube.com/shorts/g9fIWtSexLs

def is_prime(num):
    for x in range(2, num):
        if (num%x) == 0:
            return False
    return True


nums = range(1, 1000)
primes = list(filter(is_prime, nums))
print(primes)