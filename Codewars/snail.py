# type: ignore

def snail(snail_map):
    final_array = []

    for i in range(len(snail_map)):
        for j in range(len(snail_map[i])):
            pass





array1 = [[1,2,3],
          [4,5,6],
          [7,8,9]] # [1,2,3,6,9,8,7,4,5]

array2 = [[1,2,3],
          [8,9,4],
          [7,6,5]] # [1,2,3,4,5,6,7,8,9]

print(snail(array1))
print(snail(array2))