ip = "192.168.3.1"
octets = ip.split('.')
ip_result = '''
    IP address:
    {0:<8} {1:<8} {2:<8} {3:<8} 
    {0:08b} {1:08b} {2:08b} {3:08b}
    '''
print(ip_result.format(int(octets[0]), int(octets[1]), int(octets[2]), int(octets[3])))