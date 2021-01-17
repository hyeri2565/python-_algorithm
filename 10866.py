N=int(input())
Deq=[]
for i in range(N):
    command=input()
    #push_front and push_back처리
    if command[0:4]=='push':
        command_list=command.split(' ')
        command_num=int(command_list[1])
        #조건 맞으면(f로시작하는 front) 앞에 추가 아니라면 뒤에 추가(append)
        if command[5]=='f':
            Deq.insert(0,command_num)
        else:
            Deq.append(command_num)
    #pop처리
    elif command[0:3]=='pop':
        #pop 앞에서 빼올지 뒤에서 빼올지 선택, Deq가 비었을 땐 -1 출력
        if command[-5:-1]=='front':
            if len(Deq)!=0:
                Deq.pop(0)
            else:
                print(-1)
        else:
            if len(Deq)!=0:
                Deq.pop()
            else:
                print(-1)
    #size처리
    elif command[0]=='s':
        print(len(Deq))
    #empty처리
    elif command[0]=='e':
        #비었을 땐 1 출력 아니라면 0 출력
        if len(Deq)==0:
            print(1)
        else:
            print(0)
    #앞 원소 뒤 원소 출력하기 front and back
    elif command[0]=='f':
        if len(Deq)!=0:
            print(Deq[0])
        else:
            print(-1)
    elif command[0]=='b':
        if len(Deq)!=0:
            print(Deq[-1])
        else:
            print(-1)
