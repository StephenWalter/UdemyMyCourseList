import requests
from bs4 import BeautifulSoup
import time
import smtplib

while True:
    url = 'https://pastebin.com/Mfc9txQV'
    headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'})
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    if str(soup).find('Key') == -1:
        time.sleep(500)
        continue
    else:
        print("ALERT!!!!")

        create_email = 'Subject: ALERT - PASTEBIN - KEY FOUND!'
        from_address = ''
        to_address = ''
        mail = smtplib.SMTP('smtp.gmail.com', 587)

        mail.startls()
        mail.login('username', 'password')

        mail.sendmail(from_address, to_address, create_email)
        mail.close()

        break