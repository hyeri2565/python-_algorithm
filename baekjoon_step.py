#baekjoon step by step test

#1 배열 최대최소
'''
s=int(input())
n=input()
N=list(map(int,n.split(' ')))
print("{} {}".format(min(N), max(N)))
'''

#2 최댓값 2562
'''
N=[]
for i in range(9):
    N.append(int(input()))
print('{}\n{}'.format(max(N),N.index(max(N))+1))
'''

#3 아스키 코드 11654
'''
A=input()
print(ord(A))
'''
# chr를 아스키 코드로 변환하려면 ord함수사용

#4 숫자 더하기 11720
'''
B=input()
A=input()
s=0
for i in A:
   s+=int(i)
print(s)
'''

#5 알파벳 찾기 10809
'''
S=input()
hash={}
for i in range(97,123):
    
    if chr(i) in S:
        hash[chr(i)]=S.index(chr(i))
    else:
        hash[chr(i)]=-1
for j in hash.values():
    print("{}".format(j),end=' ')
'''

#6 알파벳 반복 2675
'''
n=int(input())
list=[]
for i in range(n):
    a=input()
    list.append(a)
    

for j in list:
    #hash[int(j.find(' '))]=j[j.find(' ')+1:]
    #print([z*int(j.find(' ')) for z in j],end='')
    s=j.find(' ')
    
    a=j[s+1:]
    
    for z in a:
        
        
        print(z*int(j[:s]),end='')
    print(end='\n')    
'''
#7 백트레킹 조합 15649
'''
n=input()
total_num=int(n[0])
select_num=int(n[2])
num_list=[]
for i range(1,total_num+1):
    num_list.append(i)
for i range(len(total_num)):
    total_num[i:select_num]
'''
a=input()
a1=int(a[0])
a2=int(a[2])
new_list=[]
a1_list=[i for i in range(1,a1+1)]
print(a1_list)
for i in a1_list:
    for j in range(a2):
        for x in a1_list:
            new_list.append(x)



#baekjoon 15649 제출 _순열
'''
from itertools import permutations
A=input()
a=int(A[0])
b=int(A[2])
a_list=[i for i in range(1,a+1)]
list2=[i for i in permutations(a_list,b)]
for x in list2:
    for y in range(len(x)):
        print(x[y], end=' ')
    print(end='\n')
'''

# baekjoon 조합 15650
'''
from itertools import combinations

A=input()
a=int(A[0])
b=int(A[2])
a_list=[i for i in range(1,a+1)]
comb_list=[i for i in combinations(a_list,b)]
for i in comb_list:
    for j in range(len(i)):
        print(i[j],end=' ')
    print(end="\n")
    
'''
