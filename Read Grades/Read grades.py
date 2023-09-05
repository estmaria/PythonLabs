#Author:Maria Esteban
#Date:11/30/2022
#Purpose:read student's information froma file and evaluate the in a different one

#open, read and close the file
file_name=input('File name:')
file = open(file_name)
content = file.read()
file.close()
output = open('report.txt', 'w') #create a file to write on

data=content.split()#separates each iten of the table
num_students=len(data)// 5#counts how many students are in the table
#divides the data in each student
student1=data[0:5]
student2=data[5:10]
student3=data[10:15]
student4=data[15:20]
student5=data[20:25]
student6=data[25:30]
student7=data[30:35]
student8=data[35:40]
student9=data[40:45]
student10=data[45:50]
student11=data[50:55]
student12=data[55:60]
student13=data[60:65]
student14=data[65:70]
student15=data[70:75]
student16=data[75:80]
student17=data[80:85]
student18=data[85:90]
student19=data[95:100]
student20=data[100:105]

def grade(student):
#parameter-a list with the scores of the=exams of a student
#returns-a letter based on the average on those exams
    letter=''
    #if the student does not exist it just put zeros and it would not have any letter
    if len(student)==0:
        student.extend([0,0,0])
        avg=(int(student[-1])+int(student[-2])+int(student[-3]))/3
        if avg >= 90:
            letter='A'
        elif avg>=80:
            letter='B'
        elif avg>=70:
            letter='C'
        elif avg>=60:
            letter='D'
        elif avg>0:
            letter='F'
        else:
            letter=''
    return letter
#put in a list all the different lists with the information anout individual student
student_list=[student1,student2,student3,student4,student5,student6,student7,student8,student9,
    student10,student11,student12,student13,student14,student15,student16,student17,student18,student19,student20]

def exam_averages(exam_number):
#parameter-exam_number indicates what score has to be taken into account
#returns-average of all students in a particular exam
    i=0
    list_ex=[]
    #puts the score of all students in a list
    #Here I don't know why it only took one digit at a time instead of the whole number
    while i<num_students:
        list_ex+=(student_list[i][exam_number+1])
        i+=1
    #puts a bunch of zeros sos it does't give error when later we slice the string
    while len(list_ex)<=40:
        list_ex.append('0')
    #puts all the numbers in the list on a string
    s=''
    for i in list_ex:
        s+=i
    #slices the strings and converts the numbers into integers
    #also add them togetehr to calculate the average
    ex1=int(s[0:2])+int(s[2:4])+int(s[4:6])+int(s[6:8])+int(s[8:10])+int(s[10:12])+int(s[12:14])+int(s[14:16])+int(s[16:18])
    return ex1/num_students

#rounds the averages two decimals
exam1=round(exam_averages(1),2)
exam2=round(exam_averages(2),2)
exam3=round(exam_averages(3),2)

def rows(num_row):
    if len(student_list[num_row-1])==0: #if the student doesn't exist just puts spaces so it doesn't give error
           student_list[num_row-1].extend(['','','','',''])
    #puts the info of teh students
    row=student_list[num_row-1][0]+' '+student_list[num_row-1][1]+' '+student_list[num_row-1][2]+' '+student_list[num_row-1][3]+' '+student_list[num_row-1][4]
    return row
#adds the grades to the student's info
row1=rows(1)+' '+grade(student1)+'\n'
row2=rows(2)+' '+grade(student2)+'\n'
row3=rows(3)+' '+grade(student3)+'\n'
row4=rows(4)+' '+grade(student4)+'\n'
row5=rows(5)+' '+grade(student5)+'\n'
row6=rows(6)+' '+grade(student6)+'\n'
row7=rows(7)+' '+grade(student7)+'\n'
row8=rows(8)+' '+grade(student8)+'\n'
row9=rows(9)+' '+grade(student9)+'\n'
row10=rows(10)+' '+grade(student10)+'\n'
row11=rows(11)+' '+grade(student11)+'\n'
row12=rows(12)+' '+grade(student12)+'\n'
row13=rows(13)+' '+grade(student13)+'\n'
row14=rows(14)+' '+grade(student14)+'\n'
row15=rows(15)+' '+grade(student15)+'\n'
row16=rows(16)+' '+grade(student16)+'\n'
row17=rows(17)+' '+grade(student17)+'\n'
row18=rows(18)+' '+grade(student18)+'\n'
row19=rows(19)+' '+grade(student19)+'\n'
row20=rows(20)+' '+grade(student20)
#write everything in the new file and close it
text2='Averages: midterm1 '+str(exam1)+', midterm2 '+str(exam2)+', final '+str(exam3)+'\n'
text1=row1+row2+row3+row4+row5+row6+row7+row8+row9+row10+row11+row12+row13+row14+row15+row16+row17+row18+row19+row20
output.write(text2)
output.write(text1)
output.close()
