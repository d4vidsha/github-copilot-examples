''' In this GitHub Copilot (GHC) example, the entire `possibilities` function 
    was made by GHC. The `main` function was partly written by David, but a 
    large portion was also written by GHC.

    It's also worth noting the pure ELEGANCE of the code in `possibilities`.
    It uses a recursive function to generate all possible combinations.
    Heck, this comment was also partly written by GHC.

    HUMANS NEED NOT APPLY.
'''

''' Given a target sum m, find all possible ways to make the sum with n terms.
'''
def possibilities(m, n):
    combos = []
    if n == 0:
        combos.append([])
    elif n == 1:
        if m == 0:
            combos.append([0])
        else:
            combos.append([m])
    else:
        for i in range(m+1):
            for c in possibilities(m-i, n-1):
                combos.append([i] + c)
    return combos

''' Run program.
'''
def main():

    # get inputs
    m = int(input("Target sum (m): "))
    n = int(input("Target number of terms (n): "))

    # print results
    combos = possibilities(m, n)
    print(f"Number of possibilities: {len(combos)}")
    for p in combos:
        print(p)

    return

if __name__ == "__main__":
    main()
