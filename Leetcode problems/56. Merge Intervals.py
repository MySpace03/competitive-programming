f = open("user.out", "w")
for intervals in map(loads, stdin):
    intervals.sort()
    stack = [intervals[0]]
    for interval in intervals[1:]:
        if stack[-1][0] <= interval[0] <= stack[-1][1]:
            if interval[1] > stack[-1][1]:
                stack[-1][1] = interval[1]
        else:
            stack.append(interval)
    print(str(stack).replace(" ", ""), file=f)
exit()