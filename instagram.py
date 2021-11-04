from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
import time
import random
import datetime
dt_now = datetime.datetime.now()
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
    time.sleep(10)

#ハッシュタグ検索
def tagsearch(tag):
    instaurl = 'https://www.instagram.com/explore/tags/'
    driver.get(instaurl + tag)
    time.sleep(random.randint(8, 10))
    f = open('insta.txt','a')
    f.write("listtagより、tagで検索を行いました\n")
    f.close()
    time.sleep(4)

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

        #13~16回いいね
    for i in range(random.randint(13, 16)):
        count = i
        try:
            driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            f = open('insta.txt','a')
            f.write("次の投稿へ移動しました\n")
            f.close()
            time.sleep(random.randint(random.randint(8, 10), random.randint(11, 13)))

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
        hour = dt_now.hour
        if (23 < hour or hour < 8):
            abc = random.randint(random.randint(32400, 32500), random.randint(32501, 32600))
            f = open('insta.txt', 'a')
            f.write(str(hour)+"時になりました" + str(abc) + "秒待機します。 おやすみなさい。" + "\n")
            f.close()

        else:
            abc = random.randint(random.randint(1800, 1860), random.randint(1861, 1900))

        f = open('insta.txt','a')
        f.write(str(abc)+"秒待機します\n")
        f.close()
        time.sleep(abc)
