import requests

url = "https://api.github.com"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("GitHub API Info")
        print("User URL:", data["current_user_url"])
        print("Repositories URL:", data["repository_url"])

    else:
        print("Failed with status code:", response.status_code)

except Exception as e:
    print("Error:", e)