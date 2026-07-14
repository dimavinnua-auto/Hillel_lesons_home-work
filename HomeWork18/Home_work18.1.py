

import requests

BASE_URL = "https://images-api.nasa.gov"

# Пошук зображень
search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",  # пошуковий запит
    "media_type": "image",  # тільки зображення
    "page_size": 20  # щоб було з чого вибрати
}

# Отримання файлів по nasa_id
asset_url_template = f"{BASE_URL}/asset/{{nasa_id}}"

response = requests.get(search_url, params=search_params)
data = response.json()

items = data["collection"]["items"]
nasa_ids = [item["data"][0]["nasa_id"] for item in items[:2]]
print("Знайшли",nasa_ids)

image_url = []
for nasa_id in nasa_ids:
    asset_url = f"{BASE_URL}/asset/{nasa_id}"
    asset_response = requests.get(asset_url)
    asset_data = asset_response.json()
    assets = asset_data["collection"]["items"]
    for items in assets:
        href = items["href"]
        if href.lower().startswith(".jpg"):
            image_url.append(href)
            break
print("JPG URL:", image_url)

filenames = ["mars_photo1.jpg", "mars_photo2.jpg"]
for i, url in enumerate(image_url[:2]):
    img_response = requests.get(url)
    with open(filenames[i], "wb") as f:
        f.write(img_response.content)
    print(f"{filenames[i]} збережено!")
