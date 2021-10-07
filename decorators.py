import time


def timer(func):
    def timed(**kwargs):
        start_time = time.time()
        comparisons = func(**kwargs)
        end_time = time.time()
        result_time = end_time - start_time

        arr = kwargs['arr']
        expiremnt = kwargs['expirement']
        expiremnt_str = f'Time and comparisons for {func.__name__} in expiremnt {expiremnt} with {len(arr)} elements: {result_time} {comparisons}'
        with open('results.txt', 'a') as file:
            file.write(expiremnt_str + '\n')

        return comparisons
    return timed
