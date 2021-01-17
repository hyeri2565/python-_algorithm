'''
N=int(input())
num_list=[]
for n in range(N):
    num_list.append(int(input()))
num_list.sort()
for num in num_list:
    print(num)
    '''
n_list= sorted([ int(input()) for i in range(int(input()))])
print(*n_list,sep='\n')