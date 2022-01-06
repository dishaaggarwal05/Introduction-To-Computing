#assignment_1
                                 #QUESTION_1
print("                           #question_1")
numb1=int(input("enter first number: "))
numb2=int(input("enter second number: "))
numb3=int(input("enter third number: "))
avg=(numb1+numb2+numb3)/3
print("average of three numbers= ",avg)

                                 #QUESTION_2
print("\n                           #question_2")
tax_rate=0.2
standard_deduction=10000
dependent_deduction=3000
gross_income=int(input("gross income: "))
no_of_dependents=int(input("no of dependents: "))
taxable_income=gross_income-standard_deduction-(dependent_deduction*no_of_dependents)
tax=taxable_income*tax_rate
print("Taxable Income: ",taxable_income)
print("Tax: ",tax)

                                 #QUESTION_3
print("\n                           #question_3")
print("Student:[SID, Name, Gender, Course Name, CGPA]")
student=[21105082, 'Disha_Aggarwal', 'F', 'ECE', 9.3]
print("Student:",student)

                                 #QUESTION_4
print("\n                           #question_4")
Marks=[23,43,44,34,39]
print("list of marks before sort: ",Marks)
Marks.sort()
print("list of marks after sort",Marks)

                                 #QUESTION_5
print("\n                           #question_5")
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color.pop(3)
print("(a) after removing: ",color)
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color[3:5]=['Purple']
print("(b) after replacing: ",color)
