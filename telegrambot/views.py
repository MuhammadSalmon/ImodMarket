import telebot
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Order

bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome! Please enter your password to view orders.")

@bot.message_handler(func=lambda message: True)
def authenticate(message):
    password = message.text
    if password == 'your_password':  # Replace with your desired password
        orders = Order.objects.all()
        orders_text = "\n".join([f"{order.product_name} - {order.quantity} - {order.status}" for order in orders])
        bot.send_message(message.chat.id, f"Orders:\n{orders_text}")
    else:
        bot.send_message(message.chat.id, "Invalid password!")

@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        json_str = request.body.decode('UTF-8')
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
    return JsonResponse({'status': 'ok'})
