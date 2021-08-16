def collapse_array_tia(array, null_value):
    len_array = len(array)
    for i in range(len_array):
        if array[i] == null_value:
            for j in range(i+1, len_array):
                if array[j] != null_value:
                    array[i], array[j] = array[j], null_value
                    break

my_array = [-1, 2, 4, 1, -1, 5, -1, 7, -1, -1, -1, 10, -1]
print(my_array)
collapse_array_tia(my_array, -1)
print(my_array)

