import random
from typing import List


MAX_LIMIT = 10**5


def generate_random_arr(size: int) -> List[int]:
    arr = []
    for _ in range(size):
        rand_num = random.randint(0, MAX_LIMIT)
        arr.append(rand_num)

    return arr


def generator1(size: int):
    expirements = []
    for _ in range(5):
        expirements.append(generate_random_arr(size))
    
    return expirements


def generator2(size: int):
    arr = generate_random_arr(size)
    return [sorted(arr)]


def generator3(size: int):
    arr = generate_random_arr(size)
    return [sorted(arr, reverse=True)]


def generator4(size: int):
    expirements = []
    for _ in range(3):
        arr = []
        for _ in range(size):
            rand_num = random.choice([1, 2, 3])
            arr.append(rand_num)

        expirements.append(arr)

    return expirements
