# Get input file
with open("./2020/1/input.txt") as f:
    input = f.readlines()
input = [x.strip() for x in input]
input = [ int(x) for x in input ]

# Find the three entries that sum to 2020 and multiply them by eachother
for i in input:
    for j in input:
        for k in input:
            if(i + j + k == 2020):
                print(i*j*k)
                exit()

# This is not efficient as it is O(n^3), but it works!