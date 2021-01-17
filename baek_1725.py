C=int(input())
num_list=[]
for c in range(C):
    num_list.append(int(input()))
max_list=[]
for i in range(C-1):
    sum_i=i+1
    we=1
    new_max=0
    new_i=i
    while True:
        if num_list[sum_i]>=num_list[new_i]:
            new_max=num_list[new_i]*(we+1)
            sum_i+=1
            we+=1
        else:
            if (we+1)*num_list[sum_i]>=new_max:
                new_max=(we+1)*num_list[sum_i]
                new_i=sum_i
                sum_i+=1
                we+=1
        if sum_i==C:
            max_list.append(new_max)
            break
max_list.append(num_list[-1])
max_list.sort()
print(max_list[-1])