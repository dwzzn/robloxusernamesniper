import random
import string
import time
import requests

def generate_username(length=4):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def is_username_available(username):
    url = f"https://users.roblox.com/v1/usernames/validate?request.username={username}&request.birthday=2000-01-01"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get("code") == 0  # 0 = valid
    except Exception as e:
        print(f"Error checking username '{username}': {e}")
    return False

while True:
    username = generate_username()
    print(f"Checking: {username}")
    if is_username_available(username):
        print(f"Available: {username}")
        break
