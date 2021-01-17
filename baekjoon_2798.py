#2798
n_m=input()
n_m_split=n_m.split(' ')
n_list=input()
n_list_split=n_list.split(' ')
m=int(n_m_split[1])
n=int(n_m_split[0])
three_set=0
three_list=[] #set의 3개 원소를 담은 리스트
answer=[]
for i in range(n-2):
    for j in range(i+1,n-1):
        for x in range(j+1,n):
            three_set=int(n_list_split[i])+int(n_list_split[j])+int(n_list_split[x])
            if three_set<=m:
                answer.append(three_set)
answer.sort()
result=answer[-1]
print(result)
