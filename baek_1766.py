inp = input().split(' ')
N=int(inp[0])
M=int(inp[1])
prob = [i for i in range(1, N + 1)]
for _ in range(M):
    if _ == 0:
        new_inp = input().split(' ')
        saved_first=int(new_inp[0])
        saved_last=int(new_inp[1])
        prob.remove(saved_last)
        new_first_index = prob.index(saved_first)
        prob.insert(new_first_index + 1, saved_last)
        saved_index = prob.index(saved_last)

    else:
        new_inp = input().split(' ')
        new_first=int(new_inp[0])
        new_last=int(new_inp[1])
        if new_first > saved_first:
            if new_last > saved_last:  # 3 1 / 4 2  -> 3142
                prob.remove(new_last)
                new_first_index = prob.index(new_first)
                prob.insert(new_first_index + 1, new_last)
                saved_first = new_first
                saved_last = new_last
            else:
                prob.remove(saved_last)
                prob.remove(new_last)
                # 3 2/ 4 1 -> 3 4 1 2
                prob.insert(prob.index(new_first) + 1, new_last)
                prob.insert(prob.index(new_first) + 2, saved_last)
                saved_first=new_first
                saved_last=new_last
        else:   # 4 2 /3 1 or 4 1 / 3 2
            if new_last<saved_last:
                prob.remove(new_last)
                prob.insert(prob.index(new_first)+1,new_last)
                saved_first=new_first
                saved_last=new_last
            else:
                prob.remove(new_last)
                prob.insert(prob.index(saved_last)+1,new_last)
                saved_first = new_first
                saved_last = new_last
prob=list(map(str,prob))
prob=' '.join(prob)
print(prob)
