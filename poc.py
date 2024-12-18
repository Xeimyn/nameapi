import sys

name:str =  sys.argv[1].lower() if len(sys.argv) > 1 else input("Enter username to check > ").lower()

import requests

print(f"Checking {name}...\n")

# Social media platforms
# Discord ✔
# Telegram ✔
# Facebook ✔
# Twitter ✔
# Instagram ✔
# Youtube ✔
# Github ✔
# Reddit ✔
# Twitch ✔
# Tiktok ✔
# Threads ✔
# Patreon ✔
# Snapchat ✔
# Kick ⚠
# Steam ⚠

# TRUE == AVAILABLE

# # Check if name is taken on Discord
# discord = not bool(requests.post(f"https://discord.com/api/v9/unique-username/username-attempt-unauthed",
# 					headers={"Content-Type":"application/json"},
# 					json={"username":name}).json()["taken"])
# print(f"Discord: {discord}")

# # Check if name is taken on Telegram
# telegram = bool(f"{name} is taken" not in requests.get(f"https://fragment.com/username/{name}").text.lower())
# print(f"Telegram: {not telegram}")

# # Check if name is taken on Facebook
# facebook = bool("This content isn't available right now" in requests.get(f"https://facebook.com/{name}?locale=en_US").text)
# print(f"Facebook: {facebook}")

# # # Check if name is taken on Twitter
# twitter = bool(requests.get(f"https://api.x.com/i/users/username_available.json?username={name}").json()["valid"])
# print(f"Twitter: {twitter}")

# # Check if name is taken on Instagram
# try:
# 	instagram = requests.post(f"https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/",
# 						headers={"Content-Type":"application/x-www-form-urlencoded","X-CSRFToken":"en"},
# 						data={"username":name}
# 						).json()["errors"]["username"][0]["code"] == "username_is_taken"
# except KeyError:
# 	instagram = True
# else:
# 	instagram = False
# print(f"Instagram: {instagram}")

# # Check if name is taken on Youtube
# youtube = bool(requests.get(f"https://youtube.com/@{name}").status_code == 404)
# print(f"Youtube: {youtube}")

# # Check if name is taken on Github
# github = bool(requests.get(f"https://github.com/{name}").status_code == 404)
# print(f"Github: {github}")

# # Check if name is taken on Reddit
# reddit = bool(requests.get(f"https://www.reddit.com/api/username_available.json?user={name}").text == "true")
# print(f"Reddit: {reddit}")

# # Check if name is taken on Twitch
# twitch = bool(requests.get(f"https://passport.twitch.tv/usernames/{name}").status_code == 204)
# print(f"Twitch: {twitch}")

# # Check if name is taken on Tiktok
# tiktok = bool("nickNameModifyTime" not in requests.get(f"https://www.tiktok.com/@{name}?lang=en&").text)
# print(f"Tiktok: {tiktok}")

# # Check if name is taken on Threads
# threads = bool("on Threads</title>" not in requests.get(f"https://www.threads.net/@{name}").text)
# print(f"Threads: {threads}")

# Check if name is taken on Patreon
# patreon = bool(requests.get(f"https://patreon.com/c/{name}").status_code == 404)
# print(f"Patreon: {patreon}")

# Check if name is taken on snapchat
# headers = {
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate, sdch, br",
#     "Accept-Language": "en-US,en;q=0.8",
#     "Referer": "https://example.com",
# }
# snapchat = bool(requests.get(f"https://snapchat.com/add/{name}",headers=headers).status_code == 404)
# print(f"Snapchat: {snapchat}")

# Check if name is taken on Kick
# TODO | No worky
# kick = requests.post(f"https://kick.com/api/v2/signup/verify/username",data={"username":name})
# # print(f"Kick: {kick.headers}")
# print(f"Kick: {kick.text}")

# Check if name is taken on Steam
# TODO | No worky
# steam = requests.get(f"https://steamcommunity.com/id/{name}")
# print(f"Steam: {steam.status_code}")
