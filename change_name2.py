# change_name2

import os

file_list=os.listdir(r"C:\새 폴더\kepco")
print(file_list)


file_list2=os.listdir("E:\광명지사 사진데이터\전체사진")

file_list3=os.listdir("E:\광명지사 사진데이터\전체사진"+"\\"+"과림간")

file_list4=os.listdir("E:\광명지사 사진데이터\전체사진"+"\\"+"과림간"+"\\"+"과림간10_9321Y311")
print(file_list4)
'''
for i in file_list4:
    os.rename("E:\광명지사 사진데이터\전체사진"+"\\"+"과림간"+
              "\\"+"과림간10_9321Y311"+"\\"+i,
              "E:\광명지사 사진데이터\전체사진"+"\\"+"과림간"+
              "\\"+"과림간10_9321Y311"+"\\"+i[:-5]+str(0)+i[-5]+'.jpg')
'''    
