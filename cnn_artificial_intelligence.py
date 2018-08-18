from selenium import webdriver
import codecs
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome("d:/driver1/chromedriver.exe")

f = codecs.open("d:/민재/여름방학 공부/파이썬 기초반 7월/crawling/cnn_artificial intelligence/cnn_links.txt", "w", "utf-8")

driver.get("https://edition.cnn.com/")

time.sleep(2)

driver.find_element_by_xpath("//*[@id=\"menu\"]").click()
driver.find_element_by_xpath("//*[@id=\"search-input-field\"]").click()

elem = driver.find_element_by_xpath("//*[@id=\"search-input-field\"]")
elem.send_keys("Artificial Intelligence")
elem.submit()

for order in range(0,74):

    driver.get("https://edition.cnn.com/search/?q=Artificial%20Intelligence&size=10&from="+
                str(order * 10)+"&page=" + str(order+1))

    time.sleep(3)

    source = driver.page_source

    html = BeautifulSoup(source, "html.parser")

    s1 = html.find_all("div", class_="cnn-search__results")
    # print(len(s1))

    s2 = s1[0].find_all("a")
    # print(len(s2))
    # for i in s2:
    #     print(i.text.strip())

    articlelist = []
    linklist = []
    titlelist = []

    idx = 0
    for i in s2:
        if idx % 2 == 1:
            articlelist.append(i)
        idx += 1
    #
    # for i in articlelist:
    #     titlelist.append(i.text.strip())

    # print(titlelist)

    idx = 0
    listing = order * 10
    for i in articlelist:
        titlelist.append(i.text.strip())
        linklist.append("https:"+str(i).split("href=\"")[1].split("\">")[0])
        print("{}. {} -> {}" . format(listing+1,titlelist[idx], linklist[idx]))
        f.write("{}. {} -> {}" . format(listing+1,titlelist[idx], linklist[idx]) + "\r\n")
        idx += 1
        listing += 1

    # idx = 1
    # for i, j in zip(titlelist, linklist):
    #     print("{}. {} -> {}" . format(idx,i, j))
    #     # print(str(idx) + ". "+ i + ":" + j)
    #     # f.write(str(idx) + ". "+ i + " -> " + j +"\r\n")
    #     f.write("{}. {} -> {}" . format(idx,i, j) + "\r\n")
    #     idx += 1
    time.sleep(2)

f.close()
driver.close()
