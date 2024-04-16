cred_win_uuid = "{}".format(str(uuid.uuid4())) #WIN_CRED Creential uuid
cred_win_domain_uuid = "{}".format(str(uuid.uuid4())) #WIN_DOMAIN_CRED Creential uuid
win_subtrate_uuid = "{}".format(str(uuid.uuid4()))

ip_str = "@"+"@" + "{platform.status.resources.nic_list[0].ip_endpoint_list[0].ip}"+ "@"+"@"

windows_guest_customization_data = {
# "cloud_init": null,
  "type": "",
  "sysprep": {
    "is_domain": False,
    "install_type": "PREPARED",
 #   "domain_credential_reference": null,
    "domain": "",
    "dns_ip": "",
    "dns_search_path": "",
    "unattend_xml": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<unattend xmlns=\"urn:schemas-microsoft-com:unattend\">\n   <settings pass=\"specialize\">\n      <component xmlns:wcm=\"http://schemas.microsoft.com/WMIConfig/2002/State\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" name=\"Microsoft-Windows-Shell-Setup\" processorArchitecture=\"amd64\" publicKeyToken=\"31bf3856ad364e35\" language=\"neutral\" versionScope=\"nonSxS\">\n         <ComputerName>@@{name}@@</ComputerName>\n         <RegisteredOrganization>Nutanix</RegisteredOrganization>\n         <RegisteredOwner>Acropolis</RegisteredOwner>\n         <TimeZone>UTC</TimeZone>\n      </component>\n      <component xmlns=\"\" name=\"Microsoft-Windows-TerminalServices-LocalSessionManager\" publicKeyToken=\"31bf3856ad364e35\" language=\"neutral\" versionScope=\"nonSxS\" processorArchitecture=\"amd64\">\n         <fDenyTSConnections>false</fDenyTSConnections>\n      </component>\n      <component xmlns=\"\" name=\"Microsoft-Windows-TerminalServices-RDP-WinStationExtensions\" publicKeyToken=\"31bf3856ad364e35\" language=\"neutral\" versionScope=\"nonSxS\" processorArchitecture=\"amd64\">\n         <UserAuthentication>0</UserAuthentication>\n      </component>\n      <component xmlns:wcm=\"http://schemas.microsoft.com/WMIConfig/2002/State\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" name=\"Networking-MPSSVC-Svc\" processorArchitecture=\"amd64\" publicKeyToken=\"31bf3856ad364e35\" language=\"neutral\" versionScope=\"nonSxS\">\n         <FirewallGroups>\n            <FirewallGroup wcm:action=\"add\" wcm:keyValue=\"RemoteDesktop\">\n               <Active>true</Active>\n               <Profile>all</Profile>\n               <Group>@FirewallAPI.dll,-28752</Group>\n            </FirewallGroup>\n         </FirewallGroups>\n      </component>\n   </settings>\n   <settings pass=\"oobeSystem\">\n      <component xmlns:wcm=\"http://schemas.microsoft.com/WMIConfig/2002/State\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" name=\"Microsoft-Windows-Shell-Setup\" processorArchitecture=\"amd64\" publicKeyToken=\"31bf3856ad364e35\" language=\"neutral\" versionScope=\"nonSxS\">\n         <UserAccounts>\n            <AdministratorPassword>\n               <Value>@@{WIN_VM_CRED.secret}@@</Value>\n               <PlainText>true</PlainText>\n            </AdministratorPassword>\n         </UserAccounts>\n         <AutoLogon>\n            <Password>\n               <Value>@@{WIN_VM_CRED.secret}@@</Value>\n               <PlainText>true</PlainText>\n            </Password>\n            <Enabled>true</Enabled>\n            <Username>Administrator</Username>\n         </AutoLogon>\n         <FirstLogonCommands>\n            <SynchronousCommand wcm:action=\"add\">\n               <CommandLine>cmd.exe /c netsh firewall add portopening TCP 5985 \"Port 5985\"</CommandLine>\n               <Description>Win RM port open</Description>\n               <Order>1</Order>\n               <RequiresUserInput>true</RequiresUserInput>\n            </SynchronousCommand>\n            <SynchronousCommand wcm:action=\"add\">\n               <CommandLine>powershell -Command \"Enable-PSRemoting -SkipNetworkProfileCheck -Force\"</CommandLine>\n               <Description>Enable PS-Remoting</Description>\n               <Order>2</Order>\n               <RequiresUserInput>true</RequiresUserInput>\n            </SynchronousCommand>\n            <SynchronousCommand wcm:action=\"add\">\n               <CommandLine>powershell -Command \"Set-ExecutionPolicy -ExecutionPolicy RemoteSigned\"</CommandLine>\n               <Description>Enable Remote-Signing</Description>\n               <Order>3</Order>\n               <RequiresUserInput>false</RequiresUserInput>\n            </SynchronousCommand>\n         </FirstLogonCommands>\n         <OOBE>\n            <HideEULAPage>true</HideEULAPage>\n            <SkipMachineOOBE>true</SkipMachineOOBE>\n         </OOBE>\n      </component>\n      <component xmlns:wcm=\"http://schemas.microsoft.com/WMIConfig/2002/State\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" name=\"Microsoft-Windows-International-Core\" processorArchitecture=\"amd64\" publicKeyToken=\"31bf3856ad364e35\" language=\"neutral\" versionScope=\"nonSxS\">\n         <InputLocale>en-US</InputLocale>\n         <SystemLocale>en-US</SystemLocale>\n         <UILanguageFallback>en-us</UILanguageFallback>\n         <UILanguage>en-US</UILanguage>\n         <UserLocale>en-US</UserLocale>\n      </component>\n   </settings>\n</unattend>",
    "type": ""
  }
}

