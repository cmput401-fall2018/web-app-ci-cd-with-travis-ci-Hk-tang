from selenium import webdriver


def test_home():
    driver = webdriver.Chrome()
    driver.get("http://162.246.157.149:8000")
    name = driver.find_element_by_id("name")
    about = driver.find_element_by_id("about")
    education = driver.find_element_by_id("education")
    skills = driver.find_element_by_id("skills")
    work = driver.find_element_by_id("work")
    contact = driver.find_element_by_id("contact")
    assert name is not None
    assert about is not None
    assert education is not None
    assert skills is not None
    assert work is not None
    assert contact is not None
