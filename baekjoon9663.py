#백트래킹
'''
n,n 체스판 위에 퀸 n개 서로 공격할 수 없게 놓은 문제
n이 주어졌을 때 퀸을 놓는 방법의 수
input=8 output=92


'''
'''
row_i=0
column_i=0

def fore_back(n):
    check_list=[]
    check_list2=[]
        
    for j in range(n):
        check_list2.append(0)
    for i in range(n):
        check_list.append(check_list2)
    

    for x in range(n*n):
        check_list[row_i][column_i]==1
        for y in range(check_list): # Q나왔을때 안되는 자리 -1 해주기
            for z in range(check_list[y]):
                if check_list[y][z] !=1 and y==row_i :
                    check_list[y][z]=-1
                if check_list[y][z] !=1 and z=column_i:
                    check_list[y][z]=-1
                if y==0:
                    while (y<n):
                        y+=1
                        z+=1
                        check_list[y][z]==-1
                if y<n-1:
                    while (y<_
        

print(fore_back(8))
'''

n=int(input())
count=0
row, left, right=[0 for i in range(n)], [0 for i in range(2*n-1)], [0 for i in range(2*n-1)]

def queenlocation(index):
    global count
    if index==n:
        count+=1
        return
    for col in range(n):
        if row[col]+left[index+col]+right[n-1+index-col]==0:
            row[col]=left[index+col]=right[n-1+index-col]=1
            queenlocation(index+1)
            row[col]=left[index+col]=right[n-1+index-col]=0

queenlocation(0)
print(count)
