from excel.export_to_excel import excel
from avro.export_to_avro import avro

opt,no_of_records = 0,0
col_choices = []
#asking for filetype and no of records
def ask_filetype():
	while True:
		try:
			global no_of_records
			no_of_records=int(input("Enter the number of records you want"))
			global opt
			opt = int(input("Please choose the type of file\n1.Excel\n2.avro\nplease enter your option number"))
			if opt in [1,2]:
				break
			else:
				continue
		except:
			print("That was not correct choice. Please enter again.")


#asking for requirements of sample data
def ask_details():
	while True:
	    try:
		    choice=int(input("Please enter the number of columns U want to generate"))
		    break  
	    except:
	    	print("Please enter the number")
	    	continue
	    finally:
	    	global col_choices
	    	boolean = True
	    	while boolean:
		    	for i in range(0,choice):
		    		print("Please choose the data type for column ",i,"\nAvailable data types are \n1.Integer\n2.String\n3.float\n4.Boolean")
		    		ind_choice=int(input())
		    		if ind_choice not in [1,2,3,4]:
		    			print("Choose only the listed datatypes")
		    			continue
		    		else:
		    			if i==choice-1:
		    				boolean=False
		    				col_choices.append(ind_choice)
		    			else:
		    				col_choices.append(ind_choice)
	    	break

ask_filetype()
ask_details()
if opt==1:
	xl = excel()
	xl.export_excel(col_choices,no_of_records)
elif opt==2:
	av = avro()
	av.export_avro(1,col_choices,no_of_records)
