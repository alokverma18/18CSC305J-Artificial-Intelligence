def TowerOfHanoi(n , source, destination, auxiliary):
    if n==0:
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from",source,"to",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)

n = 1
TowerOfHanoi(n,'A','B','C')
