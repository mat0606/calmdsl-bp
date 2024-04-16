network_ip_prefix = "@@{Network_IP_Prefix}@@"

network_ip_prefix_array = [] 
network_ip_prefix_array = network_ip_prefix.split("/")
print "network_ip={0}".format(network_ip_prefix_array[0])
print "network_ip_prefix={0}".format(network_ip_prefix_array[1])