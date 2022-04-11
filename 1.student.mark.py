def addstudent(name,ID,DoB):
    global addstudent
    print('''Student's Name is:''',name)
    print('''Student ID is:''',ID)
    print('''Student Dob is:''',DoB)
def course():
    global course
    tuple = ("Calculus","Linear Algebra","Biologi","Chemistry","Basic Programming","Physics","French")
    print(tuple)
    f=0
    while f < 7:
        r=tuple[f]
        s= "please enter the mark of"
        s2 ="course:"
        print(s,r,s2)
        s3="The mark for"
        s4="is:"
        mark= float(input())
        print(s3,r,s4,mark)
        f+=1

print("Insert the number of student in class:")
def number():
    global number,i,a
    a=int(input())
    i=0
    print("The number of student in the class is:",a)
    while i < a:
        a1=('Please Enter student')
        a2=('name and then id student and then DoB')      
        print(a1,i+1,a2)
        dic ={'name':input(),'ID':input(),'DoB':input()}
        addstudent(**dic)
        course()
        i+=1
number()      