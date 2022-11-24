command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
command1_change = set(command1.split()[-1].split(","))
command2_change = set(command2.split()[-1].split(","))
result = sorted(command1_change.intersection(command2_change))
print(result)