def mortalFib(n, k):
    """n represents the number of months
    k represents the amount of months each rabbit lives
    it is assummed that the rabbits mature after a month
    Problem states that we are using first index not zeroth"""

    # Base case 1 C_n <= C_2 = 1
    # Base case 2 n <= k + 1
    if n <= 2:
        return 1
    elif n <= k + 2:
        return mortalFib(n-1,k) + mortalFib(n-2,k)
    else:
        index = n - 3
        rabbits = 0
        while index >=1:
            rabbits = rabbits + mortalFib(index,k)
            index = index - 1
        return rabbits

def mortalFibIterative(n, k):
    """ n represents the number of months
    k represents the amount of months each rabbit lives
    it is assummed that the rabbits mature after a month
    Problem states to use first index but I will alter it for zeroth index"""
    """ h = 2  """
    months = []
    # Since the rabbits grow within a month the starting cases go for the first two months
    # C_0 = C_1 = 1
    # number of months till they become mature m
    m = 2
    months.append(1)
    months.append(1)
    months.append(2)
    if 3 <= k - 1 + m - 2:
        for i in range(3,k+m-2):
            months.append(months[i-1]+months[i-2])
    for i in range(k+m-2,n):
        nextIndex = 0
        for j in range(i-k, i-m+1):
            nextIndex = nextIndex + months[j]
        months.append(nextIndex)
    return months[n-1]
n = int(raw_input("Number of months: "))
k = int(raw_input("Rabbit lifespan: "))

#print mortalFib(n,k)
print mortalFibIterative(n,k)
