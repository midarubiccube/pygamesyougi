def flatten_2dim(array):
    return [item for sublist in array for item in sublist]

def argmax_2dim(array):
    flat_array = flatten_2dim(array)

    row_num = len(array)
    max_index = flat_array.index(max(flat_array))

    return max_index // row_num, max_index % row_num

a = [[0,1,1],[2,2,5],[2,1,3]]
print(argmax_2dim(a))