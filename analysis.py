from statistics import mean

sorting_names = ['insertion_sort',
                 'selection_sort',
                 'merge_sort',
                 'shell_sort']

def create_base_dict() -> dict:
    results_dict = {}

    for expirement in range(4):
        power_dict = {}
        for power in range(7, 16):
            measures_dict = {}
            for measure in ('time', 'comparisons'):
                sortings_dict = {}
                for sorting in sorting_names:
                    sortings_dict[sorting] = [] 
                measures_dict[measure] = sortings_dict
            power_dict[2**power] = measures_dict
        results_dict[expirement+1] = power_dict
    
    return results_dict


def read_results(filename: str) -> dict:
    results = create_base_dict()
    with open(filename, 'r') as file:
        for line in file:
            line = line.split(' ')
            
            sorting = line[4]
            expirement = int(line[7])
            size = int(line[9])
            time = float(line[11])
            comparisons = int(line[12])

            results[expirement][size]['time'][sorting].append(time)
            results[expirement][size]['comparisons'][sorting].append(comparisons)

    return results


def count_average(filename: str) -> dict:
    results = read_results(filename)

    for expirement in results:
        for size in results[expirement]:
            for measure in results[expirement][size]:
                for sorting in results[expirement][size][measure]:
                    lst = results[expirement][size][measure][sorting]
                    results[expirement][size][measure][sorting] = mean(lst)
    
    return results


def procces_results_for_graphs(filename: str) -> tuple:
    results = count_average(filename)

    x_axis = [2**power for power in range(7, 16)]
    y_axis = {}

    for expirement in results:
        sortings_info = {measure: {sorting: [] for sorting in sorting_names} for measure in ('time', 'comparisons')}
        for size in results[expirement]:
            for measure in results[expirement][size]:
                for sorting in results[expirement][size][measure]:
                    sortings_info[measure][sorting].append(results[expirement][size][measure][sorting])

        y_axis[expirement] = sortings_info           

    return (x_axis, y_axis)
