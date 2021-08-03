import mysql.connector
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json
from selenium.webdriver.chrome.options import Options
import passfile

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Adipoo2610",
    database="pythonpro",
    auth_plugin="mysql_native_password"
)
#print (db)

class Person:

   def __init__(self,name,city="Roorkee",work=None):
      self.name = name
      self.city = city
      if(work is not None):
         self.work = work
      else:
         work=[]
         self.work=None
   
   def show(self):
      print("My name is " + self.name +" and my current city is " + self.city)

   def update(self,username):
      cursor = db.cursor()
      cursor.execute("UPDATE info SET name=%s,work=%s,city=%s WHERE username=%s", (str(self.name), json.dumps(self.work), str(self.city), username))
      db.commit()

def printDictionary(username):
   chrome_options = Options()
   chrome_options.add_experimental_option("detach", True)
   usedriver = webdriver.Chrome('/home/pooja/Downloads/chromedriver_linux64/chromedriver')

   usedriver.maximize_window()
   
   time.sleep(2)

   usedriver.get("https://m.facebook.com/"+username+"/about/")
   # usedriver.find_element(By.XPATH, '//*[@id="mobile_login_bar"]/div[2]/a[2]').click()
   
   time.sleep(2)

   email_id = usedriver.find_element_by_id("m_login_email")
   password = usedriver.find_element_by_id("m_login_password")

   email_id.send_keys(passfile.email)
   password.send_keys(passfile.passw)
   time.sleep(5)
   usedriver.find_element_by_id("login_password_step_element").click()
   time.sleep(5)
   usedriver.find_element_by_id("checkpointSubmitButton-actual-button").click()
   time.sleep(6)
   usedriver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/form/div/article/section/div/fieldset/label[3]/div/div[2]/div').click()
   time.sleep(5)
   usedriver.find_element(By.XPATH, '//*[@id="checkpointSubmitButton-actual-button"]').click()
   time.sleep(5)
   usedriver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/form/div/article/section/div/div[2]/div/div[1]/div[2]/fieldset/label[18]/div/div[1]').click()
   time.sleep(4)
   usedriver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/form/div/article/section/div/div[2]/div/div[2]/div[2]/fieldset/label[7]/div/div[1]').click()
   time.sleep(5)
   usedriver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/form/div/article/section/div/div[2]/div/div[3]/div[2]/fieldset/label[7]/div/div[1]').click()
   time.sleep(5)
   usedriver.find_element(By.XPATH, '//*[@id="checkpointSubmitButton-actual-button"]').click()
   time.sleep(5)
   usedriver.find_element(By.XPATH, '//*[@id="checkpointSubmitButton-actual-button"]').click()
   time.sleep(5)
   height_prev = usedriver.execute_script("return document.body.scrollHeight")
   
   while(True):
      usedriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      time.sleep(3)
      height_new = usedriver.execute_script("return document.body.scrollHeight")
      if(height_new==height_prev):
         break
      else:
         height_prev = height_new
   time.sleep(3)
   usedriver.find_element(By.XPATH, "//div[contains(text(),'Likes')]/../../div[3]/a").click()
   time.sleep(3)

   while(True):
      usedriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      time.sleep(3)
      height_new = usedriver.execute_script("return document.body.scrollHeight")
      if(height_new==height_prev):
         break
      else:
         height_prev = height_new

   length = len(usedriver.find_elements(By.XPATH, '//*[@id="timelineBody"]/div/div/div/div[*]'))
   for i in range(length):
      while(True):
         usedriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
         time.sleep(3)
         height_new = usedriver.execute_script("return document.body.scrollHeight")
         if(height_new==height_prev):
            break
         else:
            height_prev = height_new
      # print(length)
      fav = []
      # print(usedriver.find_element(By.XPATH, '//*[@id="timelineBody"]/div/div/div/div['+str(i+1)+']/div/header/div/div[1]/div/div/div[1]')).text
      usedriver.find_element(By.XPATH, '//*[@id="timelineBody"]/div/div/div/div['+str(i+1)+']/div/header/div/div[3]/a').click()
      time.sleep(3)
      while(True):
         usedriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
         time.sleep(3)
         height_new = usedriver.execute_script("return document.body.scrollHeight")
         if(height_new==height_prev):
            break
         else:
            height_prev = height_new
      length1 = len(usedriver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[4]/div/div/div/div/div/div/div/div/div[*]'))
      for j in range(length1):
         for ele in usedriver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[4]/div/div/div/div/div/div/div/div/div['+str(j+1)+']/div[*]/div/span'):
            fav.append(ele.text)
      print(fav)
      time.sleep(10)
      usedriver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[3]/a').click()

def check(func):
   def inner(username):
      
      cursor = db.cursor()
      # cursor.execute("INSERT INTO info(username) VALUES ('pooja1')")
      # db.commit()
      sql = ("SELECT * FROM user where username=\'"+username+"\'")
      sql1 = ("SELECT * FROM info where username=\'"+username+"\'")
      cursor.execute(sql)

      results = cursor.fetchall()
      cursor.execute(sql1)
      results1 = cursor.fetchall()
      ch = False
      ch1 = False
      for row in results:
         ch = True
      for row in results1:
         if(row[1]!=None):
            ch1 = True
         
      if(ch==True):
         if(ch1==True):
            for row in results1:
               obj = Person(row[1],row[2],row[3])
               obj.show()
               
         else: 
            func(username)
      else:
         raise ValueError('username is not valid!')
            
   return inner

@check
def scrap(username):
   URL= "https://m.facebook.com/"+username+"/about/"
   # login(username)
   headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
   r = requests.get(URL,cookies= {'googletrans': '/es/en'},headers=headers)
   soup = BeautifulSoup(r.content, 'html5lib')
   # print(soup.prettify())
   
   table = soup.findAll('div',attrs={'class':'_55wo _2xfb _1kk1'})
   work = []
   place = ""
   i = 0
   name = "abc"
   name = soup.findAll('h3')
   for row in name:
      print(row.text)
   # print(name)
   for row in table:
      table1 = soup.findAll('div',attrs={'class':'_55wo _2xfb _1kk1'})[i]

      for row in table1.find('div',attrs={'class':'__gx'}):
         if(row=='कार्य'):
            a = table1.findAll('div',attrs={'class':'_2pir c'})
            for row in a :
               work.append((row).text)
         if(row=='वास्‍तव्‍य केलेली ठिकाणे'):
               place = (table1.h4.text)
      i = i + 1
   # print(place)
   if(work!=[]):
      if(place!=""):
         obj = Person(name,place,work)
      else:
         obj = Person(name=name,work=work)
   else:
      if(place!=""):
         obj = Person(name=name,city=place)
      else:
         obj = Person(name=name)
   obj.show()
   obj.update(username)
   printDictionary(username)

scrap('radhikagarg1601')
