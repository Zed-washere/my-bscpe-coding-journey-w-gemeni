#Once you've installed requests, try to write a scrurlt called site_checker.py that does this:
#Ask the user for a URL (or use sys.argv[1]).
#Use requests.get(url) to "knock on the door" of that website.
#Print the status code.
#Bonus: If the status code is 200, print "✅ Website is Healthy!"; otherwise, print "❌ Website might be down!"

import sys
import requests


try:
    url = sys.argv[1]
except IndexError:
    print(f"error please provide url to check ping.")
    print(f"usage: python site_checker.py <URL>")
    sys.exit(1)


try:
    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    response = requests.get(url, timeout=10)

    site_status = response.status_code

    print(f"Status Code: {site_status} for website {url} \n")

    if site_status == 200:
        print(f"Website is healthy and online!: \n\n")
    else:
        print(f"Webiste is error")


    try:
        data = response.json()
        print(f"{data}\n\n")
        print(f"filtered data: city: {data['city']}, country: {data['country']}")
    except ValueError:
        pass

    

except requests.exceptions.ConnectionError:
    print("Error: The site doesn't exist or the DNS failed.")
    print("URL probably not real. \n")
    print(" :/ ")
    sys.exit(1)

except requests.exceptions.Timeout:
    print("Error: The server took too long to respond.")
    sys.exit(1)

except requests.exceptions.HTTPError as err:
    print(f"Error: Site exists but returned an error: {err}")
    sys.exit(1)

except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)
    