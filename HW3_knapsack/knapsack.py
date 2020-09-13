import math

values_list = [25, 20, 15, 40, 50]
weights_list = [3, 2, 1, 4, 5]

def knapsack(values, weights):
    n = len(weights)
    W = 15  #weight capacity
    opsubset = []
    result = [[0 for w in range(W + 1)] for i in range(n)] # blank table

    for i in range(1, n):
        for w in range(1, W + 1):
            wi = weights[i]
            vi = values[i]

            if wi <= w:
                next_best = max([result[i - 1][w - wi] + vi, result[i - 1][w]])
                result[i][w] = next_best

                if w == W:  # building the optimal subset
                    opsubset.append(next_best - sum(opsubset))
            else:
                result[i][w] = result[i - 1][w]

    opmax = result[n - 1][W]

    print("Max Value for W = 6: ", opmax)
    print("Optimal value subset: ", opsubset)


# Open data file
data = open("data.txt")

# Create a list of lists to be sorted
master_list = []

# create lists to be filled
weights = []
vals = []

# import from file
for line in data:
    master_list.append(list(map(int, line.split())))

# fill lists from master
for list in master_list:
    weights.append(list[0])
    vals.append(list[-1])

# call knapsack function
knapsack(values_list, weights_list)