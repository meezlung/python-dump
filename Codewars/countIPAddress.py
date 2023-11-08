def ip_to_int(ip_address):
    parts = ip_address.split('.')
    return int(parts[0]) * 256**3 + int(parts[1]) * 256**2 + int(parts[2]) * 256 + int(parts[3])

def ips_between(ip1, ip2):
    start_ip = ip_to_int(ip1)
    end_ip = ip_to_int(ip2)
    
    return end_ip - start_ip


print(ips_between("10.0.0.0", "10.0.0.50"))
# * With input "10.0.0.0", "10.0.0.50"  => return   50 
# * With input "10.0.0.0", "10.0.1.0"   => return  256 
# * With input "20.0.0.10", "20.0.1.0"  => return  246