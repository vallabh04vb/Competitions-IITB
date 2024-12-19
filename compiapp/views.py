from django.shortcuts import render, HttpResponse
from compiapp.models import Socio_trivia_reg, SocioExhibition,HackathonRegistration,CaseStudy,PIL_DRAFT, union_budget_reg,mootcourt_reg,mock_parliament_reg,adhikar_reg
from django.conf import settings  
from django.core.mail import send_mail, EmailMessage, get_connection  
# from django.core import mail
from django.contrib import messages
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# from django.core.mail import EmailMessage


# Create your views here.

def index(request):
    return render(request, "index.html")

# def competitions_view(request):
#     return render(request, "index.html/#")

def SocioTrivia(request):
    return render(request, "SocioQuiz.html")

def SocialExhibition(request):
    return render(request, "SocioExhibition.html")
def Triviareg(request):
    return render(request, "Socio-Quiz-reg.html")
def hackathon(request):
    return render(request, "hackathon.html")
def hackathonreg(request):
    return render(request, "hackathonreg.html")
def Hack(request):
     if request.method == "POST":
       
       
        ateamname = request.POST.get('teamname') 
        am1 = request.POST.get('m1')   
        aemail1 = request.POST.get('email1')   
        aphone1 = request.POST.get('phone1') 
        aaddress = request.POST.get('address')
        am2 = request.POST.get('m2')   
        aemail2 = request.POST.get('email2')   
        aphone2 = request.POST.get('phone2') 
        am3 = request.POST.get('m3')   
        aemail3 = request.POST.get('email3')   
        aphone3= request.POST.get('phone3')  
        am4 = request.POST.get('m4')   
        aemail4 = request.POST.get('email4')   
        aphone4= request.POST.get('phone4')  
        acomments= request.POST.get('comments')  

         

        account2 = HackathonRegistration( teamname=ateamname, member1=am1, email1=aemail1, phone1=aphone1, address=aaddress,member2=am2, email2=aemail2, phone2=aphone2, member3=am3, email3=aemail3, phone3=aphone3, member4=am4, email4=aemail4, phone4=aphone4, comments=acomments)
        account2.save()
        sub = "Registration Successful | Hackathon | Abhyuday, IIT Bombay"
        msg = """
Hello {},

Greetings from Abhyuday, IIT Bombay!

Congratulations! You've successfully registered for the upcoming Hackathon Get ready for an exciting journey of innovation and problem-solving. Ensure your tools are prepared for the kickoff on Abhyuday's Social Fest (Dates to be released soon). This is your opportunity to showcase your skills and make a meaningful impact. 

Whatsapp Community: https://chat.whatsapp.com/BvXBdtvgvuUBDDnfpNQJtm 

Join above whatsapp group for updates and further details. To get all the details about the competition, explore our website at https://www.competitions.abhyudayiitb.org/. All further updates will be conveyed to you via mail, website or Whatsapp community and do follow us on our Instagram handle @iitbombay_abhyuday to stay connected with us!

We're thrilled to have you on board, and we can't wait to witness the incredible solutions you and your team will bring to Hackathon .

Best of luck, and get ready for an unforgettable hacking experience!

For any queries, write to me @prajyot.abhyuday@gmail.com 

Best Regards,
Prajyot Chakre
Competitions Manager
Abhyuday, IIT Bombay

""".format(ateamname)

        # email = EmailMessage(sub, msg, 'competitions.abhyudayiitb@gmail.com', [aemail])
        send_mail(sub,msg, 'competitions.abhyudayiitb@gmail.com', [aemail1,aemail2, aemail3,aemail4])
        # Send the email
        # email.send()
        messages.success(request, "You have successfully registered for ABHYUDAY COMPETITIONS 2023! please check your registered email.")
        return render(request, "hackathon.html")
def SocioExhibitionreg(request):
    return render(request, "SocioExhibitionreg.html")
