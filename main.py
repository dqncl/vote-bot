from random import randrange
import random
import time
import requests

url = 'https://api.embed.pinpoll.com/v2/vote'
proxies = ['62.113.208.89:3127','77.253.212.238:8123','78.47.194.20:3128','79.143.185.163:3127','80.153.189.234:8888','85.15.45.192:8081','85.214.16.236:3128','92.222.14.156:8080','134.0.30.69:8888','144.76.185.207:8888','178.63.44.93:3128','178.251.229.227:8080','188.40.20.142:3128','213.61.167.40:8080','217.160.22.24:3128']
proxies_available = []

def proxy_test():
    for p in proxies:
        try:
            res = requests.get('http://ipinfo.io/json', 
            proxies={'https:':p})
        except:
            continue
            print(res)
        if res.status_code == 200:
            print(res)
            proxies_available.append(p)
        
def set_random_timer():
    min = randrange(11)
    sec = min * 60
    print(f'Sleep set to {min} min')
    time.sleep(sec)

def web_req():
    proxy = random.choice(proxies_available)
    timeTillVote = randrange(4312, 312250)
    content = {'question_id':'200020','require_user_opt_in':'false','origin':'https://www.herbstfest-rosenheim.de/miss-herbstfest/miss-herbstfest/miss-herbstfest-2023-wahl-jetzt-interview-finalistinnen-ansehen-abstimmen-92385787.html','timeTillVote':timeTillVote,'answer_id':'765041','consent':'false'}
    header = {'Content-Type': 'application/json'}
    print(f'Used Proxy Server: {proxy}')
    r = requests.post(url,data=content,headers=header,proxies={'https:':proxy})
    print(r.text,"TEXT\n", r.content, "CONTENT\n", r.status_code,"STAUSCODE\n")

def main():
    while True:
        i = 0
        proxies_available.clear
        proxy_test()
        for i in range(21):
            print(proxies_available)
            set_random_timer()
            web_req()
            i=+1
            
if __name__ == "__main__":  
    while True:
        i = 0
        proxies_available.clear
        proxy_test()
        for i in range(21):
            print(proxies_available)
            set_random_timer()
            web_req()
            i=+1
