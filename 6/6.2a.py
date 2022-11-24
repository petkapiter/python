ip = input("Введите ip: ")
print(ip)
octets = ip.split(".")
correct_ip = True
if len(octets) != 4:
    correct_ip = False
else:
    for octet in octets:
        if not (octet.isdigit() and int(octet) in range(256)):
            correct_ip = False
            break
if not correct_ip:
    print("Неверный IP")
else:
    first = int(octets[0])
    if 1 <= first <= 223:
        print("unicast")
    elif 224 <= first <= 239:
        rint("multicat")
    elif ip == "255.255.255.255":
        print("local broadcast")
    elif ip == "0.0.0.0":
        print("unassigned")
    else:
        print("unused")