#assignment_2
                                #QUESTION_1
print("\n                       #question_1")
String="Python is a case sensitive language"
length=len(String)
print("(a) length of string :",length)
reversed_string= (String)[::-1]
print("(b) reversed string :",reversed_string)
print("(c) new string :", String[10:26] )
after_replacing= String.replace("a case sensitive","object oriented")
print("(d) after replacing :",after_replacing)
index= String.find("a")
print("(e) index of a :",index)
remove_white_spaces= String.replace(" ","")
print("(f) after removing white spaces :",remove_white_spaces)

                                #QUESTION_2
print("\n                       #question_2")
name= input("what is your name : ")
sid= int(input("your SID : "))
dept_name= input("department name : ")
cgpa= float(input("your CGPA : "))
print("\nHey, %s Here!\nMy SID is %d \nI am from %s department and my CGPA is %f"%(name,sid,dept_name,cgpa))

                               #QUESTION_3
print("\n                      #question_3")
a=56
b=10
print("(a) a&b :",a&b)
print("(b) a|b :",a|b)
print("(c) a^b :",a^b)
print("(d) Left shift a with 2 bits :",a<<2)
print("    Left shift b with 2 bits :",b<<2)
print("(e) Right shift a with 2 bits :",a>>2)
print("    Right shift b with 4 bits :",b>>4)

                               #QUESTION_4
print("\n                      #question_4")
first_number= int(input("enter first number : "))
second_number= int(input("enter second number : "))
third_number= int(input("enter third number : "))
if first_number>second_number:
    if first_number>third_number:
      print("\nthe greatest no is :",first_number)
    else:
      print("\nthe greatest no is :",third_number)
else:
    if second_number>third_number:
      print("\nthe greastest no is :",second_number)
    else:
      print("\nthe greatest no is :",third_number)

                               #QUESTION_5
print("\n                      #question_5")
string= input("enter string : ")
if "name" in string :
    print("\nyes")
else:
    print("\nno")

                               #QUESTION_6
print("\n                      #question_6")
side_1= int(input("enter length of first side : "))
side_2= int(input("enter length of second side : "))                          
side_3= int(input("enter length of third side : "))
if (side_1+side_2>side_3) and (side_2+side_3>side_1) and (side_1+side_3>side_2) :
     print("\nyes")
else:
     print("\nno")    

