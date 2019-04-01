import subprocess,shlex,time
import pyttsx,re,webbrowser
import speech_recognition as sr
from selenium import webdriver
global aud
global p
global s
global r
while True:
 urldataset=["songs","Song","ganna","ganne","Facebook","Cricbuzz","cricket","YouTube"]
 wikidataset=["about","Wikipedia","info","Wiki","details"]
 weatherdataset=["weather","weather report"]
 meaningdataset=["meaning"]

 


 def input1():
   global p
   global aud
   r=sr.Recognizer()
   mic=sr.Microphone()
   with mic as source:
     r.adjust_for_ambient_noise(source)
     aud=r.listen(source)
   aud=r.recognize_google(aud)
   p=shlex.split(aud)
   print type(aud)
   print type(p[1])
   print aud
   return aud

 
 

 def openurl(k):
    driver = webdriver.Chrome(executable_path="/home/akshat/chromedriver")
    url="http://"+k+".com"
    driver.get(url)
    webbrowser.open_new_tab(url)



 def weather(b):
  import weather
  command="weather" +" "+b+ "--u"
  arg=shlex.split(command)
  j=subprocess.check_output(arg)
  print j


 
 def word_meaning(c):
    from PyDictionary import PyDictionary
    dic=PyDictionary()
    print dic.meaning(c)

    
 def wikipedia(o):
    driver = webdriver.Chrome(executable_path="/home/akshat/chromedriver")
    url="https://en.wikipedia.org/wiki/"+o
    driver.get(url)
    webbrowser.open_new_tab(url)


 def Outputvoice(v):
    engine=pyttsx.init()
    rate=engine.getProperty("rate")
    volume=engine.getProperty("volume")
    engine.setProperty("volume",volume-0.40)
    engine.setProperty("rate",rate-70)
    engine.say(v)
    engine.runAndWait()


    
 def searchfile():
   b=input1()
   def fileop(r,b):
    try:
      file1=open("/home/akshat/"+r+"/"+b,"r")
      print "Destination"+" "+r
      print file1.read()
    except:
        pass
    try:
      file1=open("/home/akshat/"+r+"/"+b+".py","r")
      print "Destination"+" "+r
      print file1.read()
    except:
        pass



   def home(b):
      try:
        file1=open("/home/akshat/"+b+".py","r")
        print "Destination is Home"
        print file1.read()
      except:
            pass
      try:
        file1=open("/home/akshat/"+r+"/"+b,"r")
        print "Destination"+" "+r
        print file1.read()
      except:
        pass
         



   def Downloads(b):
     try:
       r="Downloads"
       fileop(r,b)
     except:
      pass




   def Documents(b):
    try:
     r="Documents"
     print b
     fileop(r,b)
    except:
      pass
 



   def Music(b):   
    try:
      r="Music"
      fileop(r,b)
    except:
      pass

 



   def Videos(b):
     try:
      r="Videos"
      fileop(r,b)
     except:
       pass




   def Pictures(b):
     try:
       r="Pictures"
       fileop(r,b)
     except:
       pass
    


   
   home(b)
   Downloads(b)
   Documents(b)
   Videos(b)
   Music(b)
   Pictures(b)


   
 def audio():
    from pygame import mixer
    import time
    s=input1()
    def music(r,s):
      mixer.init()
      mixer.music.load("/home/akshat/"+r+"/"+s+".mp3")
      print "destination is"+" "+r
      mixer.music.play()
      time.sleep(400)
      mixer.music.stop()

    def home(s):
     try:
      mixer.init()
      mixer.music.load("/home/akshat/"+s+".mp3")
      mixer.music.play()
      time.sleep(100)
      mixer.music.stop()
     except:
        pass


    def Downloads(s):
     try:
      r="Downloads"
      music(r,s)
     except:
       pass
    def Documents(s):
     try:
      r="Documents"
      music(r,s)
     except:
         pass
 
    def Music(s):
     try:
      r="Music"
      music(r,s)
     except:
       pass

 
    def Videos(s):
     try:
      r="Videos"
      music(r,s)
     except:
       pass

    def Pictures(s):
     try:
      r="Pictures"
      music(r,s)
     except:
      pass

    
    home(s)
    Downloads(s)
    Documents(s)
    Videos(s)
    Music(s)
    Pictures(s)


           
 input1()
 if p[0] in urldataset:
    openurl(p[0])
 else:
    if p[0] in wikidataset:
        o=p[1]+" "+p[2]
        wikipedia(o)
    else:
        if p[1] in weatherdataset:
            weather(p[0])
        else:
            if p[1] in meaningdataset:
                word_meaning(p[0])
            else:
                if aud=="search file":
                    Outputvoice("Tell the name of the file sir")
                    searchfile()
                else:
                    if aud=="play song":
                        Outputvoice("Tell me the name of the song sir")
                        audio()
 time.sleep(10)
 Outputvoice("say again")
