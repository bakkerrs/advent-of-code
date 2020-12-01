# Get input file
with open("./2020/1/input.txt") as f:
    input = [int(x.strip()) for x in f.readlines()]

# Find the three entries that sum to 2020 and multiply them by eachother
for i in input:
    for j in input:
        for k in input:
            if(i + j + k == 2020):
                print(i*j*k)
                exit()

# This is not efficient as it is O(n^3), but it works!