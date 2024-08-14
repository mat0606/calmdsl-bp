network_ip_prefix = "@@{Network_IP_Prefix}@@"

network_ip_prefix_array = [] 
network_ip_prefix_array = network_ip_prefix.split("/")
print ("network_ip=" + network_ip_prefix_array[0])
print ("network_ip_prefix=" + network_ip_prefix_array[1])