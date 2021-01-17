#baekjoon1065_2
'''
N=int(input())

hansu=0
for i in range(1,N+1):
    if i<=99:
        hansu+=1
    else:
        num_arr=list(map(int,str(i)))
        if num_arr[0]-num_arr[1]==num_arr[1]-num_arr[2]:
            hansu+=1
print(hansu)

'''
N= int(input())
a=[] #등차수열 비교할 리스트
n=[] #한수인 숫자를 담은 리스트
num1=int()

for i in range(1,N+1):
    if i<=99:
        n.append(i)
    else:
        a.append(str(i))
    
for x in a: #리스트에서 스트링 하나씩 빼오기
    num1=int(x[1])-int(x[0])
        
    s=1
    for y in range(0,len(x)-1): #스트링 인덱스 가져오기
        if int(x[y+1])-int(x[y])==num1:
            s+=1
        if len(x)==s:
            n.append(x)
    
print(len(n))

