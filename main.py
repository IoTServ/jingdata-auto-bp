# coding=utf-8
# http://chromedriver.storage.googleapis.com/index.html
from selenium import webdriver
import time

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    # 指定浏览器，参数是浏览器驱动的路径，前面加上r防止转义
    driver = webdriver.Chrome(r"./chromedriver")  # 打开浏览器
    # 用get打开页面
    driver.get("https://cloud.jingdata.com/#/insight/InsightInvestor")
    # page_text = driver.page_source
    # print(page_text)
    # 下面是演示一下其他操作
    # #查找页面的“设置”选项，并点击
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div/div[3]/button/span').click()
    time.sleep(1)
    driver.find_element_by_css_selector("div[class='tab-item']").click()
    time.sleep(1)
    driver.find_element_by_css_selector("input[placeholder='请输入手机号码/邮箱']").send_keys("####你的鲸准账号手机号")
    driver.find_element_by_css_selector("input[placeholder='请输入密码']").send_keys("######你的鲸准密码")
    driver.find_elements_by_css_selector("button[class~='submit-btn']")[1].click()
    time.sleep(2)
    driver.find_element_by_css_selector("span[class='tool-search-more']").click()
    time.sleep(1)
    for element in driver.find_elements_by_css_selector("span[class='sift-item-more']"):
        element.click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="__main_layout__"]/div[2]/div/div[1]/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/div[2]/div/div/span[2]/span[2]/span').click()
    count = 0
    print("8秒后开始进行提交操作")
    time.sleep(8)
    while True:
        print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
        print("开始点击提交按钮")
        elements = driver.find_elements_by_css_selector("span[class='bp-button']")
        print(len(elements))
        for element in elements:
            try:
                element.click()
            except Exception:
                print(Exception)
            else :
                count = count + 1
            time.sleep(1)
            if count >= 60:
                count = 0
                print("开始休眠")
                time.sleep(60*61)
                print("休眠一个小时后的时间", time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
        time.sleep(2)
        # 下一页
        # driver.execute_script("window.scrollTo(0,100000)")
        # driver.find_element_by_css_selector("i[class~='el-icon-arrow-right']").click()
        try:
            driver.find_elements_by_css_selector("button[class='btn-next']")[1].click()
        except Exception:
            print(Exception)
        time.sleep(1)
