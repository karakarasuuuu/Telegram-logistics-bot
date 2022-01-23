import pytesseract # Image recognition
import urllib.request # Get the image
import os
import time
from PIL import Image # Open image
from selenium import webdriver # Simulate browser
from selenium.webdriver.firefox.options import Options # Browser options


# Permanet link
link = "https://eservice.7-11.com.tw/e-tracking/search.aspx"
# Ref: https://www.learncodewithmike.com/2020/05/python-selenium-scraper.html
# To cancel pop-up windows
option = Options()
# option.add_argument('--headless') # To prevent opening the window

if __name__ == "__main__":

    user_input = 'P20244730847'#input('Please enter your code:')

    # Open a browser
    browser = webdriver.Firefox(executable_path='/home/karasu/home/code/logistics-crawler/geckodriver')#, options=option)
    browser.get(link)
    print('browser opened')    
        
    # Input the code
    code = browser.find_element_by_name('txtProductNum')
    code.send_keys(user_input)
    print('code inputted')

    # Get validation code
    # OCR: https://ithelp.ithome.com.tw/articles/10227263
    validation_image = browser.find_element_by_id('ImgVCode')
    validation_image.screenshot('v.png')
    time.sleep(1)
    pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
    img = Image.open('v.png')
    img.show()
    validation_code = pytesseract.image_to_string(img)
    time.sleep(1)
    # os.system('rm v.png')
    print(validation_code)

    # Input validation code
    validation = browser.find_element_by_name('tbChkCode')
    
    validation.send_keys(validation_code)

    

    # Close the browser
    # browser.quit()

'''
To be done:
- tesseract cannot recognize the number
- it can be done well at first
'''