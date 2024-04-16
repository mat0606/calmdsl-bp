Enable-WSManCredSSP -Role Server -Force

$domainString = "@@{DomainName}@@"
$splitDomainString = $domainString.split(".")

$domainPath = "DC=" + $splitDomainString[0] + ",DC=" + $splitDomainString[1] 

New-AdUser -Name "@@{mailNickName}@@" -Path $domainPath -UserPrincipalName "@@{mailNickName}@@@@@{DomainName}@@" -DisplayName "@@{displayName}@@" -Enabled $True -ChangePasswordAtLogon $True -AccountPassword (ConvertTo-SecureString "@@{Password}@@" -AsPlainText -force) -passThru