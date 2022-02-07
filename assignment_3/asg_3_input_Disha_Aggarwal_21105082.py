#ASSIGNMENT_3
                                        #QUESTION_1
print("\n                        #question_1")
string=input("enter the string: ") 
string=string.lower()
print(string)
list_1=string.split(" ")
l=len(list_1)
dict={}
#checking whether a single word is entered in input or not
if l>1:
    for x in list_1:
        if(x in dict):
            e=dict.get(x)
            e=e+1
            dict[x]=e
        else:
            dict[x]=1
if(l==1):
    for x in string:
        if(x in dict):
            e=dict.get(x)
            e=e+1
            dict[x]=e
        else:
            dict[x]=1
print(dict)


                                         #QUESTION_2
print("\n                          #question_2")
day=int(input('enter Day: '))
month=int(input('enter Month: '))
year=int(input('enter Year: '))


#Removing all the invalid cases
if day>30 and month in {2,4,6,9,11}:
    condition=False
elif day>31 and month in {1,3,5,7,8,10,12}:
    condition=False
elif (day==29 or day==30) and month==2 and year%4!=0:
    condition=False
elif day==30 and month==2 and year%4==0:
    condition=False
else:
    condition=True

#After checking the condition, following if-else statement is executed
if condition:
    #checking and changing for new year
    if day==31 and month==12:
        n_year=year+1
    else:
        n_year=year
    if month==12 and day==31:
        n_month=1
    else:
        n_month=month
#changing dates
    #checking for months with 31 days
    if month in {1,3,5,7,8,10,12}:
        if day==31:
            next_day=1
            if month!=12:
                n_month=month+1
            else:
                n_month=1
        else:
            next_day=day+1
    #checking for month of february
    elif month==2:
        if year%4==0:
            if day==29:
                next_day=1
                n_month=3
            else:
                next_day=day+1
        else:
            if day==28:
                next_day=1
            else:
                next_day=day+1
                n_month=3
    #covering all remaining cases
    else:
        if day==30:
            next_day=1
            n_month=month+1
        else:
            next_day=day+1
    #printing calculations
    print(f"Next Date is: {next_day}/{n_month}/{n_year}")
else:
    #gives a warning and ends the program
    print("That's not a valid date")



                                   #QUESTION_3
print("\n                      #question_3")
list1=list(map(int,input("Enter the numbers separated by space:").split()))
list2=[]
for x in list1:
    tuple=(x,x**2)
    list2.append(tuple)
print("\nList containing (n,n^2) is :")
print(list2)


                                   #QUESTION_4
print("\n                     #question_4")
grade_point=int(input("Enter your grade points: "))
dict={10:"Your grade is 'A+' and Outstanding performance.",
      9:"Your grade is 'A' and Excellent performance.",
      8:"Your grade is 'B+' and Very Good performance.",
      7:"Your grade is 'B' and Good performance.",
      6:"Your grade is 'C+' and Average performance.",
      5:"Your grade is 'C' and Below Average performance.",
      4:"Your grade is 'D' and Poor performance."}
if 4<=grade_point<=10:
    statement=dict.get(grade_point)
    print(statement)
else:
    print("\nError!\nPlease enter grade in range [4,10]")


                                   #QUESTION_5
print("\n                     #question_5")
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

for row in range(0,6):
    col=0
    counter=0
    while col<11:
        if col<row or col>11-row-1:
            print(" ", end="")
        else:
            print(alphabets[counter], end="")
            counter=counter+1
        col=col+1
    print("")


                                   #QUESTION_6 
print("\n                      #question 6")
condition=True

Dictionary={}
prompt="y"
while condition:
    if prompt.lower()=="y":
        SID=int(input("Enter SID of Student: "))
        name=input("Enter the name of the Student: ")
        Dictionary[SID]=name
        prompt= input("If you want to enter more details press Y/N: ")
        condition = True
    else:
        condition = False

print("(a)")
for key,value in Dictionary.items():
    print(f"{key} is {value}")
print("")

print("(b)")
Value_sort_dict= sorted(Dictionary.values())
print(f"value sorted dictionary is {Value_sort_dict}")
print("")

print("(c)")
Key_sort_dict= sorted(Dictionary.keys())
print(f"Keys sorted dictionary is {Key_sort_dict}")
print("")

print("(d)")
SID_details=int(input("e\Enter SID whose detail you need- "))
if SID_details in Dictionary.keys():
    print(f"Name of the required student is {Dictionary[SID_details]}")
else:
    print("The SID is not present in Data")
print("")


                                   #QUESTION_7
print("\n                      #question_7")
number=int(input("Total elements of Fibonacci sequence that you want(must be greater than 1)- "))

#using the formula : sum of previous two terms is equal to the present term
a_1=1
a_2=0
n=0
#initializing sum with first two terms
sum=a_1+a_2

print(f"Fibonnaci sequence with {number} terms")
print(a_2)
print(a_1)

while n<number-2:
    a_n=a_2+a_1
    a_2=a_1
    a_1=a_n
    print(a_n)
    n=n+1
    sum+=a_n
print(f"Sum of total {number} terms of sequence is {sum}")
print("END")


                                 #QUESTION_8
print("\n                   #question_8")
Set_1= {1, 2, 3, 4, 5}
Set_2= {2, 4, 6, 8}
Set_3= {1, 5, 9, 13, 17}

#Finding symmetric difference of both the sets
print("(a)")
set_not_both=Set_1^Set_2
print(f"set with elements not common in both is {set_not_both}")

#Finding symmetric difference of all sets
print("(b)")
set_only_in_one=Set_1^Set_2^Set_3
print(f"Set of elements that is only present in one set is {set_only_in_one}")

#Finding elements that is common in any two sets
print("(c)")
set_only_in_two=(Set_1|Set_2|Set_3)- (Set_1^Set_2^Set_3)-(Set_1&Set_2&Set_3)
print(f"Set of elements that is only present in two set is {set_only_in_two}")

#Finding elements common in set1 and range 1 to 10
print("(d)")
new_set_1=set()
for n in range(1,11):
    new_set_1.add(n)
not_common_1=new_set_1- Set_1
print(f"set of all integers in the range 1 to 10 that are not in Set_1 {not_common_1}")

#Finding elements common in sets 1,2,3 and range 1 to 10
print("(e)")
new_set_2=set()
for n in range(1,11):
    new_set_2.add(n)
not_common_2=new_set_2 - (Set_1|Set_2|Set_3)
print(f"set of all integers in the range 1 to 10 that are not in Set_1 and Set_2 and Set_3 {not_common_2}")











