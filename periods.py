import time as ti
from datetime import datetime, timedelta, date, time
from tkinter import * 
from tkinter.ttk import *
from time import strftime


now = datetime.now()
Ctime= now.strftime("%H:%M:%S")
Ctime2 = now.time()
print ("Current time: ", Ctime2)
day= date.today().strftime("%A")
start = time(8, 00, 00)

def add45(time2):
	plus45 = 45
	delta = timedelta(minutes = plus45)
	#print(time2)
	t = time2
	time2=(datetime.combine(date(1,1,1),t) + delta).time()
	#print(time2)
	return time2
def add50(time2):
	plus50 = 50
	delta = timedelta(minutes = plus50)
	#print(time2)
	t = time2
	time2=(datetime.combine(date(1,1,1),t) + delta).time()
	#print(time2)
	return time2
def add5(time2):
	plus5 = 5
	delta = timedelta(minutes = plus5)
	#print(time2)
	t = time2
	time2=(datetime.combine(date(1,1,1),t) + delta).time()
	#print(time2)
	return time2
def add55(time2):
	plus55 = 55
	delta = timedelta(minutes = plus55)
	#print(time2)
	t = time2
	time2=(datetime.combine(date(1,1,1),t) + delta).time()
	#print(time2)
	return time2
print(day)
def tapDay():
	##need to include 40 minute tap period
	start = time(8, 00, 00)
	#print(start+add45(start))
	if Ctime2 >= start and Ctime2 < add45(start):
		#print("first period")
		perd="first period"
	else:
		start=add45(start)
		if Ctime2>=start and Ctime2 < add5(start):
			#print("Passing Period")
			perd="Passing period"
		start = add5(start)
		#print(start)
		if Ctime2>=start and Ctime2 < add50(start):
			#print("TAP Period")
			perd="TAP period"
		start=add45(start)
		#print(start)
		if Ctime2 >= start and Ctime2 < add45(start):
			#print("Second period")
			perd="Second period"
		start=add45(start)
		if Ctime2>=start and Ctime2 < add5(start):
			#print("Passing Period")
			perd="Passing period"
		start = add5(start)
		#print(start)
		if Ctime2 >= start and Ctime2 < add45(start):
			#print("Third period")
			perd="Third period"
		start=add45(start)
		if Ctime2>=start and Ctime2 < add5(start):
			#print("Passing Period")
			perd="Passing period"
		start = add5(start)
		#print(start)
		if Ctime2 >= start and Ctime2 < add45(start):
			#print("Fourth period")
			perd="Fourth period"
		start=add45(start)
		if Ctime2>=start and Ctime2 < add5(start):
			#print("Passing Period")
			perd="Passing period"
		start = add5(start)
		#print(start)
		if Ctime2 >= start and Ctime2 < add45(start):
			#print("Fifth period")
			perd="Fifth period"
		start=add45(start)
		if Ctime2>=start and Ctime2 < add5(start):
			#print("Passing Period")
			perd="Passing period"
		start = add5(start)
		#print(start)
		if Ctime2 >= start and Ctime2 < add45(start):
			#print("Sixth period")
			perd="Sixth period"
		start=add45(start)
		if Ctime2>=start and Ctime2 < add5(start):
			#print("Passing Period")
			perd="Passing period"
		start = add5(start)
		#print(start)
		if Ctime2 >= start and Ctime2 < add45(start):
			#print("Seventh period")
			perd="Seventh period"
		start=add45(start)
		if Ctime2>=start and Ctime2 < add5(start):
			#print("Passing Period")
			perd="Passing period"
		start = add5(start)
		#print(start)
		if Ctime2 >= start and Ctime2 < add45(start):
			#print("Eigth period")
			perd="Eigth period"
		else:
			perd="No classes right now"
		return perd



def normDay():
	##need to include 40 minute tap period
	start = time(8, 00, 00)
	#print(start+add45(start))
	if Ctime2 >= start and Ctime2 < add55(start):
		#print("first period")
		perd="first period"
		return perd
	else:
		start=add50(start)
		if Ctime2>=start and Ctime2 < add5(start):
			print("Passing Period")
			perd="Passing period"
		start = add5(start)
		#print(start)
		if Ctime2 >= start and Ctime2 < add50(start):
			print("Second period")
			perd="Second period"
		start=add50(start)
		if Ctime2>=start and Ctime2 < add5(start):
			print("Passing Period")
			perd="Passing period"
		start = add5(start)
		#print(start)
		if Ctime2 >= start and Ctime2 < add50(start):
			print("Third period")
			perd="Third period"
		start=add50(start)
		if Ctime2>=start and Ctime2 < add5(start):
			print("Passing Period")
			perd="Passing period"
		start = add5(start)
		#print(start)
		if Ctime2 >= start and Ctime2 < add50(start):
			print("Fourth period")
			perd="Fourth period"
		start=add50(start)
		if Ctime2>=start and Ctime2 < add5(start):
			print("Passing Period")
			perd="Passing period"
		start = add5(start)
		#print(start)
		if Ctime2 >= start and Ctime2 < add50(start):
			perd="Fifth period"
		start=add50(start)
		if Ctime2>=start and Ctime2 < add5(start):
			perd="Passing Period"
		start = add5(start)
		#print(start)
		if Ctime2 >= start and Ctime2 < add50(start):
			perd="Sixth period"
		start=add50(start)
		if Ctime2>=start and Ctime2 < add5(start):
			perd="Passing Period"
		start = add5(start)
		#print(start)
		if Ctime2 >= start and Ctime2 < add50(start):
			perd="Seventh period"
		start=add50(start)
		if Ctime2>=start and Ctime2 < add5(start):
			perd="Passing Period"
		start = add5(start)
		#print(start)
		if Ctime2 >= start and Ctime2 < add50(start):
			perd="Eigth period"
		else:
			perd="No Classes right now"
		return perd

def updater():
	global ctr
	ctr += 1
	tk_var.set(str(ctr))
	if ctr < 10:
		root.after(1000, updater)

if __name__ == '__main__':
	start2 = time(7, 59, 00)
	end = time(15, 21, 00)
	starttime = ti.time()
	print(Ctime2)
	print(start2)
	print(end)
	root = Tk()
	ctr=0
	tk_var = StringVar()
	root.title('Period')
	def time3():
		day= date.today().strftime("%A")
		string = strftime('%I:%M:%S %p')
		if day == "Wednesday":
			per = tapDay()
			lbl.config(text = day+"\n"+"TAP DAY"+"\n"+per+"\n"+string)
		elif day == "Saturday" or day=="Sunday":
			lbl.config(text = day+"\n"+"NO SCHOOL TODAY"+"\n"+string)
		else:
			per=normDay()
			lbl.config(text = day+"\n"+per+"\n"+string)
			
		
		lbl.after(1000, time3)

	lbl = Label(root, font = ('calibri', 120, 'bold'),
            background = 'white',
            foreground = 'black')
	lbl.pack(anchor = 'center')
	time3()
	updater()
	mainloop()

	'''
	booly = True
	
	if Ctime2<start2 or Ctime2>end:
		booly= False

	while booly:
		#print("tick")
		Ctime2 = now.time()
		print ("Current time: ", Ctime2.replace(microsecond=0).isoformat())
		day= date.today().strftime("%A")
		print(day)
		if day == "Wednesday":
			print("Tap")
			tapDay()
		else:
			normDay()
		ti.sleep(5.0 - ((ti.time() - starttime) % 5.0))

	
'''