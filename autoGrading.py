import os
import subprocess
import inspect
import xlsxwriter

# Get every files in this folder
path_dir = '.'
file_list = os.listdir(path_dir)
file_list.sort()

# CurrentFile name
currentFile = inspect.getfile( inspect.currentframe() )

# var: ans
# desc: the answer what we want.
f = open('answer.txt', 'r')
ans = f.read()
f.close()

# var: resultList
# desc: saves the result of all files.
resultList = []

count = 0
for file_name in file_list:
    if '.py' in file_name and file_name != currentFile:
        cmd = 'python3 '+ file_name +' < input.txt'

        # execute submitted python file and get the output
        subProc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        output, err = subProc.communicate()
        result = output.decode('utf-8')
        check = '';

        print('#'+str(count)+' '+ file_name +':', end='')
        if result == ans :
            check = "correct"
        else :
            check = "wrong"
        print(check)

        resultList.append([file_name[3:].replace('.py', ''), check])

# Make a Excel file for result.
workbook = xlsxwriter.Workbook('grade.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0

for studentId, check in resultList:
    worksheet.write(row, col, row)
    worksheet.write(row, col+1, studentId)
    worksheet.write(row, col+2, check)
    row += 1

workbook.close()
