#!C:/Users/Ganeshk/AppData/Local/Programs/Python/Python310/Python.exe

import cgi,cgitb
form=cgi.FieldStorage()


Fname = form.getvalue("fname")
Lname = form.getvalue("lname")
Dob= form.getvalue("dob")
address= form.getvalue("Address")
Email_ID=form.getvalue("Email_Id")
Mobile_No=form.getvalue("Mobile_Number")
Pin_Code=form.getvalue("Pin_Code")
State=form.getvalue("State")
# for dropdown
if form.getvalue("country"):
   subject1=form.getvalue("country")
else:
   subject1=form.getvalue("country")

# for checkbox
if form.getvalue('Hobby_Drawing'):
   Drawing_flag = "ON"
else:
   Drawing_flag = "OFF"

if form.getvalue('Hobby_Singing'):
   Singing_flag = "ON"
else:
   Singing_flag  = "OFF"

if form.getvalue('Hobby_Dancing'):
   Dancing_flag = "ON"
else:
   Dancing_flag  = "OFF"

if form.getvalue('Hobby_Cooking'):
   Cooking_flag = "ON"
else:
   Cooking_flag = "OFF"


if form.getvalue('Hobby_Other'):
   Other_flag = "ON"
else:
   Other_flag = "OFF"

Other_hobby=form.getvalue("Other_Hobby")

#for gender
if form.getvalue('subject'):
   subject = form.getvalue('subject')
else:
   subject = "Not set"


print("Content-type:text/html\n\r\n\r")
print("<html>")
print("<body>")
print("<form>")

print("<h2>First Name : %s</h2>" % Fname)
print("<h2> Last Name : %s</h2>" % Lname)
print("<h2> Date of Birth :%s</h2>" % Dob)
print("<h2> Gender :%s</h2>" % subject)
print("<h2> Address : %s</h2>" % address)
print("<h2> Email Id%s</h2>" % Email_ID)
print("<h2> Mobile No : %s</h2>" % Mobile_No)

print("<h2> Pin Code : %s</h2>" % Pin_Code)
print("<h2> State : %s</h2>" % State)
print("<h2> Country : %s</h2>" % subject1)

print("<h2> CheckBox Drawing is : %s</h2>" % Drawing_flag)
print("<h2> CheckBox Singing is : %s</h2>" % Singing_flag)
print("<h2> CheckBox Dancing is : %s</h2>" % Dancing_flag)
print("<h2> CheckBox Cooking is : %s</h2>" % Cooking_flag)
print("<h2> CheckBox other is : %s %s</h2>" % (Other_flag,Other_hobby))



print("</form>")
print("</body>")
print("</html>")
