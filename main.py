import requests, threading, os, random
from fake_useragent import UserAgent
from colorama import Fore

ua = UserAgent()
count = 0
proxy = open("proxies.txt").read().splitlines()
headers = {
	"User-Agent": ua.random
}
def clear():
    os.system("cls")
    print(f'\n\t\t\t\t\u001b[38;5;127m╔═╗┬ ┬┬┬┌┐┌┬┌─┬┌┐ ┌─┐┬\n\t\t\t\t\u001b[38;5;128m║  ├─┤│││││├┴┐│├┴┐│ ││\n\t\t\t\t\u001b[38;5;129m╚═╝┴ ┴┴┴┘└┘┴ ┴┴└─┘└─┘┴{Fore.RESET}\n\n\n')
    print(f"{Fore.MAGENTA}The Gay Test"{Fore.RESET})
clear()

def randomproxy():
    return random.choice(proxy)

acc = input("https://camo.githubusercontent.com/")

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