def Account(request):
    if request.method == "POST":
       
        aschoolname = request.POST.get('schoolname') 
        aaddress = request.POST.get('address')   
        aemail = request.POST.get('email')   
        aphone = request.POST.get('phone')  
        aCity = request.POST.get('City')  
        astate = request.POST.get('stateName') 
        # aprofession = request.POST.get('profession') 
        aprincipal = request.POST.get('principal') 
        aPOC = request.POST.get('POC') 

        account = Socio_trivia_reg( schoolname=aschoolname, address=aaddress, email=aemail, phone=aphone, City=aCity, state=astate,  School_UDISE =aprincipal, POC=aPOC)
        account.save()
        sub = "Registration Confirmation & Students Registration for School Competitions at Social Fest'24"
        msg = """
Dear {},\n

Thank you for registering {} for the upcoming competitions as part of Social Fest organized by Abhyuday, IIT Bombay. We appreciate your interest and participation in engaging students in these impactful events.

To facilitate the registration of your students for the competitions, we have provided Google Forms for each competition. Kindly find the links below:
\n
Social Trivia Registration Form: "https://forms.gle/kCcdG2YF55kgz36Z9"
Socio Exhibition Registration Form: "https://forms.gle/your_socio_exhibition_form_link"
Adhikaar Registration Form: "https://forms.gle/your_debate_jr_form_link"
 
Please ensure that the required details of the participating students are filled in accurately using the respective forms.

For any queries, write to us at competitions.abhyudayiitb@gmail.com or Contact:
Om Desai | 7208303692 | Competitions Manager
We look forward to the active participation of your school's students in these competitions./n


Best Regards,
Regards,
Competitions
Abhyuday, IIT Bombay.
""".format(aPOC,aschoolname)

        # email = EmailMessage(sub, msg, 'competitions.abhyudayiitb@gmail.com', [aemail])
        send_mail(sub,msg, 'competitions.abhyudayiitb@gmail.com', [aemail])
        # Send the email
        # email.send()
        messages.success(request, "You have successfully registered for ABHYUDAY COMPETITIONS 2023! please check your registered email.")
        return render(request, "SocioQuiz.html")
    print('hello')
def Socio_ex(request):
    if request.method == "POST":
        # schoolname = request.POST.get('schoolname')
        aschoolname = request.POST.get('schoolname') 
        aaddress = request.POST.get('address')   
        aemail = request.POST.get('email')   
        aphone = request.POST.get('phone')  
        aCity = request.POST.get('City')  
        astate = request.POST.get('stateName') 
        # aprofession = request.POST.get('profession') 
        aprincipal = request.POST.get('principal') 
        aPOC = request.POST.get('POC') 

        ex_account = SocioExhibition( schoolname=aschoolname, address=aaddress, email=aemail, phone=aphone, City=aCity, state=astate,  principal=aprincipal, POC=aPOC)
        ex_account.save()
#         sub = "Registration Successful | Action Plan'23 | Abhyuday, IIT Bombay"
#         msg = """
#         Dear {},\n

# Greetings from Abhyuday, IIT Bombay!\n

# Congratulations on successfully registering for the competition at AbhyudayIITB.\n

# Best Regards,\n
# Team Action Plan 2023-24\n
# Abhyuday, IIT Bombay.""".format(aschoolname)

#         email = EmailMessage(sub, msg, 'info.tedxiitbombay@gmail.com', [aemail])
       
#         # Send the email
#         email.send()
        sub = "Registration Confirmation & Students Registration for School Competitions at Social Fest'24"
        msg = """
Dear {},\n

Thank you for registering {} for the upcoming competitions as part of Social Fest organized by Abhyuday, IIT Bombay. We appreciate your interest and participation in engaging students in these impactful events.

To facilitate the registration of your students for the competitions, we have provided Google Forms for each competition. Kindly find the links below:
\n
Social Trivia Registration Form: "https://forms.gle/kCcdG2YF55kgz36Z9"
Socio Exhibition Registration Form: "https://forms.gle/your_socio_exhibition_form_link"
Adhikaar Registration Form: "https://forms.gle/your_debate_jr_form_link"
 
Please ensure that the required details of the participating students are filled in accurately using the respective forms.

For any queries, write to us at competitions.abhyudayiitb@gmail.com or Contact:
Om Desai | 7208303692 | Competitions Manager
We look forward to the active participation of your school's students in these competitions./n


Best Regards,
Regards,
Competitions
Abhyuday, IIT Bombay.
"""    

        # email = EmailMessage(sub, msg, 'competitions.abhyudayiitb@gmail.com', [aemail])
        send_mail(sub,msg, 'competitions.abhyudayiitb@gmail.com', [aemail])
        messages.success(request, "You have successfully registered for ABHYUDAY COMPETITIONS 2023! please check your registered email.")
   
    return render(request, "SocioExhibition.html")
