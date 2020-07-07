# -*- coding: utf-8 -*-
# =============================================================================
# Copyright (c) 2018-, pyLeo Developer. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================


from train.captcha_run import CaptchaRun
from concurrent.futures import ThreadPoolExecutor
import requests
import time




def test(n):
	
	s = requests.session()
	response = s.get("https://cashiermd.95516.com/b2c/checkcode.action")
	image_data = response.content
	
	response = s.post("http://114.116.242.163:18088/captcha/ko/", data=image_data)
	print(response.text)
	
	# with open(f"img/{response.text}-{int(time.time())}.png", "wb") as f:
	# 	f.write(image_data)


def test2(n):
	s = requests.session()
	response = s.get("https://cashiermd.95516.com/b2c/checkcode.action")
	image_data = response.content


	s = time.time()
	
	CR = CaptchaRun()
	
	pre_text = CR.captcha2text(image_data, 'model/')
	
	CR.tf.reset_default_graph()
	
	e = time.time()
	print(' 模型预测值:', pre_text, "时间：", e - s)


	# with open(f"img/{response.text}-{int(time.time())}.png", "wb") as f:
	# 	f.write(image_data)
	
	






if __name__ == '__main__':

	# for i in range(100):
	# 	test2(i)
	
	executor = ThreadPoolExecutor(max_workers=1)
	urls = [3 for x in range(5000)]  # 并不是真的url
	for data in executor.map(test, urls):
		pass
	



