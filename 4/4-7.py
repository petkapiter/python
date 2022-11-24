mac = "AAAA:BBBB:CCCC"
mac2 = '{:b}'.format((int(mac.replace(":", ""), 16)))
print(mac2)