def Case(request):
    return render(request, "Case.html")
def Casestudyreg(request):
    return render(request, "Casestudyreg.html")
def Case_study(request):
     if request.method == "POST":
       
        ateamname = request.POST.get('teamname') 
        am1 = request.POST.get('m1')   
        aemail1 = request.POST.get('email1')   
        aphone1 = request.POST.get('phone1') 
        aaddress = request.POST.get('address')
        am2 = request.POST.get('m2')   
        aemail2 = request.POST.get('email2')   
        aphone2 = request.POST.get('phone2') 
        am3 = request.POST.get('m3')   
        aemail3 = request.POST.get('email3')   
        aphone3= request.POST.get('phone3')  
        acomments= request.POST.get('comments')  
        

        account = CaseStudy( teamname=ateamname, member1=am1, email1=aemail1, phone1=aphone1,address=aaddress, member2=am2, email2=aemail2, phone2=aphone2, member3=am3, email3=aemail3, phone3=aphone3, comments=acomments)
        account.save()
        sub = "Registration Successful | Case Study Competition | Abhyuday, IIT Bombay"
        msg = """
       
Hello Team {},

Greetings from Abhyuday, IIT Bombay!

Congratulations on successfully registering for Case Study Competition .

To move ahead and make your mark in this competition, you (Team) are required to go through the Preliminary round. You (Team) are required to develop 2 slides (max)  that comprehensively covers all relevant aspects of the case study based on the Problem Statement provided below Slides should include thorough research, a clear presentation of the main idea, identification of challenges, and an exploration of financial implications. Make sure to work on it judiciously as your submission are your ticket to the pre-finals. 

Problem Statement : https://docs.google.com/document/d/1JQnc_nmmhRyneohwXAoXqHsB-L7fMDfatfgezq0p8hk/edit?usp=sharing 

Submission Link - https://forms.gle/rtUsHKhPduU27q2Q7 
Submission Deadline - 3 Jan 2023, Wed 11:59 PM

Whatsapp Community: https://chat.whatsapp.com/LCh0msjtY8l2rRcBG1XKjs 	

Join above whatsapp community for updates and reminders. To get all the details about the competition, explore our website at https://www.competitions.abhyudayiitb.org/. All further updates will be conveyed to you via website, mail, or Whatsapp Community and do follow us on our Instagram handle @iitbombay_abhyuday to stay connected with us!

For any queries, write to me @prajyot.abhyuday@gmail.com 

Best Regards,
Prajyot Chakre
Competitions Manager
Abhyuday, IIT Bombay
""".format(ateamname)

        # email = EmailMessage(sub, msg, 'competitions.abhyudayiitb@gmail.com', [aemail])
        send_mail(sub,msg, 'competitions.abhyudayiitb@gmail.com', [aemail1,aemail2,aemail3])
        # Send the email
        # email.send()
        messages.success(request, "You have successfully registered for ABHYUDAY COMPETITIONS 2023! please check your registered email.")
        return render(request, "Case.html")  
def PIL(request):
      return render(request, "PIL.html")
def PilDraftreg(request):
    return render(request, "PilDraftreg.html")
