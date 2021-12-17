import time
today = time.strftime("%m:%d:%Y %H:%M:%S")
with open('PROG1783 Final Exam/PROG1783File2.txt', 'r') as file:
    filedata = file.read()
filedata = filedata.replace('Sukhmanpreet', '********')

with open('PROG1783 Final Exam/PROG1783File2.txt', 'w') as file:
    file.write(filedata)
    file.write(today)
with open('PROG1783 Final Exam/PROG1783File2.txt', 'r') as file:
    filedata = file.read()
    print(filedata)
