#File-dy oku line by line
def data_loader(filename):
    print('data_loader function')
    try:
       fin = open(filename)
       lines = fin.readlines()
       fin.close()
    except:   
       print('File ashylmadi')
       return []
    return lines


#Listten dictionary jasau
def dict1(lines):
    diction=dict()
    list1=[]
    list2=[]
    #Student list
    for line in lines:
        item = line[:-1].split(',')
        if line.startswith('Student'):
            diction={'class':item[0],'name':item[1],'lastname':item[2],'age':item[3],'rost':item[4],'score_m':int(item[5]),'score_h':int(item[6]),'score_p':int(item[7])}
            list1.append(diction)
	#Teacher list
        words = line[:-1].split(',')
        for word in words[5:]:
            if word!='-' and line.startswith('Teacher'):
                diction={'class':words[0],'name':words[1],'lastname':words[2],'age':words[3],'rost':words[4],'predmet':word}
                list2.append(diction)
    return list1,list2

#Testing
if __name__=="__main__":
    text=data_loader("class_data_9.txt")
    print(dict1(text))
