import requests

BASE_URL = "http://127.0.0.1:5000/"
image_path = r"C:\Users\ASUS\Desktop\mer.jpg"


def upload_image(file_path):
    with open(file_path, "rb") as f:
        response = requests.post(f"{BASE_URL}upload", files={"image": f})
        print("Upload status:", response.status_code)
    return {"response": response, "url": f"{BASE_URL}upload/mer.jpg"}


def get_image(file_name):
    response = requests.get(f"{BASE_URL}upload/mer.jpg")
    print("Get status:", response.status_code)
    return response


def delete_image(file_name):
    response = requests.delete(f"{BASE_URL}upload/mer.jpg")
    print("Delete status:", response.status_code)
    return response


result = upload_image(image_path)
print(result["response"].status_code)
print(result["url"])