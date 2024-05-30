$safeAdminPassword = ConvertTo-SecureString -string @@{WIN_VM_CRED.secret}@@ –asplaintext –force 
$safeAdminPassword
$netbiosArray = "@@{DOMAIN_NAME}@@".split(".")
$netbios = $netbiosArray[0]
Write-Host "NetBios" + $netbios
#Install-ADDSForest -CreateDnsDelegation:$false -DatabasePath "C:\Windows\NTDS" -DomainMode "Default" -DomainName "@@{DOMAIN_NAME}@@" -DomainNetbiosName "@@{DOMAIN_NAME}@@" -ForestMode "Default" -InstallDns:$true -LogPath "C:\Windows\NTDS" -NoRebootOnCompletion:$false -SysvolPath "C:\Windows\SYSVOL" -Force:$true -SafeModeAdministratorPassword $safeAdminPassword
#Install-ADDSForest -CreateDnsDelegation:$false -DatabasePath "C:\Windows\NTDS" -DomainMode "Default" -DomainName "@@{DOMAIN_NAME}@@" -DomainNetbiosName "ntnxlab" -ForestMode "Default" -InstallDns:$true -LogPath "C:\Windows\NTDS" -SysvolPath "C:\Windows\SYSVOL" -Force:$true -SafeModeAdministratorPassword $safeAdminPassword
Install-ADDSForest -CreateDnsDelegation:$false -DatabasePath "C:\Windows\NTDS" -DomainMode "Default" -DomainName "@@{DOMAIN_NAME}@@" -DomainNetbiosName $netbios -ForestMode "Default" -InstallDns:$true -LogPath "C:\Windows\NTDS" -SysvolPath "C:\Windows\SYSVOL" -Force:$true -SafeModeAdministratorPassword $safeAdminPassword