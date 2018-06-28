import api
from models import *
from menu import Menu
import schedule
import time
import datetime

class Scraper:

    def get_new_dispensaries(self):
        api.download_dispensaries()

    def scrape_menus(self):
        self.get_new_dispensaries()
        dispensaries = Dispensary.select()
        t = datetime.datetime.now()
        for d in dispensaries:
            m = Menu(d.slug, d._type)
            m.download_menu(t)

if __name__ == '__main__':

    s = Scraper()
    schedule.every().day.at("08:00").do(s.scrape_menus)

    while True:
        schedule.run_pending()
        time.sleep(1080)


