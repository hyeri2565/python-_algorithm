
file3_list=[]
file_list=os.listdir("E:\광명지사 사진데이터\전체사진")
for file in file_list:
    print(file)
    entries=os.listdir("E:\광명지사 사진데이터\전체사진"+"\\"+file)  #total folder
    for file2 in entries:
        try:
            entries2=os.listdir("E:\광명지사 사진데이터\전체사진"+"\\"+file+"\\"+file2)   #total folder2
        except:
            continue
        else:
            
            for file3 in entries2:
                a=file3.rfind('_')
                b=file3.rfind('.')
                if file3[a+1:b][0]=='0':
                    continue
                else:
                    os.rename("E:\광명지사 사진데이터\전체사진"+"\\"+file+"\\"+file2+"\\"+file3,
                              "E:\광명지사 사진데이터\전체사진"+"\\"+file+"\\"+file2+"\\"+file3[:a+1]+str(0)+file3[a+1:b]+".jpg")
               
