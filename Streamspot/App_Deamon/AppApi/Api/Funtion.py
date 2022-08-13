from libs.Email import *
from libs.mysql import *
import random

def Generate_OTP(C_ID , emailid):
    otp = random.randint(1000,9999)
    query = "INSERT INTO `otp_varification` (`id`, `otp`, `customer_id`) VALUES (NULL, '{}', '{}');".format(otp,C_ID)
    insertData(query)
    email= Mail()
    email.send(emailid.split(),"One Time Password for Stream Spot.",email.setContent(otp, emailid))

def Authentication(token, id):
    q= Select("select id from customer where sha256 ='{}'".format(token))
    # if(len(q)!= 0 and id != "" and  int(id) == q[0]['id']):
    if(len(q)!= 0 ):
        return True
    else:
        return False

   
        

