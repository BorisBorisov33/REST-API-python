import requests

# here I get the data
api_url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(api_url)
print(response.json())

# here I am uploading an image
images = {'image': open('C:/Users/as/Desktop/REST-API-python/test_image.png', 'rb')}
requests.post(api_url, files=images)
