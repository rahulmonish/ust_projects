X = [[3, 5, 6],

     [4, 8, 10],

     [2, 1, 8]]

Y = [[1, 0, 0],

     [0, 1, 0],

     [0, 0, 1]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

if result==X:
    print("They are equal")
else:
    print("they are not equal")