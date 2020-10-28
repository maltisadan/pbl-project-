from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from tkinter import *

class twitter_bot:
	def __init__(self,username,password):
		self.username=username
		self.password=password
		self.bot=webdriver.Chrome(executable_path = r"C:\Users\Manas Singh\AppData\Local\Programs\Python\Python38-32\chromedriver.exe")


	def login(self):
		bot=self.bot
		bot.get('https://twitter.com/')
		time.sleep(5)
		email=bot.find_element_by_name("session[username_or_email]")
		password=bot.find_element_by_name("session[password]")
		email.clear()
		password.clear()
		email.send_keys(self.username)
		time.sleep(2)
		password.send_keys(self.password)
		# password.send_keys(Keys.RETURN)
		pyautogui.typewrite(["enter"])
		time.sleep(1)


	def like_tweet(self,entry3):
		bot=self.bot
		bot.get('https://twitter.com/search?q=%23'+str(entry3)+'&src=typed_query')
		while True:
			pyautogui.click(pyautogui.locateCenterOnScreen('LIKE.PNG'))
			time.sleep(3)
			bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
			time.sleep(2)

def execute():
	log=twitter_bot(str(entry1.get()),str(entry2.get()))
	log.login()
	time.sleep(5)
	log.like_tweet(entry3.get())



window=Tk()
window.geometry("500x300")
emails=Label(window,text="email", font=('bold' , 14), pady=20, padx=10)
emails.grid(row=0,column=0)
entry1=Entry(window)
entry1.grid(row=0,column=3)


password=Label(window,text="password", font=('bold' , 14), pady=20, padx=10)
password.grid(row=1,column=0)
entry2=Entry(window)
entry2.grid(row=1,column=3)


hashtag=Label(window,text="hashtag", font=('bold' , 14), pady=20, padx=10)
hashtag.grid(row=2,column=0)
entry3=Entry(window)
entry3.grid(row=2,column=3)


b1=Button(window,text="G0",command=execute,width=12,bg='grey')
b1.grid(row=7,column=1)
window.mainloop()