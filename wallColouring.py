def minCost(costs):
    k=len(costs[0])
    n=len(costs)
    if k>1 and n>1:
        for i in range(1,n):
            for b in range(k):
                costs[i][b]+=min(costs[i-1][:b]+costs[i-1][b+1:])
    if k==1 and n!= 1:
        return -1
    elif n==1 and k==1:
        return costs[0][0]
    else:
        return min(costs[-1]) 

costs = [[1, 5, 7],
         [5, 8, 4],
         [3, 2, 9],
         [1, 2, 4]]
print(minCost(costs))
