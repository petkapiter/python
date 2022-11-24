ip = input("Введите ip: ")
octets = ip.split(".")
last = int(octets[0])
print (last)
if ip == "255.255.255.255":
    print("local broadcast")
elif ip == "0.0.0.0":
    print("unassigned")
elif 1 <= last <= 223:
    print("unicast")
elif 224 <= last <= 239:
    print("multicast")
else:
    print("unused")