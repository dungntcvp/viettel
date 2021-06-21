# coding: utf-8

# In[2]:

import time
from bs4 import BeautifulSoup
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# @author Ranjeet Singh <ranjeetsingh867@gmail.com>
# Modify it according to your requirements

no_of_reviews = 1000

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
driver = webdriver.Chrome(r"E:\DATA SCIENCE\chromedriver.exe")

wait = WebDriverWait(driver, 10)

# Append your app store urls here
urls = ["https://apps.apple.com/us/app/mb-bank/id1205807363#see-all/reviews"]

for url in urls:

    driver.get(url)

    page = driver.page_source

    soup_expatistan = BeautifulSoup(page, "html.parser")
    driver.get(url)
    time.sleep(5)  # wait dom ready
    driver.maximize_window()
    for i in range(1, 10):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')  # scroll to load other reviews
        time.sleep(1)
    page = driver.page_source
    soup_expatistan = BeautifulSoup(page, "html.parser")
    expand_pages = soup_expatistan.findAll("div", class_="we-customer-review lockup")
    counter = 1
    #
    file1 = open(r"C:\Users\ADMIN\PycharmProjects\app-store-crawl\appstore.txt", "a")
    # file2 = open(r"E:\DATA SCIENCE\google-play-crawler-master\myfile1.txt", "w")
    for expand_page in expand_pages:
        # try:
            print("\n===========\n")
            print("review：" + str(counter))

            a = str(counter)
            print("Author Name: " + str(expand_page.find("span", class_="we-customer-review__user").text))
            b = expand_page.find("span", class_="we-customer-review__user").text
            print("Review Date: " + expand_page.find("time", class_="we-customer-review__date").text)
            c = expand_page.find("time", class_="we-customer-review__date").text
            # '''
            # //didn't find reviewer link
            # print("Reviewer Link: ", expand_page.find("a", class_="reviews-permalink")['href'])
            # '''
            print("Title: " + expand_page.find("h3", class_="we-customer-review__title").text)
            d = expand_page.find("h3", class_="we-customer-review__title").text
            reviewer_ratings = expand_page.find_next()['aria-label']
            reviewer_ratings = reviewer_ratings.split(' ')[0]
            reviewer_ratings = ''.join(x for x in reviewer_ratings if x.isdigit())
            print("Reviewer Ratings: " + reviewer_ratings)
            f = reviewer_ratings
            '''
            //didn't find review title
            print("Review Title: ", str(expand_page.find("span", class_="review-title").string))
            '''
            # print("Review Body: ", str(expand_page.find("div", class_="we-clamp").text))
            all_reviews = expand_page.find("div", class_="we-clamp").find_all_next(lambda tag: tag.name == "p")
            list_of_inner_text = [x.text for x in all_reviews]
            # If you want to print the text as a comma separated string
            text = ' '.join(list_of_inner_text)
            print("Review Body: " + text)
            # print("Review Body: ", str(expand_page.find("div", class_="we-clamp").find_next()['p'].text))
            counter += 1
            # f = str(expand_page.find("div", class_="UD7Dzf").text)
            # listabc = str(counter)+","+str(expand_page.find("span", class_="X43Kjb").text)+","+expand_page.find("span", class_="p2TkOb").text+","+reviewer_ratings+","+str(expand_page.find("div", class_="UD7Dzf").text)+"\n"

            listabc = a + "," + b + "," + c + "," + d + "," + f + "," + text + "\n"
            # listabc = a + "," + b + "," + c + "\n"
            # listabc = a+"\n"
            # listcdf = f+"\n"
            file1.write(listabc)
            # file2.write(listcdf)
            # developer_reply = expand_page.find_parent().find("div", class_="LVQB0b")
            # if hasattr(developer_reply, "text"):
            #     print("Developer Reply: "+"\n", str(developer_reply.text))
            # else:
            #     print("Developer Reply: ", "")

        # except:
        #     pass
    file1.close()  # to change file access modes
# file2.close()
driver.quit()
