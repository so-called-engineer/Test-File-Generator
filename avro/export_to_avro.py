import random,string,os
from fastavro import writer,reader,parse_schema
class avro():
	def __init__(self):
		pass
	def export_avro(self,col,col_choices,no_of_records):
		samp=[]
		for i in range(0,len(col_choices)):
			if col_choices[i]==1:
				samp.append({'name': f'col{col}', 'type': 'int'})
				col+=1
			if col_choices[i]==2:
				samp.append({'name': f'col{col}', 'type': 'string'})
				col+=1
			if col_choices[i]==3:
				samp.append({'name': f'col{col}', 'type': 'float'})
				col+=1
			if col_choices[i]==4:
				samp.append({'name': f'col{col}', 'type': 'boolean'})
				col+=1
		schema = {
			'doc':'A sample avro file',
			'name':'sample data',
			'namespace':'test',
			'type':'record',
			'fields':samp,
		}
		parsed_schema=parse_schema(schema)
		lis=[]
		for i in range(0,no_of_records):
			dictionary = {}
			col=1
			for ele in samp:
				if ele['type']=="int":
					dictionary[f'col{col}']=random.randint(0,no_of_records)
					col+=1
				if ele['type']=="string":
					dictionary[f'col{col}']=''.join(random.choice(string.ascii_lowercase) for i in range(10))
					col+=1
				if ele['type']=="float":
					dictionary[f'col{col}']=random.uniform(0,no_of_records)
					col+=1
				if ele['type']=="boolean":
					dictionary[f'col{col}']=random.choice([0,1])
					col+=1
			lis.append(dictionary)
		with open(os.getcwd()+"\\output_file.avro",'wb') as out:
			writer(out,parsed_schema,lis)
		print("-------------------------------------------------")
		print("Exported to avro.Please Check your current folder")
		print("-------------------------------------------------")