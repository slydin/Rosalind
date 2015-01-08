n = int(raw_input("Please input n the number of months: "))
k = int(raw_input("Please input k the number of offspring produced by a pair each month: "))

#recursive implementation
def bunnyFibRec(months, numOffSpring):
    if months <= 2:
        return 1
    return numOffSpring*bunnyFibRec(months-2,k) + bunnyFibRec(months-1,k)

#iterative implementation
def bunnyFibIterative(months, numOffSpring):
    if months <= 2:
        return 1
    bunnyFib1 = 1
    bunnyFib2 = 1
    bunnyFib3 = 1
    for i in range(2,months):
        bunnyFib3 = numOffSpring*bunnyFib1 + bunnyFib2
        bunnyFib1 = bunnyFib2
        bunnyFib2 = bunnyFib3
    return bunnyFib3

print bunnyFibRec(n, k)
print bunnyFibIterative(n,k)
