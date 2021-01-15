import pandas as pd
import random,xlsxwriter,string,os
class excel():
	def __init__(self,col=0,writer=pd.ExcelWriter(os.getcwd()+"\\output_file.xlsx",engine='xlsxwriter')):
		self.col=col
		self.writer=writer
	def export_excel(self,col_choices,no_of_records):
		try:
			for i in range(0,len(col_choices)):
				if col_choices[i]==1:
					df1 = pd.DataFrame({f'col{self.col+1}': random.sample(range(0,no_of_records),no_of_records)})
					df1.to_excel(self.writer,sheet_name="Sheet1",index=False,startcol=self.col)
					self.col+=1
				if col_choices[i]==2:
					df2 = pd.DataFrame({f'col{self.col+1}':[(''.join(random.choice(string.ascii_lowercase) for i in range(10))) for ele in range(0,no_of_records)]})
					df2.to_excel(self.writer,sheet_name="Sheet1",index=False,startcol=self.col)
					self.col+=1
				if col_choices[i]==3:
					df3 = pd.DataFrame({f'col{self.col+1}':[random.uniform(0,no_of_records) for ele in range(0,no_of_records)]})
					df3.to_excel(self.writer,sheet_name="Sheet1",index=False,startcol=self.col)
					self.col+=1
				if col_choices[i]==4:
					df4 = pd.DataFrame({f'col{self.col+1}':[True if random.choice([0,1])==1 else False for ele in range(0,no_of_records)]})
					df4.to_excel(self.writer,sheet_name="Sheet1",index=False,startcol=self.col)
					self.col+=1
		except Exception as e:
			print(e)
		self.writer.save()
		print("--------------------------------------------------")
		print("Exported to Excel.Please Check your current folder")
		print("--------------------------------------------------")