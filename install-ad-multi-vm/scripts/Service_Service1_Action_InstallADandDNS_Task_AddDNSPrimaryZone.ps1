Add-DnsServerPrimaryZone -NetworkID @@{subnet}@@ -ZoneFile “@@{platform.status.resources.nic_list[0].ip_endpoint_list[0].ip}@@.in-addr.arpa.dns”
Add-DnsServerForwarder -IPAddress 8.8.8.8 -PassThru
#Test-DnsServer -IPAddress @@{platform.status.resources.nic_list[0].ip_endpoint_list[0].ip}@@ -ZoneName "ntnx.local"
Test-DnsServer -IPAddress @@{platform.status.resources.nic_list[0].ip_endpoint_list[0].ip}@@ -ZoneName "@@{DOMAIN_NAME}@@"