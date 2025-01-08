def is_prime(num: int) -> bool:
    if num > 1:
        for i in range(2, (num//2)+1):
            if (num % i) == 0:
                return True
        return False
    else:
        return True
