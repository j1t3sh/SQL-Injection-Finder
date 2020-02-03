#/usr/bin/python3
from googlesearch import search
import sys
import urllib
import urllib.request
from termcolor import colored
import random

website_list=[]
#query = "inurl:php?id= site:.com"
dork = "inurl:" + input(colored("Please input the sqli Dork(eg- php?id=, aspx?id=) ---->  ",'green'))
extension = "site:" + input(colored("Please specify the website extension(eg- .in,.com,.pk) -----> ",'green'))
total_output = int(input(colored("Pleases specify the total no. of websites you want) ----> ",'green')))
page_no = int(input(colored("From which Google page you want to start(eg- 1,2,3) ----> ",'green')))
query = dork + " " +  extension 
pause_random = int(random.randrange(3, 10, 1))
for j in search(query, num=10,start=page_no*10,stop=total_output, pause=pause_random): 
    website_list.append(j) 
print(website_list)
'''for i in website_list:
        try:
            fullurl = i

            resp = urllib.request.urlopen(fullurl + "'")
            body = resp.read()
            fullbody = body.decode('utf-8')
            if "SQL syntax" in fullbody:  
                print(i + " ===> " +  colored(" Vulnerable!",'green'))
            else:
                print (i + " ===> " + colored(" Not Vulnerable!",'red'))
                
        except:
            print(i + "  ===> " + colored(" Cannot be Determined",'blue'))
            continue
'''