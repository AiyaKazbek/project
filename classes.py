#Aiya and Galymzhan
class Person(): 
	age=0
	rost=0
	name=''
	lastname=''
	#constructor
	def __init__(self,init_name='Aiya',
	                  init_lastname='Kazbek',
			  init_age='19',
		          init_rost='170'):
		self.name=init_name
		self.lastname=init_lastname
		self.age=init_age
		self.rost=init_rost
		print('vse attributes initiony!!!')
	#Getter methods
	def get_name(self):
		return (self.name,self.lastname)
	def get_age(self):
		return self.age
	def get_rost(self):
		return self.rost
	#Setter method
	def set_name(self,new_name,new_last):
		self.name=new_name
		self.lastname=new_last
	def set_age(self,new_age):
		self.age=new_age
	def set_rost(self,new_rost):
		self.rost=new_rost

	#print person info in format
	def print_info(self):
		print('Name:',self.name,self.lastname)
		print("Age:",self.age)
		print('Rost:',self.rost)

#Student class  (Aiya)
class Student(Person):
	score_m=0
	score_h=0
	score_p=0
	def get_score_m(self):
		return self.score_m
	def get_score_h(self):
		return self.score_h
	def get_score_p(self):
		return self.score_p

	def set_score_m(self,new_score_m):
		self.score_m=new_score_m
	def set_score_h(self,new_score_h):
		self.score_h=new_score_h
	def set_score_p(self,new_score_p):
		self.score_p=new_score_p

	def __init__(self,init_name, init_lastname, init_age, init_rost, init_score_m, init_score_p, init_score_h):
		super().__init__(init_name,init_lastname,init_age,init_rost)
		self.score_m=init_score_m
		self.score_p=init_score_p
		self.score_h=init_score_h

	def print_info(self):
		print('Name:',self.name,self.lastname)
		print('Age:',self.age)
		print('Rost',self.rost)
		print('Math bal:',self.score_m)
		print('History bal:',self.score_h)
		print('Prog bal:',self.score_p)

#class Teacher  (Galymzhan)
class Teacher(Person):
	predmet=''

	def get_predmet(self):
		return self.predmet

	def set_predmet(self,new_predmet):
		self.predmet=new_predmet

	def __init__(self,init_name, init_lastname, init_age, init_rost, init_predmet):
		super().__init__(init_name,init_lastname,init_age,init_rost)
		self.predmet=init_predmet


	def print_info(self):
		print('Name:',self.name,self.lastname)
		print('Age:',self.age)
		print('Rost',self.rost)
		print('Predmet:',self.predmet)


#Aiya
if __name__=='__main__':
	Aia=Person()
	Aia.print_info()
	print()
	stud1=Student('Johnson','Robert',21,170,80,100,90)
	stud1.print_info()
	print()
	stud2=Student('Smith','Jack',20,180,85,98,85)
	stud2.print_info()
	print()
	stud3=Student('Taylor','Mary',21,165,87,96,80)
	stud3.print_info()
	print()
	stud4=Student('Weber','John',19,182,70,89,80)
	stud4.print_info()
	print()
	stud5=Student('Huber','Tom',20,175,90,95,97)
	stud5.print_info()
	print()
	t1=Teacher('Manson','Harry',45,178,'Mathematics')
	t1.print_info()
	print()
	t2=Teacher('White','Susanne',38,167,'History')
	t2.print_info()
	print()
	t3=Teacher('Huffman','Daniel',40,172,'Programming')
	t3.print_info()
	print()
	#average scores(Aiya)
	def average(a,b,c,d):
		sum1=a.score_m+a.score_p+a.score_h
		sum2=b.score_m+b.score_p+b.score_h
		sum3=c.score_m+c.score_p+c.score_h
		sum4=d.score_m+d.score_p+d.score_h

		avr1=sum1/3
		avr2=sum2/3
		avr3=sum3/3
		avr4=sum4/3
		return avr1,avr2,avr3,avr4
	
	print('Averages:', average(stud1,stud2,stud3,stud4))
	print()
	#Galymmzhan	
	#Maximum score
	maxm=None
	maxp=None
	maxh=None
	listm=[stud1.score_m,stud2.score_m,stud3.score_m,stud4.score_m]
	for item in listm:
		if maxm is None or item>maxm:
			maxm=item
	print('Max Math: ', maxm)
	
	listh=[stud1.score_h,stud2.score_h,stud3.score_h,stud4.score_h]
	for item in listh:
		if maxh is None or item>maxh:
			maxh=item

	print("Max History: ",maxh)

	listp=[stud1.score_p,stud2.score_p,stud3.score_p,stud4.score_p]
	for item in listp:
		if maxp is None or item>maxp:
			maxp=item

	print('Max Prog: ',maxp)
