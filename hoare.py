def partition_hoare(array, start, end):
    i, j = start, end - 1
# no explicit pivot
    while True:
        # infinite until return
        while array[i] <= array[end] and i < j:
            i += 1

        while array[j] >= array[end] and i < j:
            # second condition i<j makes sure that
            # i and j don't cross each other
            j -= 1

        if i == j:
            if array[i] <= array[end]:
                i += 1

            array[i], array[end] = array[end], array[i]
            return i
        else:
            array[i], array[j] = array[j], array[i]
