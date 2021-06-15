from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path=r'C:\QA\Selenium\chromedriver.exe')
browser.implicitly_wait(10)
browser.get('https://www.seleniumeasy.com/test/table-search-filter-demo.html')
table=browser.find_element_by_css_selector('table#task-table')# מזהה טבלה כולה
rows=table.find_elements_by_tag_name('tr')#יוצר רשימה של שורות בתוך הטבלה לפי TAG NAME

for row in rows:# עובר על שורות  ברשימה
    cells=row.find_elements_by_tag_name('td') # מגדיר רשימת תאים בשורה לפי TAG NAME
    for cell in cells:# עובר על תאים
        print(cell.text,'|',end='\t') #
    print()