import requests

url = "https://api.github.com"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Save data to file
        with open("api_output.txt", "w") as file:
            file.write(str(data))

        print("API data saved successfully!")

    else:
        print("Failed with status code:", response.status_code)

except Exception as e:
    print("Error:", e)