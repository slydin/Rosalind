def mendelianInheritance(k, m, n):
    """ k - homozygous dominent allelles, m - heterozygous alleles
    n - homozygous recessive allleles"""
    N = k + m + n
    dominant100 = 0.0
    dominant75 = 0.0
    dominant50 = 0.0
    
    # 100% Dominant
    dominant100 = (k * ( 2*m + 2*n - 1 + k)) / (N*(N-1))
    # 75% Dominant
    dominant75 = (m * (m - 1))/ (N*(N-1))
    # 50% Dominant
    dominant50 = (2*m*n)/(N*(N-1))

    print dominant100 + dominant75 * (3.0/4) + dominant50 * (1.0/2)

k = float(raw_input("Number of homozygous dominant factors: "))
m = float(raw_input("Number of heterozygous dominant factors: "))
n = float(raw_input("Number of homozygous recessive factors: "))

mendelianInheritance(k,m,n)
