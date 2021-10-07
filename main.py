from sortings import insertion_sort, selection_sort, merge_sort, shell_sort
from generators import generator1, generator2, generator3, generator4


def expirement_sorting():
    generator_list = [generator1, generator2, generator3, generator4]
    for power in range(7, 16):
        size = 2**power
        for generator in generator_list:
            expirements = generator(size)
            for expirement in expirements:
                insertion_sort(arr=expirement, expirement=generator.__name__[-1])
                selection_sort(arr=expirement, expirement=generator.__name__[-1])
                merge_sort(arr=expirement, expirement=generator.__name__[-1])
                shell_sort(arr=expirement, expirement=generator.__name__[-1])


if __name__ == '__main__':
    expirement_sorting()
