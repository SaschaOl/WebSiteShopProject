import Shop
import bot
import threading



if __name__ == "__main__":
    thread1 = threading.Thread(target = bot.bot.infinity_polling)
    thread1.start()
    Shop.shop_project.run(debug = True)