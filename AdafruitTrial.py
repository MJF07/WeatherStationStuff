ADAFRUIT_AIO_USERNAME = "MJF07"
ADAFRUIT_AIO_KEY      = "aio_sZbV40vIXJPUVzXFxSFn9Q8lfhSm"
FEED_NAME="1"


#Adafruit IO credentials

AIO_USERNAME = 'MJF07' # Replace with your Adafruit IO username

AIO_KEY = 'io_sZbV40vIXJPUVzXFxSFn9Q8lfhSm' # Replace with your Adafruit IO key

# The feed name you want to send data to (replace 'test-data' with your feed name)

FEED_NAME = '1'

# Adafruit IO endpoint URL

url = f'https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{FEED_NAME}/data'

# Data to send

data = {

"value": 42 # Replace with the value you want to send

}

# Headers for authentication

headers = {

'X-AIO-Key': AIO_KEY,

'Content-Type': 'application/json'

}

# Send a POST request to Adafruit IO

response = requests.post(url, json=data, headers=headers)

# Check the response

if response.status_code == 201:
    print("Data successfully sent to Adafruit IO.")

else:
    print(f"Failed to send data. Status code: {response.status_code}, Error: {response.text}")

