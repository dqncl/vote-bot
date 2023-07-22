from random import randrange
import time
import requests
import subprocess

website = "https://www.herbstfest-rosenheim.de/miss-herbstfest/miss-herbstfest/miss-herbstfest-2023-wahl-jetzt-interview-finalistinnen-ansehen-abstimmen-92385787.html"

def set_random_timer():
    min = randrange(11)
    sec = min * 60
    print(f"Sleep set to {min} min")
    time.sleep(sec)
    
def refresh_proxies():
    print("Refreshing proxies...\nNew proxies added to list:\n")
    subprocess.run(["/bin/python", "/home/daniel/Projects/vote-bot/proxy-test.py", ">>", "/home/daniel/Projects/vote-bot/working-proxies.txt"])

def get_rand_proxy() -> str:
    with open("working-proxies.txt", "r") as f:
        proxies = f.read().split("\n")
        rand_proxy = proxies[randrange(len(proxies))]
        return rand_proxy

def web_req():
    proxy = get_rand_proxy()
    print(f"Used Proxy Server: {proxy}")
    post_req = ""
    #TODO create Webrequest
    set_random_timer()

refresh_proxies()