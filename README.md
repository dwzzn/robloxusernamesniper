# roblox username sniper (4 characters, can be changed)
**REQUIRED:** python v3.12.1 due to **import requests**

This code looks for usernames existing in the "https://users.roblox.com/v1/usernames" section which contains all existing usernames..
It checks if each username is valid and returns "Available" via return data.get("code") == 0
I removed the ratelimiter which will spam roblox servers, add **timer.Sleep(in seconds here)** to avoid this
