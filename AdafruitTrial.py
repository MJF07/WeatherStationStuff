

import requests
AIO_USERNAME = "MJF07"
ADAFRUIT_AIO_KEY = "aio_Fuhr25ZCn1t3KN45NuuVyuAuC7y5"

# The feed    name you want to send data to (replace 'test-data' with your feed name)

FEED_NAME = "feed1"
FEED_NAME2 = "feed2"
FEED_NAME3 = "feed3"
FEED_NAME4 = "feed4"
FEED_NAME5 = "feed5"
FEED_NAME6 = "feed6"
# Adafruit IO endpoint URL

url = f'https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{FEED_NAME}/data'
url2 = f'https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{FEED_NAME2}/data'
url3 = f'https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{FEED_NAME3}/data'
url4 = f'https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{FEED_NAME4}/data'
url5 = f'https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{FEED_NAME5}/data'
url6 = f'https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{FEED_NAME6}/data'
# Data to send

data = {

"value":55 # Replace with the value you want to send

}


data2 = {

"value": 10 # Replace with the value you want to send

}


data3 = {

"value": 10 # Replace with the value you want to send

}

data4 = {

"value":5 # Replace with the value you want to send

}

data5= {

"value":55 # Replace with the value you want to send

}

data6= {

"value":9 # Replace with the value you want to send

}

# Headers for authentication

headers = {

'X-AIO-Key': ADAFRUIT_AIO_KEY,

'Content-Type': 'application/json'

}

# Send a POST request to Adafruit IO

response = requests.post(url, json=data, headers=headers)
response2 = requests.post(url2, json=data2, headers=headers)
response3 = requests.post(url3, json=data3, headers=headers)
response4 = requests.post(url4, json=data3, headers=headers)
response5 = requests.post(url5, json=data3, headers=headers)
response6 = requests.post(url5, json=data3, headers=headers)
# Check the response

if response.status_code == 200:
    print("Data successfully sent to Adafruit IO.")

else:
    print("Failed to send data. Status code: {response.status_code}, Error: {response.text}")


get_info = requests.get(url2, headers=headers)
data=get_info.json() #convert the response to JSON
print("Latest data")
for entry in data:
    print (f"Value:{entry['value']} | Time (24h):{entry['created_at']}")


