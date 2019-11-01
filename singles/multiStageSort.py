from operator import attrgetter

def multiStageSort(toSort, specs):
    for key, order in reversed(specs):
        if order == "asc":
            reverse = False
        elif order == "desc":
            reverse = True
        else:
            Exception("sorting order must be 'asc' or 'desc'")
        toSort.sort(key=attrgetter(key), reverse=reverse)
    return toSort