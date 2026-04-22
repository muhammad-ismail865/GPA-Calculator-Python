courses=["pf","pf_lab","dld","dld_lab","Ew","cal","FA"]
credit_hour=[3,1,2,1,3,3,3]
i=0
total=0
while i<len(courses):
    courses[i]=int(input(f"Enter the number of {courses[i]}:"))
    if(courses[i]>=80 and courses[i]<=100):
        gpa=4
    elif(courses[i]>=75 and courses[i]<=79):
        gpa=3.5
    elif(courses[i]>=70 and courses[i]<=74):
        gpa=3
    elif(courses[i]>=65 and courses[i]<=69):
        gpa=2.5
    elif(courses[i]>=60 and courses[i]<=64):
        gpa=2
    elif(courses[i]>=55 and courses[i]<=59):
        gpa=1.5
    elif(courses[i]>=50 and courses[i]<=54):
        gpa=1
    elif(courses[i]<50 and courses[i]>=0):
        gpa=0
    else:
        print("Please enter a valid number for this course")
    total+=gpa*credit_hour[i]
    i+=1
t_credit=sum(credit_hour)
gpa=total/t_credit
print(f"Your gpa is {gpa}")