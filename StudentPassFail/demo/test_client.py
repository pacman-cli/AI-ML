import urllib.request
import json
import sys

# URL of the Spring Boot application (HTTP, not HTTPS)
url = "http://localhost:8081/predict"

# Data to send
data = {
    "hours_studied": 5,
    "attendance": 90
}

print(f"Sending POST request to {url}...")
print(f"Data: {json.dumps(data, indent=2)}")

try:
    json_data = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(url, data=json_data, headers={'Content-Type': 'application/json'}, method='POST')

    with urllib.request.urlopen(req) as response:
        status_code = response.getcode()
        body = response.read().decode('utf-8')

        print(f"\nStatus Code: {status_code}")
        print("Response Body:")
        print(body)

        if status_code == 200:
            print("\n✅ SUCCESS! The API is working correctly.")
        else:
            print(f"\n❌ FAILED. Server returned status {status_code}")

except urllib.error.HTTPError as e:
    print(f"\n❌ HTTP Error: {e.code} {e.reason}")
    try:
        print(e.read().decode('utf-8'))
    except:
        pass
except urllib.error.URLError as e:
    print(f"\n❌ Connection Error: {e.reason}")
    print("Make sure the server is running on http://localhost:8081")
except Exception as e:
    print(f"\n❌ An error occurred: {e}")
