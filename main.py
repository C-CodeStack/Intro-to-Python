def make_matrix():
  matrix=[[]]
  matrix = [["_" for x in range(5)] for x in range(5)]
  return matrix

def print_matrix(matrix):
  for row in matrix:
    print(' '.join(map(str,row)))

matrix = make_matrix()

# Do not modify the code above this line
# Begin your work on the code below
