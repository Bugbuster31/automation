import requests

# Replace 'YOUR_API_KEY' with your actual Flickr API key
api_key = 'd317af65f5d9ca6dcfbab3f4046156cd'
base_url = 'https://api.flickr.com/services/rest/'

# Example for flickr.photos.getPopular
popular_photos_params = {
    'method': 'flickr.photos.getPopular',
    'api_key': api_key,
    'user_id': '199812832@N05',
}

response = requests.get(base_url, params=popular_photos_params)
print(response)
data = response.text
print(data)