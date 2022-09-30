#/usr/bin/python3
from googlesearch import search
from socket import timeout
import sys
from termcolor import colored
import urllib
import urllib.request
import terminal_banner
import random
import os


os. system('clear')

banner = ("""
                    
              ╔═╗╔═╗ ╦  ╦   ╔═╗╦╔╗╔╔╦╗╔═╗╦═╗
              ╚═╗║═╬╗║  ║───╠╣ ║║║║ ║║║╣ ╠╦╝
              ╚═╝╚═╝╚╩═╝╩   ╚  ╩╝╚╝═╩╝╚═╝╩╚═                          
                        Made with ❤️ 
            For the Community, By the Community   

            ###################################

                  Developed by Jitesh Kumar
            Intagram  - https://instagram.com/jitesh.haxx
            linkedin  - https://linkedin.com/j1t3sh 
                Github - https://github.com/j1t3sh
                                    
       ( DONT COPY THE CODE. CONTRIBUTIONS ARE MOST WELCOME ❤️ )
                                                                                
""")
banner_terminal = terminal_banner.Banner(banner)
print (colored(banner_terminal, 'green')+ "\n")

website_list=[] #list of websites
dork = "inurl:" + input(colored("Please input the sqli Dork(eg- php?id=, aspx?id=) ---->  ",'cyan'))
extension = "site:" + input(colored("Please specify the website extension(eg- .in,.com,.pk) [default: none] -----> ",'cyan')) #Add none as extension
total_output = int(input(colored("Pleases specify the total no. of websites you want) ----> ",'cyan')))
page_no = int(input(colored("From which Google page you want to start(eg- 1,2,3) ----> ",'cyan')))

if extension == "site:":
    extenstion = ""

try:
    query = dork + " " +  extension 
    pause_random = int(random.randrange(4, 10, 2))
    for j in search(query, num=10,start=page_no*5,stop=total_output, pause=pause_random,
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'): #add User-Agent
        website_list.append(j) 

    for i in website_list:
            try:
                fullurl = i
                try:
                    resp = urllib.request.urlopen(fullurl + "'", timeout=15) #set timeout 
                except timeout:
                    print (i + " ===> " + colored("Time out !",'orange'))
                    pass #pass if website not responding after 15 seconds
                body = resp.read()
                fullbody = body.decode('utf-8')
                if "SQL syntax" in fullbody:  
                    print(i + " ===> " +  colored(" Vulnerable!",'green')) #if vulnerable
                else:
                    print (i + " ===> " + colored(" Not Vulnerable!",'red')) #if not vulnerable
                    
            except:
                print(i + "  ===> " + colored(" Can not be Determined",'blue'))
                continue
except:

    print("Your IP has been blocked by Google, Wait for 1 hr. ")
    print("Go chill outside then comeback & start to hunt again :)")
