Import-Module ADFSToolbox
#$fqdn = [System.Net.Dns]::GetHostByName(($env:computerName)) | FL HostName | Out-String | %{ "{0}" -f $_.Split(':')[1].Trim() };
#$filename = "C:\$fdqn.pfx"

#Export-AdfsDiagnosticsFile -ServerNames @("$fqdn")
Export-AdfsDiagnosticsFile