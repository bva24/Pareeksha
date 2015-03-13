from django.shortcuts import render
from register.models import *
from register.forms import *
# Create your views here.

def register(request):
	if request.method == 'POST':
		name = str(request.POST.get('name',''))
		reg = Registration()
		reg.save()
	return render(request,'register/register.html',{})
	
	

# Give Form Name for the class
def add_new_student(request):
    
    if request.method == 'POST':
        print('Form submitted')
        student_form = Student_Form(request.POST)
        if student_form.is_valid():
            print('Form is valid');
            student_form.save()
        else:
            print('Invalid request')
            
    student_form2 = Student_Form()   
    return render(request,'register/student.html',{'form':student_form2})

# Need to create Student.html file 