def PilDrafting(request):
     if request.method == "POST":
       
        ateamname = request.POST.get('teamname') 
        am1 = request.POST.get('m1')   
        aemail1 = request.POST.get('email1')   
        aphone1 = request.POST.get('phone1') 
        aaddress = request.POST.get('address')
        am2 = request.POST.get('m2')   
        aemail2 = request.POST.get('email2')   
        aphone2 = request.POST.get('phone2') 
        am3 = request.POST.get('m3')   
        aemail3 = request.POST.get('email3')   
        aphone3= request.POST.get('phone3')  
        acomments= request.POST.get('comments')  
        

        account = PIL_DRAFT( teamname=ateamname, member1=am1, email1=aemail1, phone1=aphone1,address=aaddress, member2=am2, email2=aemail2, phone2=aphone2, member3=am3, email3=aemail3, phone3=aphone3, comments=acomments)
        account.save()

        
        sub = " Registration Successful | PIL Drafting Competition | Abhyuday, IIT Bombay"
        msg = """
Hello Team {},

Greetings from Abhyuday, IIT Bombay!

Congratulations! We are thrilled to inform you that your registration for the upcoming Public Interest Litigation (PIL) Drafting Competition has been successfully completed. All the details, including Topic of PIL,submission instructions, formatting guidelines, judging criteria, and the content required for drafting the Public Interest Litigation (PIL), will be accessible in the document provided below. Please review the document carefully to ensure compliance with the specified requirements. 

Details :  https://docs.google.com/document/d/1HrfWIjsFSD8oGMwnfj9BdTgL_MjHHQAoVUWw1rRFSwg/edit?usp=sharing 

Submission Link - https://forms.gle/Yv66AffDxpQBBGZq9 
Submission Deadline - 15 Jan 2023, Mon 11:59 PM

Whatsapp Community: https://chat.whatsapp.com/B7liSLdlYU64Pv7xkzuNhM 	

Join above Whatsapp Community for updates and reminders. To get all the details about the competition, explore our website at https://www.competitions.abhyudayiitb.org/. All further updates will be conveyed to you via website, mail, or Whatsapp Community and do follow us on our Instagram handle @iitbombay_abhyuday to stay connected with us!

For any queries, write to me @prajyot.abhyuday@gmail.com 

Best Regards,
Prajyot Chakre
Competitions Manager
Abhyuday, IIT Bombay
""".format(ateamname)

        # email = EmailMessage(sub, msg, 'competitions.abhyudayiitb@gmail.com', [aemail])
        send_mail(sub,msg, 'competitions.abhyudayiitb@gmail.com', [aemail1, aemail2, aemail3])
        # Send the email
        # email.send()
        messages.success(request, "You have successfully registered for ABHYUDAY COMPETITIONS 2023! please check your registered email.")
        return render(request, "PIL.html") 
def Union_budget(request):
      return render(request, "SPF.html")
def union_budgetreg(request):
    return render(request, "SPFreg.html")
def SP_F(request):
    
        aschoolname = request.POST.get('schoolname') 
        aaddress = request.POST.get('address')   
        aemail = request.POST.get('email')   
        aphone = request.POST.get('phone')  
        aCity = request.POST.get('City')  
        astate = request.POST.get('stateName') 
        # aprofession = request.POST.get('profession') 
        # aprincipal = request.POST.get('principal') 
        # aPOC = request.POST.get('POC') 

        account = union_budget_reg( team_leader_Name=aschoolname,  College_Name=aaddress, email=aemail, phone=aphone, City=aCity, state=astate)
        account.save()
        sub = "Registration Successful | The Union Budget | Abhyuday, IIT Bombay"
        msg = """
    

Dear {},

Greetings from Abhyuday, IIT Bombay!

Congratulations on successfully registering as a team leader for The Union Budget.

To move ahead and make your mark in this competition, you are required to fill in the Team Information and Questionnaire Form, which contains the details of all of your team members, along with a basic questionnaire containing questions about the budget allocation process and various legislatures across the world and answer them to the best of your knowledge. The answers should reflect more of your personal analysis and plainly writing facts or points won't fetch you any points.
Make sure to fill it in judiciously as your answers are your ticket to the finals. 

Form Link - https://forms.gle/qYKrA6pSiazEXbf68 
Deadline to submit this form - 25th December 11:59pm

To get all the details about the competition, explore our website at https://www.competitions.abhyudayiitb.org/ . All further updates will be conveyed to you via mail, and do follow us on our Instagram handle @iitbombay_abhyuday to stay connected with us!

For any queries, write to me devang.abhyuday@gmail.com 

So, get ready to be a part of the Parliament right here at IIT Bombay.

Best Regards,
Devang Agarwal
Competitions Manager
Abhyuday, IIT Bombay
""".format(aschoolname)

        # email = EmailMessage(sub, msg, 'competitions.abhyudayiitb@gmail.com', [aemail])
        send_mail(sub,msg, 'competitions.abhyudayiitb@gmail.com', [aemail])
        # Send the email
        # email.send()
        messages.success(request, "You have successfully registered for ABHYUDAY COMPETITIONS 2023! please check your registered email.")
        return render(request, "SPF.html")      
