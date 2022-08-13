

from asyncio.log import logger
import re
from select import select
from django.http import HttpResponse, JsonResponse, request
from django.shortcuts import render
from libs.mysql import *
from django.views.decorators.csrf import csrf_exempt
from Api.Funtion import *
@csrf_exempt
def VersionCheck(req):
   if(req.method == "GET"):
          rv= Select("select * from version_control_application;") 
          res=  JsonResponse({"response":True , "data":rv})
          return HttpResponse(res)


@csrf_exempt
def Signup_Customer(req):
       if(req.method == "POST"):
         try:
            query ="INSERT INTO `customer` (`id`, `email`, `mobile`, `name`, `address_id`, `photo`, `email_varification`, `mobile_varification`, `date`, `session_id`, `sha256`,`pass`) VALUES (NULL,'{}', '{}', '{}', '0', '0', '0', '0', '{}', '0', '{}','{}');".format(req.POST['email'],req.POST['mobile'],req.POST['name'],req.POST['date'],req.POST['sha'],req.POST['pass'])
            rv= insertData(query)
            Generate_OTP(rv,req.POST['email'])
            res=  JsonResponse({"response":True , "data":Select("select id from customer where id= {}".format(rv))})
            response = HttpResponse(res,None,200,"successfully registered")
         except:
            res=  JsonResponse({"response":False , "data":[{"message":"Something went wrong"}]})
            response = HttpResponse(res,None,208,"User Already registered")
       else:
             response = HttpResponse("Method Not Allowed!",None,405,"Method Not Allowed")
       return response

@csrf_exempt
def OTP_Varification(req):
       try:
         if(req.headers['sha'] != None and req.headers['sha'] != ""  and Authentication(req.headers['sha'],req.POST['id'])):
               if(req.method == "POST"):
                  try:
                     rv= Select("select otp from otp_varification where otp={} and customer_id= (select id from customer where id={} and mobile={} and email= '{}')".format(req.POST['otp'],req.POST['id'],req.POST['mobile'],req.POST['email']))
                     print(rv)
                     if(len(rv)!= 0 and req.POST['otp']!= "" and rv[0]['otp']==int(req.POST['otp'])):
                           res=  JsonResponse({"response":True , "data":Select("select id from customer where id= {}".format(req.POST['id']))})
                     else:
                           res=  JsonResponse({"response":False , "data":[{"message":"Incorrect OTP"}]})
                     response = HttpResponse(res,None,200,"Successfully Requested")
                  except:
                     res=  JsonResponse({"response":False , "data":[{"message":"Something went wrong"}]})
                     response = HttpResponse("Bad Request",None,400,"Bad Request")
               else:
                     response = HttpResponse("Method Not Allowed!",None,405,"Method Not Allowed")
         else:
               response = HttpResponse("UnAuthorized Access!",None,401,"UnAuthorized Access")
       except:
         response = HttpResponse("UnAuthorized Access!",None,401,"UnAuthorized Access")

       return response

@csrf_exempt
def Login(req):
       try:
         if(req.headers['sha'] != None and req.headers['sha'] != ""  and Authentication(req.headers['sha'],12)):
               if(req.method == "POST"):
                  try:
                     rv= Select("SELECT * FROM `customer` where sha256 = '{}';".format(req.headers['sha']))
                     print(rv)
                     if(len(rv)!= 0 and req.POST['mobile']!= "" and req.POST['password']!= "" and rv[0]['mobile']==req.POST['mobile'] and rv[0]['pass']==req.POST['password'] ):
                           res=  JsonResponse({"response":True , "data":Select("select id,name,email,mobile from customer where id= {}".format(rv[0]['id']))})
                     else:
                           res=  JsonResponse({"response":False ,  "data":[{"message":"Incorrect Credentials"}]})
                     response = HttpResponse(res,None,200,"Successfully Requested")
                  except:
                     res=  JsonResponse({"response":False ,  "data":[{"message":"Something went wrong"}]})
                     response = HttpResponse("Bad Request",None,400,"Bad Request")
               else:
                     response = HttpResponse("Method Not Allowed!",None,405,"Method Not Allowed")
         else:
               response = HttpResponse("UnAuthorized Access!",None,401,"UnAuthorized Access")
       except:
         response = HttpResponse("UnAuthorized Access!",None,401,"UnAuthorized Access")

       return response

             
           
          
       

        
          
   