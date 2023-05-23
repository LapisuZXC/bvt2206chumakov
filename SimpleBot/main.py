import telebot
from telebot import types
import psycopg2
import datetime

timetable_show = [2,3,4,5,6]

def week():
    number = int(datetime.datetime.utcnow().isocalendar()[1])
    return number

conn = psycopg2.connect(database="bvt2206_Chumakov_Dmitriy_bot",
                        user="postgres",
                        password="Zawarudo112",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()

understandable_text = ('хочу','привет')

cursor.execute("SELECT r.id, r.day, r.start_time, r.subject ,r.lesson_type, r.room_number,  p.full_name FROM public.timetable r, public.teacher p WHERE r.teachers=p.id")
Full_time_table = list(cursor.fetchall())

token = "6008875672:AAEgZqWsKnYAczYG5Q28gPopTwZ-7pgINgI"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу","/help","/week","/nextweek")
    keyboard.row("/Понедельник","/Вторник","/Среда")
    keyboard.row("/Четверг","/Пятница","/Суббота") 
    bot.send_message(message.chat.id,'Здравствуйте! Хотите узнать свежую информацию о МТУСИ?',reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id,'Я умею: \n ')



@bot.message_handler(commands=['Понедельник'])
def monday(message):
    result = f'================= \n Понедельник (нечётная) \n'
    for number in range(30,35):
        if Full_time_table[number][3] == 'нет пары':
                    result+= str(Full_time_table[number][2]) + '\n'
                    result+='<Нет пары> \n'
        else:
            for item in timetable_show:
                result += f'{Full_time_table[number][item]} \n'
        result+='\n'
    result += f'================= \n Понедельник (чётная) \n'
    for number in range(5):
        if Full_time_table[number][3] == 'нет пары':
                    result+= str(Full_time_table[number][2]) + '\n'
                    result+='<Нет пары> \n'
        else:
            for item in timetable_show:
                result += f'{Full_time_table[number][item]} \n'
        result+='\n'
    bot.send_message(message.chat.id,result)  

@bot.message_handler(commands=['Вторник'])
def tuesday(message):
    result = f'================= \n Вторник (нечётная) \n'
    for number in range(35,40):
        if Full_time_table[number][3] == 'нет пары':
                    result+= str(Full_time_table[number][2]) + '\n'
                    result+='<Нет пары> \n'
        else:
            for item in timetable_show:
                result += f'{Full_time_table[number][item]} \n'
        result+='\n'
    result += f'================= \n Вторник (чётная) \n'
    for number in range(5,10):
        if Full_time_table[number][3] == 'нет пары':
                    result+= str(Full_time_table[number][2]) + '\n'
                    result+='<Нет пары> \n'
        else:
            for item in timetable_show:
                result += f'{Full_time_table[number][item]} \n'
        result+='\n'
    bot.send_message(message.chat.id,result)  

@bot.message_handler(commands=['Среда'])
def wednesday(message):
    result = f'================= \n Среда (нечётная) \n'
    for number in range(40,45):
        if Full_time_table[number][3] == 'нет пары':
                    result+= str(Full_time_table[number][2]) + '\n'
                    result+='<Нет пары> \n'
        else:
            for item in timetable_show:
                result += f'{Full_time_table[number][item]} \n'
        result+='\n'
    result += f'================= \n Среда (чётная) \n'
    for number in range(10,15):
        if Full_time_table[number][3] == 'нет пары':
                    result+= str(Full_time_table[number][2]) + '\n'
                    result+='<Нет пары> \n'
        else:
            for item in timetable_show:
                result += f'{Full_time_table[number][item]} \n'
        result+='\n'
    bot.send_message(message.chat.id,result)  

@bot.message_handler(commands=['Четверг'])
def thursday(message):
    result = f'================= \n Четверг (нечётная) \n'
    for number in range(45,50):
        if Full_time_table[number][3] == 'нет пары':
                    result+= str(Full_time_table[number][2]) + '\n'
                    result+='<Нет пары> \n'
        else:
            for item in timetable_show:
                result += f'{Full_time_table[number][item]} \n'
        result+='\n'
    result += f'================= \n Четверг (чётная) \n'
    for number in range(15,20):
        if Full_time_table[number][3] == 'нет пары':
                    result+= str(Full_time_table[number][2]) + '\n'
                    result+='<Нет пары> \n'
        else:
            for item in timetable_show:
                result += f'{Full_time_table[number][item]} \n'
        result+='\n'
    bot.send_message(message.chat.id,result)  

@bot.message_handler(commands=['Пятница'])
def friday(message):
    result = f'================= \n Пятница (нечётная) \n'
    for number in range(50,55):
        if Full_time_table[number][3] == 'нет пары':
                    result+= str(Full_time_table[number][2]) + '\n'
                    result+='<Нет пары> \n'
        else:
            for item in timetable_show:
                result += f'{Full_time_table[number][item]} \n'
        result+='\n'
    result += f'================= \n Пятница (чётная) \n'
    for number in range(20.25):
        if Full_time_table[number][3] == 'нет пары':
                    result+= str(Full_time_table[number][2]) + '\n'
                    result+='<Нет пары> \n'
        else:
            for item in timetable_show:
                result += f'{Full_time_table[number][item]} \n'
        result+='\n'
    bot.send_message(message.chat.id,result)  

@bot.message_handler(commands=['Суббота'])
def satruday(message):
    result = f'================= \n Суббота (нечётная) \n'
    for number in range(55,60):
        if Full_time_table[number][3] == 'нет пары':
                    result+= str(Full_time_table[number][2]) + '\n'
                    result+='<Нет пары> \n'
        else:
            for item in timetable_show:
                result += f'{Full_time_table[number][item]} \n'
        result+='\n'
    result += f'================= \n Суббота (чётная) \n'
    for number in range(25,30):
        if Full_time_table[number][3] == 'нет пары':
                    result+= str(Full_time_table[number][2]) + '\n'
                    result+='<Нет пары> \n'
        else:
            for item in timetable_show:
                result += f'{Full_time_table[number][item]} \n'
        result+='\n'
    bot.send_message(message.chat.id,result)  

  
 


@bot.message_handler(commands=['week'])
def this_week(message):
    result = ''
    cursor.execute("SELECT r.id, r.day, r.start_time, r.subject ,r.lesson_type, r.room_number,  p.full_name FROM public.timetable r, public.teacher p WHERE r.teachers=p.id")
    Full_time_table = list(cursor.fetchall())
    if week() % 2 == 0:
        result = result + f'{week()} неделя (чётная) \n' 
        
        for i in range(30):
            if Full_time_table[i][0] == i+1:    
                if i == 0 or i == 5 or i == 10 or i == 15 or i == 20 or i == 25:
                    result += '================\n \n'
                    result += str(Full_time_table[i][1]) +'\n \n'
                if Full_time_table[i][3] == 'нет пары':
                    result+= str(Full_time_table[i][2]) + '\n'
                    result+='<Нет пары> \n \n'
                else:
                    for l in timetable_show:
                        result = result + str(Full_time_table[i][l] ) +'\n'
                    result+= '\n'

    elif week() % 2 != 0:
        result += f'{week()} неделя (нечётная) \n'
        for i in range(30,59):
            if Full_time_table[i][0] == i+1:    
                if i == 30 or i == 35 or i == 40 or i == 45 or i == 50 or i == 55:
                    result += '================\n \n'
                    result += str(Full_time_table[i][1]) +'\n \n'
                if Full_time_table[i][3] == 'нет пары':
                    result+=str(Full_time_table[i][2]) + '\n'
                    result+='<Нет пары> \n \n'
                else:
                    for l in timetable_show:
                        result = result + str(Full_time_table[i][l] ) +'\n'
                    result+= '\n'
    bot.send_message(message.chat.id,result)


@bot.message_handler(commands=['nextweek'])
def next_week(message):
    week_count = week() + 1
    result = ''
    
    if week_count % 2 == 0:
        result = result + f'{week_count} неделя (чётная) \n' 
        
        for i in range(30):
            if Full_time_table[i][0] == i+1:    
                if i == 0 or i == 5 or i == 10 or i == 15 or i == 20 or i == 25:
                    result += '================\n \n'
                    result += str(Full_time_table[i][1]) +'\n \n'
                if Full_time_table[i][3] == 'нет пары':
                    result+= str(Full_time_table[i][2]) + '\n'
                    result+='<Нет пары> \n \n'
                else:
                    for l in timetable_show:
                        result = result + str(Full_time_table[i][l] ) +'\n'
                    result+= '\n'

    elif week_count % 2 != 0:
        result+= f'{week_count} неделя (нечётная) \n'
        for i in range(30,59):
            if Full_time_table[i][0] == i+1:    
                if i == 30 or i == 35 or i == 40 or i == 45 or i == 50 or i == 55:
                    result += '================\n \n'
                    result += str(Full_time_table[i][1]) +'\n \n'
                if Full_time_table[i][3] == 'нет пары':
                    result+=str(Full_time_table[i][2]) + '\n'
                    result+='<Нет пары> \n \n'
                else:
                    for l in timetable_show:
                        result = result + str(Full_time_table[i][l] ) +'\n'
                    result+= '\n'
    bot.send_message(message.chat.id,result)

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id,'Тогда вам сюда - https://mtuci.ru/')
    elif message.text.lower() == "привет":
        bot.send_message(message.chat.id,'Здравствуйте!')
    elif message.text.lower() not in understandable_text:
        bot.send_message(message.chat.id,'Я не понимаю')





bot.infinity_polling()