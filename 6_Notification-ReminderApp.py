
#** Run this code on anaconda 
import time
from turtle import title
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title = "Please Drink Water",
        message = "A well-known myth says you should drink eight 8-ounce glasses of water every day to be healthy.",
        # app_icon = "C:\\Users\\ADMIN\\OneDrive\\Desktop\\Python Projects\\waterglass.ico",
        timeout = 10
    )