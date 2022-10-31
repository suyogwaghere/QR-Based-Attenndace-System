import os
import xlsxwriter

counter = 0
d = "suyog"
q = "attendance/"
filename = (d)

if (os.path.exists(filename+".") == False):
    print("\nThe file name is in if: "+filename)
    print(os.path.exists(filename+".") == False)
    filename = (filename)

else:
    while (os.path.exists(filename+"("+str(counter+1)+")"+".") == True):
        counter += 1
    print("\nThe file name is in else: "+filename)
    filename = (filename+"("+str(counter+1)+")")

print("\nThe file name is : "+filename)
p = "attendance/test.txt"
os.makedirs(os.path.dirname(p), exist_ok=True)
f = xlsxwriter.Workbook(filename+'.xlsx')
fob = f.add_worksheet()
fob.write('A1', 'Name')
fob.write('B1', 'Class & batch')
fob.write('C1', 'Year')
fob.write('D1', 'Lecture')
fob.write('E1', 'In Time')
print("file created")
f.close()
