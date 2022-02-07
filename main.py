import requests, threading, os, random
from fake_useragent import UserAgent

ua = UserAgent()
count = 0
proxy = open("proxies.txt").read().splitlines()
headers = {
	"User-Agent": ua.random
}
acc = input("https://camo.githubusercontent.com/")

def randomproxy():
    return random.choice(proxy)

def main():
	try:
		global count
		requests.get(f"https://camo.githubusercontent.com/{acc}", headers=headers, proxies={"http": 'http://' + randomproxy()})
		count += 1
		print(f'Boosted - {count}')
		os.system(f'title Made by BRYoN aka. Chiinkiboi ^| Views Counter: {count}')
	except Exception as e:
		print(e)
		pass

while True:
	thread = threading.Thread(target=main)
	thread.start()