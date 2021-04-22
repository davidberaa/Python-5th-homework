# task 1

# import requests
#
# response = requests.get("https://www.mes.gov.ge/index.php?lang=geo")
#
# a = open("mes.gov.ge", "w")
# a.write(str(response.content))
#
# print(str(response.content).count("განათლება"))



# task 2

# import requests
#
# response1 = requests.get("https://httpbin.org/image/jpeg")
# a = open("image1.png", "wb")
# a.write(response1.content)
# a.close()
#
# response2 = requests.get("https://httpbin.org/image/png")
# b = open("image2.png", "wb")
# b.write(response2.content)
# b.close()
#
# response3 = requests.get("https://httpbin.org/image/svg")
# c = open("image3.png", "wb")
# c.write(response3.content)
# c.close()
#
# response4 = requests.get("https://httpbin.org/image/webp")
# d = open("image4.png", "wb")
# d.write(response4.content)
# d.close()



# task 3

import requests

response = requests.get("https://httpbin.org/ip")

a = open("my-ip.txt", "w")
for i in str(response.content):
    if i.isnumeric() or i == ".":
        a.write(str(i))
