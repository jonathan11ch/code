#Import pandas lib as pd
import pandas as pd
import numpy as np

#Function to read files

def reading_files():

	name_file1 = '1MC03-SCJ-IM-REP-SS01_SL03-242400_P07_Data.xlsx'
	name_file2 = '1MC03-SCJ-IM-REP-SS01_SL03-242400_P08_Data.xlsx'

	all_dfs1 = pd.read_excel(name_file1, sheet_name = None)
	all_dfs2 = pd.read_excel(name_file2, sheet_name = None)

	#Converting into one tab 

	all_dfs1.keys()
	all_dfs2.keys()

	df_1 = pd.concat(all_dfs1, ignore_index = True)
	df_2= pd.concat(all_dfs2, ignore_index = True)


	# Adding 'row_from_file' and 'Identify GUI'


	df_1['Row_from_file'] = '1MC03-SCJ-IM-REP-SS01_SL03-242400_P07_Data.xlsx'
	df_2['Row_from_file' ]= '1MC03-SCJ-IM-REP-SS01_SL03-242400_P08_Data.xlsx'

	df_1.insert(1, 'test','')
	df_1['Identify GUID'] = 'old'
	df_2.insert(1, 'test','')
	df_2['Identify GUID'] = 'new'


	# Combining the files (new and old) into one


	excel_merged = df_1.concat(df_2)
	writer = pd.ExcelWriter('Comparison.xlsx', engine='xlsxwriter')
	excel_merged.to_excel(writer)

	#Writing the fil1
	file1 = pd.ExcelWriter(name_file1, engine='xlsxwriter')
	df_1.to_excel(file1)

	file2 = pd.ExcelWriter(name_file2, engine='xlsxwriter')
	df_2.to_excel(file2)

	file1.save()
	file2.save()
	writer.save()


# Comparing GUID column and using tags to identify same/new/old

def same_GUID():

	comparison_file = 'Comparison.xlsx'
	info = pd.read_excel(comparison_file, header = 0)
	info.loc[info['GUID'].duplicated(keep=False), 'Identify GUID' ] = 'same'
	info.drop('Unnamed: 0', axis=1, inplace=True)
	mask = info.style.applymap(highlight_rows, axis=0)
	print(mask)
	writer_1 = pd.ExcelWriter('Comparison.xlsx', engine='xlsxwriter')
	info.to_excel(writer_1)
	writer_1.save()
	








def highlight_rows(s):

	con = s.copy()
	con[:] = None
	if (s['Identify GUID'] == 'same'):
		con[:] = "background-color: green"

	return con
        



	'''

	duplicated = info[info['GUID'].duplicated(keep=False)]
	print(duplicated)

	a = duplicated.groupby('GUID').apply(lambda x: list(x.index))

	for m in range (len(a)):

		row_a = info.loc[a[m][0]]
		row_b = info.loc[a[m][1]]

		condition = row_a.eq(row_b)

		print(condition)
	'''


 
a = reading_files()
b = same_GUID()