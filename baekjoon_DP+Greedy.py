#DP 피보나치수열 n번째 값 나타내는 함수

#피보나치 예시
p_list=[1,1,2,3,5,8,13]

#피보나치 생성 함수
new_p_list=[]
def pn(index_n):
    if index_n==0:
        return new_p_list.append(1)
    elif index_n==1:
        return new_p_list.append(1)
    else:
        return new_p_list.append( new_p_list[index_n-1]+new_p_list[index_n-2] )

for i in range(0,10):
    pn(i)
print(new_p_list)

#피보나치 수열에서 n번째 수열의 원소값 구하는 함수
def pn2(n2):
    if n2==0:
        return 1
    elif n2==1:
        return 1
    else:
        return pn2(n2-1)+pn2(n2-2)

print(pn2(3))