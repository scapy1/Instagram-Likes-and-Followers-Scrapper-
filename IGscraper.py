import instaloader,os
os.system ("pip install instaloader")
os.system ("clear")
R = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
Y = '\033[1;33m'
W = "\033[0m"
logo=(f"""{R}____________IG-Scraper________________________________

{Y}[+] TeleGram : scapy
{B}[+] Youtube    : scapy
{R}_____________________________________""")

print(logo)
def Liker():
	os.system('rm -rf user.txt')
	os.system('clear')
	print(logo)
	USER = input(Y+"Enter UserName : ")
	PASSWORD = input(G+"Enter PassWord : ")
	link1 = input(R+'Enter Half Post Link : ')
	L = instaloader.Instaloader()
	L.login(USER, PASSWORD)
	Post = instaloader.Post.from_shortcode(L.context, link1)
	for like in Post.get_likes():
	   namaste = '@'+like.username
	   print(namaste)
	   with open ('user.txt','a+') as good :
	   	good.write(namaste+'\n')
def Followers():
	os.system('rm -rf user.txt')
	os.system('clear')
	print(logo)
	USER = input(Y+"Enter UserName : ")
	PASSWORD = input(G+"Enter PassWord : ")
	username1 = input(R+'Enter Target UserName : ')
	L = instaloader.Instaloader()
	L.login(USER, PASSWORD)
	profile = instaloader.Profile.from_username(L.context, username1)
	for follow in profile.get_followers():
	   namaste = '@'+follow.username
	   print (namaste)
	   with open ('user.txt','a+') as good :
	   	good.write(namaste+'\n')
Choose=input(f'''{Y}[1] Scrape Followers
{G}[2] Scrape Likes
{B}[3] Exit
{R}[+] Choose ==> ''')
if Choose == '2':
	Liker()
if Choose == '1':
	Followers()
if Choose == '3':
	os.system('exit')
	