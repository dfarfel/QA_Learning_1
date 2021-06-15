import webbrowser,time,os,pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import os


browser = webdriver.Chrome(executable_path=r'C:\QA\Selenium\chromedriver.exe')
browser.implicitly_wait(5)
browser.get ('https://captcha.guru/ru/feedback/')
time.sleep(5)
iframe = browser.find_elements_by_tag_name('iframe')[0]
browser.switch_to.frame(iframe)
act = browser.find_element_by_css_selector('.recaptcha-checkbox-border')
act.click()
t=random.uniform(1, 4) #пауза между скачиваниями случайна
browser.switch_to.default_content()
iframe = browser.find_elements_by_tag_name('iframe')[3]
browser.switch_to.frame(iframe)
time.sleep(3)
act = browser.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div[1]/div/strong')
print(act.text)
a=['a fire hydrant','parking meters','bicycles','traffic lights','boats']
if act.text not in a:
                #обновили картинку с капчи
                act = browser.find_element_by_xpath('//*[@id="recaptcha-reload-button"]')
                act.click()
                time.sleep(t)
                browser.switch_to.default_content()
                iframe = browser.find_elements_by_tag_name('iframe')[3] #узнаем категорию капчи:автобусы,гидранты...
                browser.switch_to.frame(iframe)
                time.sleep(2)
                act = browser.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div[1]/div/strong')
                print(act.text)
elif act.text in a:
                    #сохраняем картинку
    os.chdir('C:\QA\pictures')
    im=pyautogui.screenshot(imageFilename=str(0)+'.jpg',region=(509,411,495,495))
    im.save(r'C:\QA\pictures\im.jpg')
                #
                # #нарезаем картинку
                # img = image.open('0.jpg')
                # area1=(0,0,163,163) #спереди,сверху,справа,снизу)
                # img1 = img.crop(area1)
                # area2=(163,0,326,163)
                # img2 = img.crop(area2)
                # area3=(326,0,489,163)
                # img3 = img.crop(area3)
                #
                # area4=(0,163,163,326)
                # img4 = img.crop(area4)
                # area5=(163,163,326,326)
                # img5 = img.crop(area5)
                # area6=(326,163,489,326)
                # img6 = img.crop(area6)
                #
                # area7=(0,326,163,489)
                # img7 = img.crop(area7)
                # area8=(163,326,326,489)
                # img8 = img.crop(area8)
                # area9=(326,326,489,489)
                # img9 = img.crop(area9)
                #
                # img1.save("1"+".png")
                # img2.save("2"+".png")
                # img3.save("3"+".png")
                # img4.save("4"+".png")
                # img5.save("5"+".png")
                # img6.save("6"+".png")
                # img7.save("7"+".png")
                # img8.save("8"+".png")
                # img9.save("9"+".png")