WIN_SPEC = {
  "description": "",
  "action_list": [],
#  "message_list": [],
  "uuid": win_subtrate_uuid,
 # "state": "ACTIVE",
  "readiness_probe": {
    "connection_type": "POWERSHELL",
    "retries": "5",
    "connection_protocol": "http",
    "disable_readiness_probe": True,
   # "address": ip_str,
    "delay_secs": "0",
    "connection_port": 5985,
    "login_credential_local_reference": {
      "kind": "app_credential",
      "name": "WIN_VM_CRED",
      "uuid": cred_win_uuid
     }
  },
  "editables": {
  },
  "os_type": "Windows",
  "type": "AHV_VM",
  "create_spec": {
    "name": "vm-@@{calm_array_index}@@-@@{calm_time}@@",
    "categories": "",
  #  "availability_zone_reference": null,
  #  "backup_policy": null,
    "type": "",
    "cluster_reference": {
      "kind": "cluster",
      "type": "",
      "name": "@@{Cluster_Name}@@", #"SGNTNXWLPE_AZ01",
      "uuid": "@@{cluster_uuid}@@" #"0005e085-b472-5a84-1ebd-ac1f6b3b4778"
    },
    "resources": {
      "nic_list": [
      {
        "nic_type": "NORMAL_NIC",
   #     "vpc_reference": null,
        "ip_endpoint_list": [],
   #     "network_function_chain_reference": null,
        "network_function_nic_type": "INGRESS",
        "mac_address": "",
        "subnet_reference": {
          "kind": "subnet",
          "type": "",
          "name": "@@{PE_Network}@@",
          "uuid": "@@{pe_network_UUID}@@"#"98069d20-b800-49c7-a98a-15b883bebe79"
        },
        "type": ""
      }],
     #  "parent_reference": null,
     #  "guest_tools": null,
      "num_vcpus_per_socket": 1,
      "num_sockets": 2,
      "serial_port_list": [],
      "gpu_list": [],
      "memory_size_mib": 2048,
      "power_state": "ON",
      "hardware_clock_timezone": "",
      "guest_customization": windows_guest_customization_data,
      "type": "",
      "account_uuid": "@@{cluster_account_reference_UUID}@@", #"7862442b-7d23-4f7a-811e-578434b861f5",
      "boot_config": {
        "boot_device": {
          "type": "",
          "disk_address": {
            "adapter_type": "SCSI",
            "device_index": 0,
            "type": ""
          }
        }
      },
      "type": "",
     # "boot_type": "LEGACY",
     # "mac_address": ""
      "disk_list": [
      {
        "data_source_reference": {
          "kind": "image",
          "type": "",
          "name": "@@{win_env_image}@@", #"windows-2019-calm-template.qcow2",
          "uuid": "@@{win_image_UUID}@@", #"f95344b0-cc32-4008-90f7-2e060cbdf2bf"
        },
        "type": "",
        "disk_size_mib": 0,
        "device_properties": {
          "type": "",
          "device_type": "DISK",
          "disk_address": {
            "adapter_type": "SCSI",
            "device_index": 0,
            "type": ""
          }
        }
      }]
    }
  },
  "variable_list": [],
  "name": "Untitled"
}  
    

print "WIN_SPEC={}".format(WIN_SPEC)
print "cred_win_uuid={}".format(cred_win_uuid)
print "cred_win_domain_uuid={}".format(cred_win_domain_uuid)
print "win_subtrate_uuid={}".format(win_subtrate_uuid)