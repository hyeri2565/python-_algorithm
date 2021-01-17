#스택
#입력으로 주어지는 명령을 처리하는 프로그램
#push x: x를 스택에 넣는 연산
#pop : 스택 내에 가장 위에 있는 정수를 뺀 뒤 그 수를 출력, 빈 스택일땐 -1 출력
#size : 스택에 있는 정수의 개수를 출력
#empty: 스택이 비어있으면 1출력 아니라면 0을 출력
#top : 스택의 가장 위에 있는 정수 출력, 빈 스택일 땐 -1출력

#명령의 수 N
N=int(input())
command_list=[input() for _ in range(N)]
def stack(command):
    if command[0:2]=='pu':
        stack_list.append(int(command[5:]))
    elif command[0:3]=='pop':
        if len(stack_list)!=0:
            return stack_list.pop()
        else:
            return -1
    elif command[0:2]=='si':
        return len(stack_list)
    elif command[0:2]=='em':
        if len(stack_list)==0:
            return 1
        else:
            return 0
    elif command[0:3]=='top':
        if len(stack_list)!=0:
            return stack_list[-1]
        else:
            return -1

stack_list=[]
#print(stack(*command_list),'\n')
for i in range(len(command_list)):
    if command_list[i][0:2]!='pu':
        print(stack(command_list[i]))
    else:
        stack(command_list[i])