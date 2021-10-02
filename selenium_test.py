from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

GITHUB_URL = "https://github.com/"


driver = webdriver.Chrome("./chromedriver.exe")
driver.maximize_window()
driver.get(GITHUB_URL)


element = driver.find_element_by_name("q")
element.send_keys("React")
element.send_keys(Keys.RETURN)

element = driver.find_element_by_xpath("//a[text()='Advanced search']")
element.click()

select = Select(driver.find_element_by_xpath("//label[text()='Written in this language']/../../dd/select"))
select.select_by_visible_text('JavaScript')


select = Select(driver.find_element_by_xpath("//label[text()='With this license']/../../dd/select"))
select.select_by_visible_text('Boost Software License 1.0')

driver.find_element_by_xpath("//label[text()='With this many stars']/../../dd/input").send_keys(">45")

driver.find_element_by_xpath("//label[text()='With this many followers']/../../dd/input").send_keys(">50")

driver.find_element_by_xpath("//div[@class='form-group flattened']/div/button").click()


repo_list = driver.find_elements(By.XPATH, "//ul[@class='repo-list']/li")

assert len(repo_list) == 1, "multiple repos available after advance search"

repo = "mvoloskov/decider"
repo_name = driver.find_element_by_xpath('//div[@class="f4 text-normal"]/a')
assert repo_name.text == "mvoloskov/decider", f"{repo} repo not found"

repo_name.click()


driver.find_element_by_xpath("//div[@role='grid']//div[@role='rowheader']//a[@title='README.md']").click()


read_me = driver.find_element_by_xpath("//article").text
print(read_me[0:300])

driver.quit()