def mootcourt(request):
      return render(request, "mootcourt.html")
def mootcourtreg(request):
    return render(request, "mootcourtreg.html")
def moot_court(request):
     if request.method == "POST":
       
        ateamname = request.POST.get('teamname') 
        am1 = request.POST.get('m1')   
        aemail1 = request.POST.get('email1')   
        aphone1 = request.POST.get('phone1') 
        aaddress = request.POST.get('address')
        am2 = request.POST.get('m2')   
        aemail2 = request.POST.get('email2')   
        aphone2 = request.POST.get('phone2') 
        am3 = request.POST.get('m3')   
        aemail3 = request.POST.get('email3')   
        aphone3= request.POST.get('phone3')  
        acomments= request.POST.get('comments')  
        

        account4 = mootcourt_reg( teamname=ateamname, member1=am1, email1=aemail1, phone1=aphone1, College=aaddress, member2=am2, email2=aemail2, phone2=aphone2, member3=am3, email3=aemail3, phone3=aphone3, comments=acomments)
        account4.save()
        
        sub = "Registration Successful | Moot Court Competition| Abhyuday, IIT Bombay"
        msg = """
Hello Team {},

Greetings from Abhyuday, IIT Bombay!

Congratulations! We are pleased to inform you that your registration for the upcoming Moot Court Competition has been successfully processed. Welcome to this exciting legal journey!
As this competition is part of the Social Fest, every round will take place exclusively within the premises of IIT Bombay. The vibrant atmosphere and academic setting of our campus will undoubtedly enhance your overall experience during the competition.

Whatsapp Community: https://chat.whatsapp.com/HFG9t9Zf7bdC4npSrU0kcW 

Join above Whatsapp Community for updates and further details. To get all the details about the competition, explore our website at https://www.competitions.abhyudayiitb.org/. All further updates will be conveyed to you via mail, website or Whatsapp community and do follow us on our Instagram handle @iitbombay_abhyuday to stay connected with us!

We look forward to your active participation and wish you the best of luck in the Moot Court Competition.

For any queries, write to me prajyot.abhyuday@gmail.com 

Best Regards,
Prajyot Chakre
Competitions Manager
Abhyuday, IIT Bombay
""".format(ateamname)

        # email = EmailMessage(sub, msg, 'competitions.abhyudayiitb@gmail.com', [aemail])
        send_mail(sub,msg, 'competitions.abhyudayiitb@gmail.com', [aemail1, aemail2, aemail3])
        # Send the email
        # email.send()
        messages.success(request, "You have successfully registered for ABHYUDAY COMPETITIONS 2023! please check your registered email.")
        return render(request, "mootcourt.html")    
def mock_parliament(request):
      return render(request, "adhikar.html")
def Mock_parliamentreg(request):
    return render(request, "adhikarreg.html")
