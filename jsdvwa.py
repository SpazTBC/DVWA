#!/usr/bin/python3

# DVWA JAVASCRIPT VULNERABILITY

import hashlib
import requests
import codecs

url = "http://localhost/vulnerabilities/javascript/"

# Headers
headers = {
    #Enter Your Own Headers (To Get These Use Burp Suite)
    #Example Below

    #"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0",
    #"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    #"Accept-Language": "en-US,en;q=0.5",
    #"Accept-Encoding": "gzip, deflate, br",
    #"Referer": "http://localhost/vulnerabilities/javascript/",
    #"Content-Type": "application/x-www-form-urlencoded",
    #"Origin": "http://localhost",
    #"DNT": "1",
    #"Connection": "close",
    #"Cookie": "PHPSESSID=ge2i5ou0n58jrdsgl2gkc1u6p0; security=low",
    #"Upgrade-Insecure-Requests": "1"
}

# Encoding Process
u_input = input("Enter a word: ")
rot13_encoded_word = codecs.encode(u_input, 'rot_13') # Rot-13 First
md5_sum = hashlib.md5(rot13_encoded_word.encode()).hexdigest() # Get the MD5 Sum of the Rot-13 Word

# Ask for Phrase
phrase = input("Enter a phrase: ")

# Send Request
site_input = input("Would You Like To Send This As A Request? (yes/no): ")

if site_input.lower() == "yes":
    data = {"token": md5_sum, "phrase": phrase, "send": "Submit"} # Submit the Phrase we gave the code, and give the sum that was generated.
    response = requests.post(url, headers=headers, data=data)
    print("HTTP Status Code:", response.status_code)
    
    # Check if the response contains "Well done!"
    if "Well done!" in response.text:
        print("Success! Well done!") # If you did it correctly you'll get this
    else:
        print("Request failed.") # If you didn't do it correctly, this will be the result.
else:
    print("Request not sent.")

# Summary
final_input = input("Would You Like A Summary Of What You Did? (yes/no): ")

if final_input.lower() == "yes":
    print("TOTAL SUMMARY:")
    print("Plain Text Word:", u_input)
    print("Rot-13 Encoded Word:", rot13_encoded_word)
    print("MD5 Sum:", md5_sum)
    print("Phrase:", phrase)
    print("\nThank you for using our program!")
else:
    print("Thank you for using our program!")
