print("=====================")
print("STUDENT REPORT CARD")
print("=====================\n\n")

student={
    "Name":"",
    "Age":"",
    "Average":"",
    "Class":""
}

students=[]
classopt=["yellow","red","green"]
subopt=["math", "english", "ict", "art"]


def calc(math,eng,ict,art):
    totalss=int(math+eng+ict+art)
    ave=int(totalss/4)
    return ave

def gradess(ave):
    if (ave>=80):
        grade='A'
        remark="Excellent"
    elif(ave>=70):
        grade='B'
        remark="very good"
    elif(ave>=50):
        grade='C'
        remark="average"
    elif(ave>=40):
        grade='D'
        remark="poor"
    elif(ave<40):
        grade='F'
        remark="very poor"
    return grade,remark

def extra(grades):
    count= 0
    for i in grades:
        if (i>=50):
            count+=1
    return count

def findmax(grades):
    max=grades[0]
    for i in grades:
        if (max<i):
            max=int(i)
    return max


def findmin(grades):
    min=grades[0]
    for i in grades:
        if (min>i):
            min=int(i)
    return min
    
def highest(students):
    maxhigh=0
    for student in students:
        i=student.get("Average")
        if i> maxhigh:
            maxhigh=i
            maxstud=student.get("Name")
    return maxhigh,maxstud

def checksub(sub,subopt):
    sub=sub.lower()
    sub=sub.replace(",","")
    word=sub.split()
    while sorted(word)!=sorted(subopt):
        print("ERROR! The subject that exist is math, english, art, ict\n write the subject\n")
        sub=input("")
        sub=sub.lower()
        sub=sub.replace(",","")
        word=sub.split()



def checkclass(classopt,classs): 
    while True:
            classs=classs.lower()
            x=classs not in classopt 
            if x==True:
             print("ERROR! There is only yellow, red or green\n")
             classs=input("Class:")
             student["Class"]=classs
            else:
                # x=False
                break

while(True):
    
    print("\n  Do you want to add a student?")
    print(" y. add students\n p. display studnets \n h. see the highest student \n n. exit")
    res=input("\ny,n, h or p\n")
    if (res=='y'):
        grades=[]
        student={}
        name=input("Name:")
        student["Name"]=name
        age= input("age:")
        student["Age"]=age

        classs=input("Class:")
        student["Class"]=classs
        checkclass(classopt,classs)
        

        print("write the subject")
        sub=input("\n")
        checksub(sub,subopt)


        math=int(input("Math:"))
        grades.append(math)
        eng=int(input("English:"))
        grades.append(eng)
        ict=int(input("ICT:"))
        grades.append(ict)
        art=int(input("Art:"))
        grades.append(art)

        ave=calc(math,eng,ict,art)
        student["Average"]=ave
        grade,remark=gradess(ave)
        count=extra(grades)
        high=findmax(grades)
        low=findmin(grades)

        print(f"\naverage: {ave}")
        print(f"grade: {grade}")
        print(f"remark: {remark}\n")
        print(f"\nThe higest score is: {high} and lowest is:{low}")
        print(f"The count: {count}")
        students.append(student)

    elif (res=='p'):
        print("=====================")
        print("STUDENT REPORT CARD")
        print("=====================\n")
        for student in students:
            print(f"Name: {student['Name']}")
            print(f"Age: {student['Age']}")
            print(f"Class: {student['Class']}")
            print(f"Average: {student['Average']}")
            print("\n")
        break
    
    elif(res=='h'):
        highe,highstud=highest(students)
        print(f"The highest student is {highstud} with {highe}")

    elif(res=='n'):
        print("Exiting....")
        break

    else:
        print("PLS ENTER YES OR NO")

 


 










#doesnt exit after the wrong one