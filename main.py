from selenium import webdriver

# Start a webdriver instance (e.g. Chrome)
driver = webdriver.Chrome()

# Open the WhatsApp web page
driver.get("https://web.whatsapp.com/")

# Wait for the user to scan the QR code
input("Scan the QR code and press Enter")

# Find the contact you want to send a message to
search_box = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")
search_box.send_keys("<Name or Phone Number of Contact>")

# Wait for the contact to appear
contact = driver.find_element_by_xpath("//*[@id='pane-side']/div[1]/div/div/div[1]")
contact.click()

# Find the message input box and send the message
message_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
message_box.send_keys("<Your message>")

# Send the message
driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()
