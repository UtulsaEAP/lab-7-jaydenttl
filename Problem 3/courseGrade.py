'''
Name: Jayden Ly
Lab Time: 2:40
input: ./Problem 3/StudentInfo.tsv
'''
def letterGrades(studentavg):
    grade = ''
    if  studentavg >= 90:
        grade = 'A'
        return grade
    elif studentavg >= 80:
        grade = 'B'
        return grade
    elif studentavg >= 70:
        grade = 'C'
        return grade
    elif studentavg >= 60: 
        grade = 'D'
        return grade
    else:
        grade = 'F'
        return grade

def courseGrade():
    file_name = input()
    # TODO: Declare any necessary variables here. 
    avg = ''
    new_string = file_name.replace("StudentInfo", "report")
    nwrite_name = new_string.replace("tsv", "txt")
    # TODO: Read a file name from the user and read the tsv file here. 
    
    file = open(file_name, 'r')
    writefile = open(nwrite_name, "w")
    data = file.readlines()


    student_info = [str(num) for num in data ]
    #print(data)
    #print(student_info[0])
    # TODO: Compute student grades and exam averages, then output results to a text file here. 
    #for i in range(len(data)):
        #split n then t
    mid1list = []
    mid2list = []
    mid3list = []
    #LetterList = []
    
    for num in range(len(data)):
        stripped = student_info[num].strip('\t')
        stripped = stripped.split()
        studentavg = (int(stripped[2]) + int(stripped[3]) + int(stripped[4])) / 3
        mid1list.insert(1,int(stripped[2]))
        mid2list.insert(1,int(stripped[3]))
        mid3list.insert(1,int(stripped[4]))
        
        writefile.write(str(stripped[0])+'\t'+ str(stripped[1]) +'\t'+ str(stripped[2]) +'\t'+str(stripped[3]) +'\t'+str(stripped[4]) +'\t'+str(letterGrades(studentavg))+'\n')

        #LetterList.insert(1, letterGrades(studentavg))

    mid1avg = "%.2f" % (sum(mid1list) / len(mid1list))
    mid2avg = "%.2f" % (sum(mid2list) / len(mid2list))
    mid3avg = "%.2f" % (sum(mid3list) / len(mid3list))
    writefile.write('Averages: midterm1 ' + str(mid1avg)+', midterm2 '+str(mid2avg)+', final '+str(mid3avg))
    #Averages: midterm1 78.80, midterm2 68.47, final 64.20
        
    return

if __name__ == "__main__":
    courseGrade()
    
    