def adhi(request):
     if request.method == "POST":
       
        aschoolname = request.POST.get('schoolname') 
        aaddress = request.POST.get('address')   
        aemail = request.POST.get('email')   
        aphone = request.POST.get('phone')  
        aCity = request.POST.get('City')  
        astate = request.POST.get('stateName') 
        # aprofession = request.POST.get('profession') 
        # aprincipal = request.POST.get('principal') 
        # aPOC = request.POST.get('POC') 

        account = mock_parliament_reg( Name=aschoolname, College=aaddress, email=aemail, phone=aphone, City=aCity, state=astate,  )
        account.save()
        sub = " Registration Successful | Mock Parliament | Abhyuday, IIT Bombay"
        msg = """
Dear {},

Greetings from Abhyuday, IIT Bombay!

Congratulations on successfully registering for the Mock Parliament.

To move ahead and make your mark in this competition, you are required to submit a 3-4 min video of yourselves speaking out your personal views on the topic “Should India protect its domestic industries by restricting trade and using trade protectionism?”. You should upload your video in the following google form. The video should contain more of your own analysis and reasons. Support your analysis by relevant facts and figures. You will be judged on the basis of clarity, communication and reason.

Make sure to fill it in judiciously as this video is your ticket to the finals.

Form Link - https://forms.gle/T7HjHqBAEvvcVgHb7
Deadline to submit this form - 25th December 11:59pm

To get all the details about the competition, explore our website at https://www.competitions.abhyudayiitb.org/ . All further updates will be conveyed to you via mail, and do follow us on our Instagram handle @iitbombay_abhyuday to stay connected with us!

For any queries, write to me @devang.abhyuday@gmail.com 

So, get ready to be a part of the Parliament right here at IIT Bombay.

Best Regards,
Devang Agarwal
Competitions Manager
Abhyuday, IIT Bombay
""".format(aschoolname)

        # email = EmailMessage(sub, msg, 'competitions.abhyudayiitb@gmail.com', [aemail])
        send_mail(sub,msg, 'competitions.abhyudayiitb@gmail.com', [aemail])
        # Send the email
        # email.send()
        messages.success(request, "You have successfully registered for ABHYUDAY COMPETITIONS 2023! please check your registered email.")
        return render(request, "adhikar.html")  
def adhikar(request):
      return render(request, "adhikar_jr.html")
def adhikarreg(request):
    return render(request, "adhikar_jrreg.html")
def adhi_jr(request):
     if request.method == "POST":
       
        aschoolname = request.POST.get('schoolname') 
        aaddress = request.POST.get('address')   
        aemail = request.POST.get('email')   
        aphone = request.POST.get('phone')  
        aCity = request.POST.get('City')  
        astate = request.POST.get('stateName') 
        # aprofession = request.POST.get('profession') 
        aprincipal = request.POST.get('principal') 
        aPOC = request.POST.get('POC') 

       
        account5 = adhikar_reg( schoolname=aschoolname, address=aaddress, email=aemail, phone=aphone, City=aCity, state=astate,  principal=aprincipal, POC=aPOC)
        account5.save()
        sub = "Registration Confirmation & Students Registration for School Competitions at Social Fest'24"
        msg = """
Dear {},\n

Thank you for registering {} for the upcoming competitions as part of Social Fest organized by Abhyuday, IIT Bombay. We appreciate your interest and participation in engaging students in these impactful events.

To facilitate the registration of your students for the competitions, we have provided Google Forms for each competition. Kindly find the links below:
\n
Social Trivia Registration Form: "https://forms.gle/kCcdG2YF55kgz36Z9"
Socio Exhibition Registration Form: "https://forms.gle/your_socio_exhibition_form_link"
Adhikaar Registration Form: "https://forms.gle/your_debate_jr_form_link"

Please ensure that the required details of the participating students are filled in accurately using the respective forms.

For any queries, write to us at competitions.abhyudayiitb@gmail.com or Contact:
Om Desai | 7208303692 | Competitions Manager
We look forward to the active participation of your school's students in these competitions./n


Best Regards,
Regards,
Competitions
Abhyuday, IIT Bombay.
""".format(aPOC,aschoolname)
        send_mail(sub,msg, 'competitions.abhyudayiitb@gmail.com', [aemail])
        # Send the email
        # email.send()
        messages.success(request, "You have successfully registered for ABHYUDAY COMPETITIONS 2023! please check your registered email.")
        return render(request, "adhikar_jr.html")  