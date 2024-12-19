from django.db import models

# Create your models here.
class mootcourt_reg(models.Model):
    

    teamname= models.CharField(max_length=200, default="")
    College = models.CharField(max_length=12 , default="")
    member1 = models.CharField(max_length=200, default="")
    email1 = models.CharField( max_length=254 , default="")
    phone1 = models.CharField(max_length=12 , default="")
  
    member2 = models.CharField(max_length=200, default="")
    email2 = models.CharField( max_length=254 , default="")
    phone2 = models.CharField(max_length=12 , default="")
    member3 = models.CharField(max_length=200, default="")
    email3 = models.CharField( max_length=254 , default="")
    phone3 = models.CharField(max_length=12 , default="")
    comments = models.CharField(max_length=12 , default="")


   

    def __str__(self):
        return self.teamname
    
    
class SocioExhibition(models.Model):
    

    schoolname= models.CharField(max_length=200, default="")
    address = models.CharField(max_length=200, default="")
    email = models.CharField( max_length=254 , default="")
    phone = models.CharField(max_length=12 , default="")
    

    City = models.CharField( max_length=50, default = "")
    state= models.CharField( max_length=50, default = "")
    
    # profession = models.CharField( max_length=50, default = "")
    principal = models.CharField( max_length=50, default = "", null=True)
    POC = models.CharField( max_length=50, default = "")

   

    def __str__(self):
        return self.schoolname 
      
class HackathonRegistration(models.Model):
    

   
    teamname= models.CharField(max_length=200, default="")
    member1 = models.CharField(max_length=200, default="")
    email1 = models.CharField( max_length=254 , default="")
    phone1 = models.CharField(max_length=12 , default="")
    address = models.CharField(max_length=12 , default="")
    member2 = models.CharField(max_length=200, default="")
    email2 = models.CharField( max_length=254 , default="")
    phone2 = models.CharField(max_length=12 , default="")
    member3 = models.CharField(max_length=200, default="")
    email3 = models.CharField( max_length=254 , default="")
    phone3 = models.CharField(max_length=12 , default="")
    member4 = models.CharField(max_length=200, default="")
    email4 = models.CharField( max_length=254 , default="")
    phone4 = models.CharField(max_length=12 , default="")
    comments = models.CharField(max_length=12 , default="")
    def __str__(self):
        return self.teamname
    
class CaseStudy(models.Model):
    

    teamname= models.CharField(max_length=200, default="")
    member1 = models.CharField(max_length=200, default="")
    email1 = models.CharField( max_length=254 , default="")
    phone1 = models.CharField(max_length=12 , default="")
    address = models.CharField(max_length=12 , default="")
    member2 = models.CharField(max_length=200, default="")
    email2 = models.CharField( max_length=254 , default="")
    phone2 = models.CharField(max_length=12 , default="")
    member3 = models.CharField(max_length=200, default="")
    email3 = models.CharField( max_length=254 , default="")
    phone3 = models.CharField(max_length=12 , default="")
    comments = models.CharField(max_length=12 , default="")

    

    
   

    def __str__(self):
        return self.teamname 
class PIL_DRAFT(models.Model):
    

    teamname= models.CharField(max_length=200, default="")
    member1 = models.CharField(max_length=200, default="")
    email1 = models.CharField( max_length=254 , default="")
    phone1 = models.CharField(max_length=12 , default="")
    address = models.CharField(max_length=12 , default="")
    member2 = models.CharField(max_length=200, default="")
    email2 = models.CharField( max_length=254 , default="")
    phone2 = models.CharField(max_length=12 , default="")
    member3 = models.CharField(max_length=200, default="")
    email3 = models.CharField( max_length=254 , default="")
    phone3 = models.CharField(max_length=12 , default="")
    comments = models.CharField(max_length=12 , default="")

    

    
   

    def __str__(self):
        return self.teamname  
class union_budget_reg(models.Model):
    

    team_leader_Name= models.CharField(max_length=200, default="")
    College_Name = models.CharField(max_length=200, default="")
    email = models.CharField( max_length=254 , default="")
    phone = models.CharField(max_length=12 , default="")
    

    City = models.CharField( max_length=50, default = "")
    state= models.CharField( max_length=50, default = "")
    
    # profession = models.CharField( max_length=50, default = "")
    # principal = models.CharField( max_length=50, default = "", null=True)
    # POC = models.CharField( max_length=50, default = "")

   

    def __str__(self):
        return self.team_leader_Name
class Socio_trivia_reg(models.Model):
    

    schoolname= models.CharField(max_length=200, default="")
    address = models.CharField(max_length=200, default="")
    email = models.CharField( max_length=254 , default="")
    phone = models.CharField(max_length=12 , default="")
    

    City = models.CharField( max_length=50, default = "")
    state= models.CharField( max_length=50, default = "")
    
    # profession = models.CharField( max_length=50, default = "")
    School_UDISE = models.CharField( max_length=50, default = "", null=True)
    POC = models.CharField( max_length=50, default = "")

   

    def __str__(self):

        return self.schoolname
class mock_parliament_reg(models.Model):
    

    Name= models.CharField(max_length=200, default="")
    College = models.CharField(max_length=200, default="")
    email = models.CharField( max_length=254 , default="")
    phone = models.CharField(max_length=12 , default="")
    

    City = models.CharField( max_length=50, default = "")
    state= models.CharField( max_length=50, default = "")
    
    # profession = models.CharField( max_length=50, default = "")
    # principal = models.CharField( max_length=50, default = "", null=True)
    # POC = models.CharField( max_length=50, default = "")

   

    def __str__(self):
        
        return self.Name
class adhikar_reg(models.Model):
    

    schoolname= models.CharField(max_length=200, default="")
    address = models.CharField(max_length=200, default="")
    email = models.CharField( max_length=254 , default="")
    phone = models.CharField(max_length=12 , default="")
    

    City = models.CharField( max_length=50, default = "")
    state= models.CharField( max_length=50, default = "")
    
    # profession = models.CharField( max_length=50, default = "")
    principal = models.CharField( max_length=50, default = "", null=True)
    POC = models.CharField( max_length=50, default = "")

   

    def __str__(self):
        
        return self.schoolname