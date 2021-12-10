# Import  modules
import classes as cl
import data_parser as dp

print('Entered main program')
text=dp.data_loader("class_data_9.txt")
list1,list2=dp.dict1(text)
list_avr=[]
#Student_list
for x in range(len(list1)-1):
	if list1[x]['class']=='Student':
		i=cl.Student(list1[x]['name'],list1[x]['lastname'],list1[x]['age'],list1[x]['rost'],list1[x]['score_m'],list1[x]['score_h'],list1[x]['score_p'])
	#average
	sum=i.score_m+i.score_p+i.score_h
	avr=sum/3
	print('Average: ',avr)
	print(i.print_info())
	print()
#Sort averages
	list_avr.append(avr)
list_avr.sort()
print('List of avereages: ',list_avr)
print()
#Maximum and Minimum average
max=None
min=None
for item in list_avr:
	if max is None or item>max:
		max=item
	if min is None or item<min:
		min=item
print('Min average: ',min)
print('Max average: ',max)
