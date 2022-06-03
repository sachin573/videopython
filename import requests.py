import requests
city ='new york'
api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(city)
response = requests.get(api_url, headers={'X-Api-Key': 'P3bNLRZlg24B7Ny7GAX+sA==wHDzHG8vClUw9ZWl'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)