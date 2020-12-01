# Get input file
with open("./2020/1/input.txt") as f:
    input = f.readlines()
input = [x.strip() for x in input]
input = [ int(x) for x in input ]

# Find the two entries that sum to 2020 and multiply them by eachother
for i in input:
    for j in input:
        if(i + j == 2020):
            print(i*j)
            exit()
