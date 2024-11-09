
# Import the required module from the fyers_apiv3 package
from fyers_apiv3 import fyersModel

# Replace these values with your actual API credentials
client_id = 'GCEG4OMS1B-100'
secret_key = 'P09QMZT9GH'
redirect_uri = 'https://www.google.com/'
user_name = 'XS08415'

totp_key = 'RU376TSN3LAENIQZT3PNB2HWWYORMSNF'

response_type = "code"  
state = "sample_state"

# Create a session model with the provided credentials
session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type=response_type
)

# Generate the auth code using the session model
response = session.generate_authcode()

# Print the auth code received in the response
print(response)







# link = response

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
# import pyotp as tp

# driver = webdriver.Chrome()
# driver.get(link)

# time.sleep(20)
# login_with_client_id_x_path = '//*[@id="login_client_id"]'
# elem = driver.find_element(By.XPATH , login_with_client_id_x_path)
# elem.click()
# time.sleep(1)
# client_id_input_x_path = '//*[@id="fy_client_id"]'
# elem2 = driver.find_element(By.XPATH , client_id_input_x_path)
# elem2.send_keys("XS08415")
# time.sleep(10)
# elem2.send_keys(Keys.RETURN)
# time.sleep(20)
# driver.close()

# t = tp.TOTP(totp_key).now()

# driver.find_element(By.XPATH , )

# driver.close()


