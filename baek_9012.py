T=int(input())
YesOrNo=[]
for i in range(T):
    stack_list=[]
    New=input()
    for j in range(len(New)):
        stack_list.append(New[j])
        if stack_list[-1]==")":
            try:
                if stack_list[-2]=='(':
                    del stack_list[-1]
                    del stack_list[-1]
            except:
                pass
    if len(stack_list)==0:
        YesOrNo.append("YES")
    else:
        YesOrNo.append("NO")
for answer in YesOrNo:
    print(answer)



