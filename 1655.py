from bisect import bisect_left
N=input()
num_list=[]
num_list.append(int(input()))
print(num_list[0])
for i in range(int(N)-1):
    num = int(input())
    # 숫자가 삽입 될 인덱스 찾기
    index = bisect_left(num_list, num)
    # 숫자 삽입, array 길이 1 증가
    num_list.insert(index, num)

    if len(num_list)%2==1:
        ind=int(len(num_list)/2)
        print(num_list[ind])
    else:
        ind=int(len(num_list)/2-1)
        print(num_list[ind])
