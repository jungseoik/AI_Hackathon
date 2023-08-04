from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
from selenium.webdriver.common.action_chains import ActionChains

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com/imghp?hl=ko&authuser=0&ogbl")
elem = driver.find_element(By.NAME, "q")
elem.send_keys("조코딩")
elem.send_keys(Keys.RETURN)
time.sleep(2)

SCROLL_PAUSE_SEC = 1

# 스크롤 높이 가져옴
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # 끝까지 스크롤 다운
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 1초 대기
    time.sleep(SCROLL_PAUSE_SEC)

    # 스크롤 다운 후 스크롤 높이 다시 가져옴
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_elements(By.CSS_SELECTOR, ".LZ4I")[0].click()
        except:
            break
        # break
    last_height = new_height


time.sleep(2)


images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
count = 1
for image in images:
    try:
        ActionChains(driver).move_to_element(image).click().perform()
        # image.click()
        time.sleep(3)
        imgUrl = driver.find_elements(By.CSS_SELECTOR, ".r48jcc.pT0Scc.iPVvYb")[0].get_attribute('src')
        urllib.request.urlretrieve(imgUrl, str(count) +".jpg")
        count +=1
    except:
        pass





# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()