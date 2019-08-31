inp = int(input())
inp_split = [int(i) for i in str(inp).split('0')]

result = []
for i in range(len(inp_split)):
    inp_sort = [int(j) for j in str(inp_split[i])]
    inp_sort.sort()
    for j in inp_sort:
        result.append(str(j))

result_join = int("".join(result))
print("Input : %d" % inp)
print("Result : %d" % result_join)