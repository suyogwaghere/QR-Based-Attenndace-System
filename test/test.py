import xlsxwriter
filename = "output/suyog.xlsx"
# f = open(filename, 'w')
# f.write("Name"+'\t')
# f.write("Class & batch"+'\t')
# f.write("Year"+'\t')
# f.write("Lecture"+'\t')
# f.write("In Time"+'\n')
# print('suyog')
# f.close


# import xlsxwriter module

# Workbook() takes one, non-optional, argument
# which is the filename that we want to create.
f = xlsxwriter.Workbook(filename)

# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
fob = f.add_worksheet()

# Use the worksheet object to write
# data via the write() method.
fob.write('A1', 'Name')
fob.write('B1', 'Class & batch')
fob.write('C1', 'Year')
fob.write('D1', 'Lecture')
fob.write('E1', 'In Time')
# fob.write(1,0, 'suyog')
# fob.write(1,1, 'AIML-B')
# fob.write(1,2, '4')
# fob.write(1,3, '2')
# fob.write(1,4, '12PM')
my_list = ['suyog', 'AIML-B',
           '4', '2', '12PM']
# my_list = [z, branch.get()+'-'+batch.get(), year.get(), lecture.get(), intime]
for col_num, data in enumerate(my_list):
    fob.write(1, col_num, data)
my_lis = ['depak', 'AIML-B',
           '2', '5', '2PM']
# my_list = [z, branch.get()+'-'+batch.get(), year.get(), lecture.get(), intime]
for col_num, data in enumerate(my_lis):
    fob.write(2, col_num, data)

def enterData(z):
            if z in names:
                pass
            else:
                it = datetime.now()
                names.append(z)
                #z=''.join(str(z))
                roww = 1
                z = (z.decode('utf-8'))
                intime = it.strftime("%I:%M %p")
                my_list = ['suyog', 'AIML-B', '4', '2', '12PM']
                # my_list = [z, branch.get()+'-'+batch.get(), year.get(), lecture.get(), intime]
                for col_num, data in enumerate(my_list):
                    worksheet.write(roww, col_num, data)
                roww += 1
                # fob.write(1, 0, z)
                # fob.write(1, 1, branch.get()+'-'+batch.get())
                # fob.write(1, 2, year.get())
                # fob.write(1, 3, lecture.get())
                # fob.write(1, 4, intime)
                # fob.write(z+'\t'+branch.get()+'-'+batch.get() +'\t'+year.get()+'\t'+lecture.get()+'\t'+intime+'\n')
            return names

# worksheet.write("Name"+'\t')
# worksheet.write("Class & batch"+'\t')
# worksheet.write("Year"+'\t')
# worksheet.write("Lecture"+'\t')
# worksheet.write("In Time"+'\n')
# Finally, close the Excel file
# via the close() method.
f.close()
print('smart generated')
