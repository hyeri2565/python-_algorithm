#Divide and Conqure
#종이의 개수
row_num=int(input())
paper_list=[]
for i in range(row_num):
    paper_list.append(list(map(int,input().split())))
paper_dict={0:0,1:0,-1:0}
for paper in paper_list:
    paper_dict[0]=paper_dict[0]+paper.count(0)
    paper_dict[1]=paper_dict[1]+paper.count(1)
    paper_dict[-1]=paper_dict[-1]+paper.count(-1)
print( int(paper_dict[0]/(row_num/3)) )
print( int(paper_dict[1]/(row_num/3)) )
print( int(paper_dict[-1]/(row_num/3)) )

