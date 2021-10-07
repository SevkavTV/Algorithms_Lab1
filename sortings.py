from typing import List
from decorators import timer


@timer
def selection_sort(arr: List[int], expirement: int) -> int:
    arr = arr.copy()
    comparisons = 0
    for i in range(len(arr)-1):
        mins_ind = i
        for j in range(i+1, len(arr)-1):
            if arr[j] < arr[mins_ind]:
                mins_ind = j
            comparisons += 1
        
        arr[i], arr[mins_ind] = arr[mins_ind], arr[i]

    return comparisons


@timer
def insertion_sort(arr: List[int], expirement: int) -> int:
    arr = arr.copy()
    comparisons = 0
    for i in range(1, len(arr)):
        curr_element = arr[i]
        j = i - 1
        while j >= 0 and curr_element < arr[j]:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        comparisons += 1
        arr[j + 1] = curr_element

    return comparisons


@timer
def merge_sort(arr: List[int], expirement: int) -> int:
    return _merge_sort_count(arr)


def _merge_sort_count(arr: List[int]) -> int:
    arr = arr.copy()
    comparisons = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        comparisons_right = _merge_sort_count(left)
        comparisons_left = _merge_sort_count(right)
        comparisons += comparisons_right + comparisons_left

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              arr[k] = left[i]
              i += 1
            else:
                arr[k] = right[j]
                j += 1
            comparisons += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return comparisons


@timer
def shell_sort(arr: List[int], expirement: int) -> int:
    arr = arr.copy()
    comparisons = 0
    
    n = len(arr)
    gap = 1

    while gap < n/3:
        gap = gap * 3 + 1

    while gap >= 1:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                comparisons += 1
                arr[j] = arr[j - gap]
                j -= gap
                
            comparisons += 1
            arr[j] = temp

        gap //= 3
    
    return comparisons
    
