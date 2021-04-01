matrix = [
    #Row1 0
    [1,2,3],
    #Row2 1
    [4,5,6],
    #Row3 2
    [7,8,9]
]

## Use a nested to loop to iterate through a matrix 

for row in matrix:
    for item in row:
        print(item)