import requests
import time


def aa():
	s = requests.session()
	t = time.time()
	
	r = s.get("https://cashiermd.95516.com/b2c/checkcode.action")
	
	with open(f"../train/captcha.png", "wb") as f:
		f.write(r.content)


aa()


