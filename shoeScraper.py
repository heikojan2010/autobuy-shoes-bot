import requests, json
from selenium import webdriver
import time



r = requests.get('https://featuresneakerboutique.com/products.json')

products = json.loads((r.text))['products']

for product in products:
    productname = product['title']

    if productname == "Puma Court Rider 2K - White/Ultra Grey":
        producturl = 'https://featuresneakerboutique.com/products/' + product['handle']

driver = webdriver.Chrome(executable_path='/Users/home/gaysthtcode/web_scraping/chromedriver')
driver.get("https://feature.com/products/puma-court-rider-2k-white-ultra-grey")
#To Click On size-10
driver.find_element_by_xpath('//div[@data-value="10"]').click()

#Add item to le shopping cart...
driver.find_element_by_xpath('//*[@id="product_form_6568763686983"]/button').click()


#go to CHECK OUT page
driver.find_element_by_xpath('//*[@id="shopify-section-header"]/div/div[2]/div[3]/a')
time.sleep(1)


driver.find_element_by_xpath('//*[@id="ajax-cart"]/div/div/section/footer/a').click()

#Enter Email
driver.find_element_by_xpath('//*[@id="checkout_email"]').send_keys('maryhadalittlelamb@webmailz.gov')
#Enter First Name
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]').send_keys('Jane')
time.sleep(0.5)
#Etner Last Name 
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_last_name"]').send_keys('Doe')
#Enter Street Address
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address1"]').send_keys('1600 Pennsylvania Avenue NW')
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_city"]').send_keys('New York')
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]').send_keys('11106')
#Enter Phone
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_phone"]').send_keys('646-666-6666')

#go to Next checkout page / shipping type selection
driver.find_element_by_xpath('//*[@id="continue_button"]').click()
time.sleep(5)

#go to Payment page
driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/div[2]/div[1]/form/div[2]/button').click()
