import requests
import demjson
import random
import time



def run():
    s = requests.session()
    n = 1945
    while 1:
        h = {
                        "Accept": "*/*",
                      "Accept-Encoding": "gzip, deflate",
                      "Accept-Language": "zh-CN,zh;q=0.9",
                      "Connection": "keep-alive",
                      "Host": "chuanbo.weiboyi.com",
                      "Referer": "http://www.weiboyi.com/",
                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"

        }
        r = s.get("http://chuanbo.weiboyi.com/hwauth/index/captchaajax", headers=h)
        t = r.text
        t = t.replace("(", "")
        t = t.replace(")", "")
        a = demjson.decode(t)
        url = a['url']

        time.sleep(2)

        h = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Host": "img.weiboyi.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"

        }
        img = s.get(url, headers=h)

        with open(f"../images/h{n}.jpg", "wb") as f:
            f.write(img.content)
        n += 1
        time.sleep(3)



if __name__ == "__main__":

    run()