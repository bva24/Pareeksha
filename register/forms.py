from django.forms import ModelForm
from register.models import *
####

# Define Forms for each of the models which are suppose to be displayed

# Student Model Form  -> Form name == Model name 

class Student_Form(ModelForm):
    class Meta:
        model = Student
        fields = ['Student_ID',
                  'Student_Name',
                  'Father_Name',
                  'Date_of_Birth',
                  'Age',
                  'Patashala_Name_If_Applicable',
                  'Guru_Details',
                  'Veda_Shakha',
                  'Exam_Short_Name',
                  'Kramaha',
                  'Stharaha',
                  'TotalQuestions',
                  'Permanent_Address',
                  'Present_Address',
                  'Place',
                  'District',
                  'Pincode',
                  'State',
                  'Country',
                  'LandLine_Num',
                  'Mobile_Num']
                  
                  
                  
        
