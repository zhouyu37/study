#_*_coding:utf-8_*_

import re
import os

def menu():
	print('''
        ----------------------------------------------------
	|                                                  |
	|==================func menu=======================|
	|                                                  |
	|    1 import student info                         |
	|    2 find student info	                   |
	|    3 delete student info			   |
	|    4 modify student info                         |
	|    5 sort					   |
	|    6 statistic num of students                   |
	|    7 diplay all students' info		   |
	|    0 exit					   |
	|						   |			
	|==================================================|
        ''')

def main():
	ctrl=True
	while ctrl:
		menu()
		option_int=input("please select:")
		if option_int == 0:
			print("exit")
			ctrl=False
		elif option_int == 1:
			insert()
		elif option_int == 2:
			search()
		elif option_int == 3:
			delete()
		elif option_int == 4:
			modify()
		elif option_int == 5:
			sort()
		elif option_int == 6:
			total()
		elif option_int == 7:
			show()

def insert():
	studentlist=[]
	mark=True
	while mark:
		id=input("input ID:")
		if not id:
			break
		name=raw_input("input name:")
		if not name:
			break
		try:
			english=int(input("input english score:"))
			python=int(input("input python score:"))
			c=int(input("input c score:"))
		except Exception as e:
			print("input is invalid")
			continue
		student={"id":id,"name":name,"english":english,"python":python,"c":c}
		studentlist.append(student)
		inputMark=raw_input("continue add student?(y/n):")
		if inputMark == "y":
			mark = True
		else:
			mark=False
	save(studentlist)
	print("insert student info success!")

def search():
	mark=True
	student_query = []
	while mark:
		id = ""
		name=""
		if os.path.exists("student.txt"):
			mode=input("id is 1 and name is 2:")
			if mode == 1:
				id=input("input the student id:")
			elif mode == 2:
				name=raw_input("input the student name:")
			else:
				print("the input is invalid,please retry again!")
				search()
			with open("student.txt","r") as rfile:
				student_old=rfile.readlines()
				for stu in student_old:
					d=dict(eval(stu))
					if id:
						if d['id'] == id:
							student_query.append(d)
					elif name:
						if d['name'] == name:
							student_query.append(d)
			show_student(student_query)
			student_query=[]
			inputMark=raw_input("if contiue(y/n)")
 			if inputMark == "y":
				mark = True
			else:
				mark = False

		else:
			print("there is no data")
			return

def delete():
	mark=True
	while mark:
		try:
			studentid=int(input("input deleted ID:"))
		except Exception as e:
			print("input1 is invalid")
			continue
		if studentid:
			if os.path.exists("student.txt"):
				with open("student.txt","r") as rfile:
					student_old=rfile.readlines()
			else:
				student_old=[]
			ifdel = False
			if student_old:
				with open("student.txt","w") as wfile:
					for list in student_old:
						if dict(eval(list))["id"] !=studentid:
							wfile.write(list)
						else:
							ifdel=True
				if ifdel:
					print("%s has deleted!" % studentid)
				else:
					print("%s cannot find" % studentid)
		show()
		inputMark=raw_input("continue del student?(y/n):")
                if inputMark == "y":
                        mark = True
                else:
                        mark=False	
		

def modify():
	show()
	if os.path.exists("student.txt"):
		with open("student.txt","r") as rfile:
			student_old=rfile.readlines()
	else:
		return 
	student_id=input("which id should be modified!:")
	with open("student.txt","w") as wfile:
		for line in student_old:
			d=dict(eval(line))
			if d["id"] == student_id:
				print("i find this student which should be modified!")
				while True:
					try:
						d["name"]=raw_input("input the name:")
						d["english"]=int(input("input the english score:"))
						d["python"]=int(input("input the python score:"))
						d["c"]=int(input("input the c score:"))
					except Exception as e:
						print("please reput reply")
					else:
						break
				student=str(d)
				wfile.write(student+"\n")
				print("modify success!")
			else:
				wfile.write(line)
	inputMark=raw_input("continue to  modify student?(y/n):")
        if inputMark == "y":
		modify()

							

def sort():
	show()
	if os.path.exists("student.txt"):
		with open("student.txt","r") as rfile:
			student_old=rfile.readlines()
			student_new=[]
			for line in student_old:
				d=dict(eval(line))
				student_new.append(d)
	else:
		return

	ordermark=input("up is1 and down is 2:")
	if ordermark == 1:
		ascORdescBool=False
	elif ordermark == 2:
		ascORdescBool=True
	else:
		print("the input is invalid!")
		sort()
	mode=input("sort type 1 english 2 python 3 c 0 total:")
	if mode == 1:
		student_new.sort(key=lambda x:x["english"],reverse=ascORdescBool)
	elif mode ==2:
		student_new.sort(key=lambda x:x["python"],reverse=ascORdescBool)
	elif mode == 3:
		student_new.sort(key=lambda x:x["c"],reverse=ascORdescBool)
	elif mode == 0:
		student_new.sort(key=lambda x:x["english"]+x["python"]+x["c"],reverse=ascORdescBool)
	else:
		print("your input is invalid!")
		sort()
	show_student(student_new)

def total():
	if os.path.exists("student.txt"):
		with open("student.txt","r") as rfile:
			student_old=rfile.readlines()
			if student_old:
				print("there are %d students"%len(student_old))
			else:
				print("there is no students")
	else:
		print("no studets files")


def show():
	student_new = []
	if os.path.exists("student.txt"):
		with open("student.txt","r") as rfile:
			student_old=rfile.readlines()
		for line in student_old:
			student_new.append(eval(line))
		if student_new:
			show_student(student_new)
	else:
		print("no data in file")

def show_student(studentlist):
	for line in studentlist:
		print(line.get("id"),line.get("name"),line.get("english"),line.get("python"),line.get("c"),line.get("english")+line.get("python")+line.get("c"))	
#	format_title="%s%s\t%s\t%s\t%s\t%s"
#	print(format_title%("ID","NAME",“ENGLISH”,“PYTHON”,“C”,”TOTAL“))
#	format_data="%s%s\t%s\t%s\t%s\t%s"
#	for info in studentlist:
#		print(str(info,type(info))
#	print(studentlist)

def save(student):
	try:
		student_txt=open("student.txt","a")
	except Exception as e:
		student_txt=open("student.txt","w")
	for info in student:
		student_txt.write(str(info)+"\n")
	student_txt.close()
	


if __name__ == "__main__":
	main()	
