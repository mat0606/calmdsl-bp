Enable-WSManCredSSP -Role Server -Force

$domainString = "@@{DOMAIN_NAME}@@"
$splitDomainString = $domainString.split(".")

$domainPath = "DC=" + $splitDomainString[0] + ",DC=" + $splitDomainString[1] 

for (($i = 0); $i -lt 10; $i++){
  $currentCount = $i + 1
  $userNameProjAdm = "@@{USER_CRED.username}@@" + $currentCount + "projadm"
  $userPrincipalNameProjAdm = "@@{USER_CRED.username}@@" + $currentCount + "projadm" + "@@{DOMAIN_NAME}@@"
  $userNameDeveloper = "@@{USER_CRED.username}@@" + $currentCount + "developer"
  $userPrincipalNameDeveloper = "@@{USER_CRED.username}@@" + $currentCount + "developer"
#  New-AdUser -Name $userNameProjAdm -Path $domainPath -UserPrincipalName $userPrincipalNameProjAdm -DisplayName $userNameProjAdm -Enabled $True -CannotChangePassword $True -PasswordNeverExpires $True -AccountPassword (ConvertTo-SecureString "@@{USER_CRED.secret}@@" -AsPlainText -force) -passThru
  New-AdUser -Name $userNameProjAdm -UserPrincipalName $userPrincipalNameProjAdm -DisplayName $userNameProjAdm -Enabled $True -CannotChangePassword $True -PasswordNeverExpires $True -AccountPassword (ConvertTo-SecureString "@@{USER_CRED.secret}@@" -AsPlainText -force) -passThru
#  New-AdUser -Name $userNameDeveloper -Path $domainPath -UserPrincipalName $userPrincipalNameDeveloper -DisplayName $userNameDeveloper -Enabled $True -CannotChangePassword $True -PasswordNeverExpires $True -AccountPassword (ConvertTo-SecureString "@@{USER_CRED.secret}@@" -AsPlainText -force) -passThru
  New-AdUser -Name $userNameDeveloper -UserPrincipalName $userPrincipalNameDeveloper -DisplayName $userNameDeveloper -Enabled $True -CannotChangePassword $True -PasswordNeverExpires $True -AccountPassword (ConvertTo-SecureString "@@{USER_CRED.secret}@@" -AsPlainText -force) -passThru
}