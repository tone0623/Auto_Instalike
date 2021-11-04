from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
import time
import random
import datetime
from webdriver_manager.chrome import ChromeDriverManager
import Return_Value as rv

count = 0

#ログイン
def login():
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    f = open('insta.txt','a')
    f.write("instagramにアクセスしました\n")
    f.write(str(datetime.datetime.now()) + "\n")
    f.close()
    time.sleep(5)

 #メアドと 、パスワードを入力
    username, password = rv.return_pass()

    driver.find_element_by_name('username').send_keys(username)
    time.sleep(3)
    driver.find_element_by_name('password').send_keys(password)
    time.sleep(3)

 #ログインボタンを押す
    driver.find_element_by_class_name('L3NKy       ').click()
    time.sleep(random.randint(4, 6))
    f = open('insta.txt','a')
    f.write("instagramにログインしました\n")
    f.write(str(datetime.datetime.now()) + "\n")
    f.close()
    time.sleep(6)

#ハッシュタグ検索
def tagsearch(tag):
    instaurl = 'https://www.instagram.com/explore/tags/'
    driver.get(instaurl + tag)
    time.sleep(random.randint(2, 10))
    f = open('insta.txt','a')
    f.write("listtagより、tagで検索を行いました\n")
    f.close()
    time.sleep(1)

#いいね
def clicknice():
    target = driver.find_elements_by_class_name('_9AhH0')[10]
    actions = ActionChains(driver)
    actions.move_to_element(target)
    actions.perform()
    f = open('insta.txt','a')
    f.write("最新の投稿まで画面を移動しました\n")
    f.close()
    time.sleep(5)

    try:
        driver.find_elements_by_class_name('_9AhH0')[9].click()
        time.sleep(random.randint(2, 10))
        f = open('insta.txt','a')
        f.write("投稿をクリックしました\n")
        f.close()
        time.sleep(3)
        driver.find_element_by_class_name('fr66n').click()
        f = open('insta.txt','a')
        f.write("投稿をいいねしました\n")
        f.close()
        time.sleep(2)

    except WebDriverException:
        f = open('insta.txt','a')
        f.write("エラーが発生しました")
        f.write(str(datetime.datetime.now()) + "\n")
        f.close()
        return

        #17~19回いいね
    for i in range(random.randint(17, 19)):
        count = i
        try:
            driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            f = open('insta.txt','a')
            f.write("次の投稿へ移動しました\n")
            f.close()
            time.sleep(random.randint(random.randint(6, 8), random.randint(8, 10)))

        except WebDriverException:
            f = open('insta.txt','a')
            f.write("２つ目の位置でエラーが発生しました")
            f.write(str(datetime.datetime.now()) + "\n")
            f.close()
            time.sleep(6)

        try:
            driver.find_element_by_class_name('fr66n').click()
            f = open('insta.txt','a')
            f.write("投稿をいいねしました\n")
            f.close()
            time.sleep(8)
        except WebDriverException:
            f = open('insta.txt','a')
            f.write("3つ目の位置でエラーが発生しました ")
            f.write(str(datetime.datetime.now()) + "\n")
            f.close()
    f = open('insta.txt','a')
    f.write( str(count) + '件の投稿をいいねしました ' + str(datetime.datetime.now()) + "\n" )
    f.close()

if __name__ == '__main__':

    taglist = rv.return_tag()
       # driver = webdriver.Chrome('./chromedriver')
        driver: WebDriver = webdriver.Chrome(ChromeDriverManager().install())
        time.sleep(1)
        login()

        tagsearch(random.choice(taglist))
        time.sleep(3)
        clicknice()

        driver.close()

        abc = random.randint(random.randint(1300, 1400), random.randint(1401, 1500))
        f = open('insta.txt','a')
        f.write(str(abc)+"秒待機します\n")
        f.close()
        time.sleep(abc)
