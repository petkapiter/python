#!/usr/bin/env python
mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
cisco = []
for change in mac:
    cisco.append(change.replace(":", "."))
print (cisco)
