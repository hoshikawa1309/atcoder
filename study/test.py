from pprint import pprint
matrix = [[1,2,3],[4,5,6],[7,8,9]]
pprint(matrix)

matrix = list(zip(*matrix))
pprint(matrix)