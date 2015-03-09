from django.db import models

# Create your models here.

###########################


#Gotra Model
class Gotra(models.Model):
    Gotra_Name  =   models.CharField(max_length =   50,null=True, blank=True)
    
    def __unicode__(self):
        return self.Gotra_Name
        
        
#Sutra Model
class Sutra(models.Model):
    Sutra_Name  =   models.CharField(max_length =   50,null=True, blank=True)
    
    def __unicode__(self):
        return self.Sutra_Name       
        

#Nakshatra Model
class Nakshatra(models.Model):
    Nakshatra_Name  =   models.CharField(max_length =   50,null=True, blank=True)
    
    def __unicode__(self):
        return self.Nakshatra_Name  
        

        
#Veda and Shakha Combined Model
class Veda_Shakha(models.Model):
    Veda_Shakha_Name  =   models.CharField(max_length =   200,null=True, blank=True)
    
    def __unicode__(self):
        return self.Veda_Shakha_Name
        
#Exam Name Model
class Exam(models.Model):
    Exam_Name  =   models.CharField(max_length =   100,null=True, blank=True)
    
    def __unicode__(self):
        return self.Exam_Name


#Exam-Name Short Form Model
class ShortExamName(models.Model):
    Exam_Short_Name  =   models.CharField(max_length =   10,null=True, blank=True)
    
    def __unicode__(self):
        return self.Exam_Short_Name 
        
        
#Kramaha() Model
class Kramaha(models.Model):
    Kramaha_Indicator  =   models.CharField(max_length=2, null=True, blank=True)
    
    def __unicode__(self):
        return self.Kramaha_Indicator
        
        
#Stharaha() Model
class Stharaha(models.Model):
    Stharaha_Indicator  =   models.CharField(max_length=2, null=True, blank=True)
    
    def __unicode__(self):
        return self.Stharaha_Indicator


#Number of Question() Model
class TotalQuestion(models.Model):
    Num_of_Questions  =   models.CharField(max_length=5, null=True, blank=True)
    
    def __unicode__(self):
        return self.Num_of_Questions


#Sambhavana() Model
class Sambhavana(models.Model):
    Sambhavana  =   models.IntegerField(max_length=10, null=False, blank=False)
    
    def __unicode__(self):
        return self.Sambhavana



#Special_Prathama_Sambhavana() Model
class SpecialPrathamaSambhavana(models.Model):
    Special_Prathama_Sambhavana  =   models.IntegerField(max_length=10, null=False, blank=False)
    
    def __unicode__(self):
        return self.Special_Prathama_Sambhavana
        
        
#Special_Uttama_Sambhavana() Model
class Special_Uttama_Sambhavana(models.Model):
    Special_Prathama_Sambhavana  =   models.IntegerField(max_length=10, null=False, blank=False)
    
    def __unicode__(self):
        return self.Special_Uttama_Sambhavana


#Place Model
class Place(models.Model):
    Place_Name  =   models.CharField(max_length =   80,null=True, blank=True)
    
    def __unicode__(self):
        return self.Place_Name 
        
        
#District Model
class District(models.Model):
    District_Name  =   models.CharField(max_length =   80,null=True, blank=True)
    
    def __unicode__(self):
        return self.District_Name    
        
        
#State Model
class State(models.Model):
    State_Name  =   models.CharField(max_length =   50,null=True, blank=True)
    
    def __unicode__(self):
        return self.State_Name       
        
        
#Country Model
class Country(models.Model):
    Country_Name  =   models.CharField(max_length =   50,null=True, blank=True)
    
    def __unicode__(self):
        return self.Country_Name    
        
        
#Category Model
class Category(models.Model):
    Pandit_Category_Name  =   models.CharField(max_length =   50,null=True, blank=True)
    
    def __unicode__(self):
        return self.Pandit_Category_Name    
        
        

#Pathashala Model
class Pathashala(models.Model):
    Pathashala_Name  =   models.CharField(max_length =   100,null=True, blank=True)
    Address         =   models.TextField(blank=False)
    Place           =   models.ForeignKey(Place,null=True, blank=True)
    District        =   models.ForeignKey(District,null=True, blank=True)
    Pincode         =   models.IntegerField(max_length =  10,null=True, blank=True)
    State           =   models.ForeignKey(State,null=True, blank=True)
    Country         =   models.ForeignKey(Country,null=True, blank=True)
    LandLine_Num    =   models.IntegerField(max_length =  12,null=True, blank=True)
    Mobile_Num      =   models.IntegerField(max_length =  10,null=True, blank=True)
    
    def __unicode__(self):
        return self.Pathashala_Name 
        
        


#Vidwan Model
class Guru(models.Model):
    Guru_Id   = models.CharField(max_length=10, null=False, blank=False)
    Guru_Name   = models.CharField(max_length   =   100)
    Category         =  models.ForeignKey(Category)
    Age  =   models.IntegerField(max_length=3, null=True, blank=True)
    Serving_Patashala   = models.ForeignKey(Pathashala,null=True, blank=True)
    Guru_Address       =   models.TextField(blank=False)
    Place           =   models.ForeignKey(Place,null=True, blank=True)
    District        =   models.ForeignKey(District,null=True, blank=True)
    Pincode         =   models.IntegerField(max_length =  10,null=True, blank=True)
    State           =   models.ForeignKey(State,null=True, blank=True)
    Country         =   models.ForeignKey(Country,null=True, blank=True)
    LandLine_Num    =   models.IntegerField(max_length =  12,null=True, blank=True)
    Mobile_Num      =   models.IntegerField(max_length =  10,null=True, blank=True)
    def __unicode__(self):
        return self.Guru_Name
        
        



#Student - Present - Details Model
class Student(models.Model):    
    Student_ID  =   models.CharField(max_length=10, null=False, blank=False)
    Student_Name   = models.CharField(max_length   =   100)
    Father_Name =   models.CharField(max_length   =   100,null=True, blank=True)
    Date_of_Birth  = models.DateField()
    Age  =   models.IntegerField(max_length=3, null=True, blank=True)
    Patashala_Name_If_Applicable   = models.ForeignKey(Pathashala,null=True, blank=True)
    Guru_Details    =   models.ForeignKey(Guru)
    Veda_Shakha     =   models.ForeignKey(Veda_Shakha)
    Exam_Short_Name =   models.ForeignKey(ShortExamName)
    Kramaha         =   models.ForeignKey(Kramaha)
    Stharaha        =   models.ForeignKey(Stharaha)
    TotalQuestions  =   models.ForeignKey(TotalQuestion)
    Permanent_Address          =   models.TextField(blank=False)
    Present_Address          =   models.TextField(blank=False)
    Place           =   models.ForeignKey(Place,null=True, blank=True)
    District        =   models.ForeignKey(District,null=True, blank=True)
    Pincode         =   models.IntegerField(max_length =  10,null=True, blank=True)
    State           =   models.ForeignKey(State,null=True, blank=True)
    Country         =   models.ForeignKey(Country,null=True, blank=True)
    LandLine_Num    =   models.IntegerField(max_length =  12,null=True, blank=True)
    Mobile_Num      =   models.IntegerField(max_length =  10,null=True, blank=True)
    
    def __unicode__(self):
        return self.Student_Name            
