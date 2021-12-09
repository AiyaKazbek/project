import classes as cl
####################################
### This modules works with file ###
####################################


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



def dict1(lines):
    diction=dict()
    list1=[]
    list2=[]
    for line in lines:
        item = line[:-1].split(',')
        if line.startswith('Student'):
            diction={'class':item[0],'name':item[1],'lastname':item[2],'age':item[3],'rost':item[4],'score_m':int(item[5]),'score_h':int(item[6]),'score_p':int(item[7])}
            list1.append(diction)
	#listTeacher
        words = line[:-1].split(',')
        for word in words[5:]:
            if word!='-' and line.startswith('Teacher'):
                diction={'class':words[0],'name':words[1],'lastname':words[2],'age':words[3],'rost':words[4],'predmet':word}
                list2.append(diction)
    
    return list1,list2

#def dict2(lines):
 #   diction=dict()
  #  list2=[]
   # for line in lines:
    #    words = line[:-1].split(',')
     #   for word in words[5:]:
      #      if word!='-' and line.startswith('Teacher'):
       #         diction={'class':words[0],'name':words[1],'lastname':words[2],'age':words[3],'rost':words[4],'predmet':word}
        #        list2.append(diction)
   # return list2
    
    
    
if __name__=="__main__":
    text=data_loader("class.txt")
    #words=get_words(text)
    print(dict1(text))
