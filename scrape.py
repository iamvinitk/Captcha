import base64
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import test

driver = webdriver.Chrome()

driver.get("http://results.vtu.ac.in/vitaviresultcbcs2018/index.php")

# find the captcha element
ele_captcha = driver.find_element_by_xpath("//img[contains(./@src, 'captcha_new.php')]")

# get the captcha as a base64 string
img_captcha_base64 = driver.execute_async_script("""
    var ele = arguments[0], callback = arguments[1];
    ele.addEventListener('load', function fn(){
      ele.removeEventListener('load', fn, false);
      var cnv = document.createElement('canvas');
      cnv.width = this.width; cnv.height = this.height;
      cnv.getContext('2d').drawImage(this, 0, 0);
      callback(cnv.toDataURL('image/jpeg').substring(22));
    }, false);
    ele.dispatchEvent(new Event('load'));
    """, ele_captcha)

# save the captcha to a files
with open(r"captcha.jpg", 'wb') as f:
    f.write(base64.b64decode(img_captcha_base64))

time.sleep(5)
usn = "1CD15CS001"
captcha = test.process()
username = driver.find_element_by_name("lns")
username.send_keys(usn)
captchacode = driver.find_element_by_name("captchacode")
captchacode.send_keys(captcha)
captchacode.send_keys(Keys.ENTER)
