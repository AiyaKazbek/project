# Import  modules
import classes as cl
import data_parser as dp

print('Entered main program')
text=dp.data_loader("class.txt")
list1,list2=dp.dict1(text)



print(list1)
for x in range(len(list1)):
	print(x)
	if list1[x]['class']=='Student':
		i=cl.Student(list1[x]['name'],list1[x]['lastname'],list1[x]['age'],list1[x]['rost'],list1[x]['score_m'],list1[x]['score_h'],list1[x]['score_p'])
	#average
	sum=i.score_m+i.score_p+i.score_h
	print('avr=',sum/3)
	print(i.print_info())
for x in range(len(list2)):
	print(x)
	if list2[x]['class']=='Teacher':
		l=cl.Teacher(list2[x]['name'],list2[x]['lastname'],list2[x]['age'],list2[x]['rost'],list2[x]['predmet'])

	print(l.print_info())