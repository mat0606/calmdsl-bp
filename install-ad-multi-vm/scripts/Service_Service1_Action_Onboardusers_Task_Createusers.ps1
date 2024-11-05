Enable-WSManCredSSP -Role Server -Force

$domainString = "@@{DOMAIN_NAME}@@"
$splitDomainString = $domainString.split(".")

$domainPath = "DC=" + $splitDomainString[0] + ",DC=" + $splitDomainString[1] 

New-ADGroup -Name “SSPProjectAdminGp” -Description “This is a group for project admin role” -GroupScope Universal -ManagedBy “@@{WIN_VM_CRED.username}@@”
New-ADGroup -Name “SSPDeveloperGp” -Description “This is a group for developer role” -GroupScope Universal -ManagedBy “@@{WIN_VM_CRED.username}@@”
New-ADGroup -Name “SSPBPDeveloperGp” -Description “This is a group for BP developer role” -GroupScope Universal -ManagedBy “@@{WIN_VM_CRED.username}@@”
New-ADGroup -Name “NKPSuperAdminGp” -Description “This is a group for NKP Super Admin role” -GroupScope Universal -ManagedBy “@@{WIN_VM_CRED.username}@@”
New-ADGroup -Name “NKPProjectAdminGp” -Description “This is a group for NKP Project Admin role” -GroupScope Universal -ManagedBy “@@{WIN_VM_CRED.username}@@”
New-ADGroup -Name “NKPWorkspaceAdminGp” -Description “This is a group for NKP Workspace Admin role” -GroupScope Universal -ManagedBy “@@{WIN_VM_CRED.username}@@”

for (($i = 0); $i -lt 20; $i++){
  $currentCount = $i + 1
  $userNameProjAdm = "@@{USER_CRED.username}@@" + $currentCount + "projadm"
  $userPrincipalNameProjAdm = "@@{USER_CRED.username}@@" + $currentCount + "projadm" 
  $userNameDeveloper = "@@{USER_CRED.username}@@" + $currentCount + "developer"
  $userPrincipalNameDeveloper = "@@{USER_CRED.username}@@" + $currentCount + "developer"
  $userNameBPDeveloper = "@@{USER_CRED.username}@@" + $currentCount + "BPdeveloper"
  $userPrincipalNameBPDeveloper = "@@{USER_CRED.username}@@" + $currentCount + "BPdeveloper"
  $userNameNKPSuperAdmin = "nkp" + $currentCount + "SuperAdmin"
  $userPrincipalNameNKPSuperAdmin = "nkp" + $currentCount + "SuperAdmin"
  $userNameNKPProjectAdmin = "nkp" + $currentCount + "ProjectAdmin"
  $userPrincipalNameNKPProjectAdmin = "nkp" + $currentCount + "ProjectAdmin"
  $userNameNKPWorkspaceAdmin = "nkp" + $currentCount + "WorkspaceAdmin"
  $userPrincipalNameNKPWorkspaceAdmin = "nkp" + $currentCount + "WorkspaceAdmin"
 
#  New-AdUser -Name $userNameProjAdm -Path $domainPath -UserPrincipalName $userPrincipalNameProjAdm -DisplayName $userNameProjAdm -Enabled $True -CannotChangePassword $True -PasswordNeverExpires $True -AccountPassword (ConvertTo-SecureString "@@{USER_CRED.secret}@@" -AsPlainText -force) -passThru
  New-AdUser -Name $userNameProjAdm -UserPrincipalName $userPrincipalNameProjAdm -DisplayName $userNameProjAdm -Enabled $True -CannotChangePassword $True -PasswordNeverExpires $True -AccountPassword (ConvertTo-SecureString "@@{USER_CRED.secret}@@" -AsPlainText -force) -passThru
#  New-AdUser -Name $userNameDeveloper -Path $domainPath -UserPrincipalName $userPrincipalNameDeveloper -DisplayName $userNameDeveloper -Enabled $True -CannotChangePassword $True -PasswordNeverExpires $True -AccountPassword (ConvertTo-SecureString "@@{USER_CRED.secret}@@" -AsPlainText -force) -passThru
  Add-ADGroupMember -Identity "SSPProjectAdminGp" -Members $userNameProjAdm -passThru
  
  New-AdUser -Name $userNameDeveloper -UserPrincipalName $userPrincipalNameDeveloper -DisplayName $userNameDeveloper -Enabled $True -CannotChangePassword $True -PasswordNeverExpires $True -AccountPassword (ConvertTo-SecureString "@@{USER_CRED.secret}@@" -AsPlainText -force) -passThru
  
  Add-ADGroupMember -Identity "SSPDeveloperGp" -Members $userNameDeveloper -passThru
  
  New-AdUser -Name $userNameBPDeveloper -UserPrincipalName $userPrincipalNameBPDeveloper -DisplayName $userNameBPDeveloper -Enabled $True -CannotChangePassword $True -PasswordNeverExpires $True -AccountPassword (ConvertTo-SecureString "@@{USER_CRED.secret}@@" -AsPlainText -force) -passThru
  
  Add-ADGroupMember -Identity "SSPBPDeveloperGp" -Members $userNameBPDeveloper -passThru
  
  New-AdUser -Name $userNameNKPSuperAdmin -UserPrincipalName $userPrincipalNameNKPSuperAdmin -DisplayName $userNameNKPSuperAdmin -Enabled $True -CannotChangePassword $True -PasswordNeverExpires $True -AccountPassword (ConvertTo-SecureString "@@{USER_CRED.secret}@@" -AsPlainText -force) -passThru
  
  Add-ADGroupMember -Identity "NKPSuperAdminGp" -Members $userNameNKPSuperAdmin -passThru
  
  New-AdUser -Name $userNameNKPProjectAdmin -UserPrincipalName $userPrincipalNameNKPProjectAdmin -DisplayName $userNameNKPProjectAdmin -Enabled $True -CannotChangePassword $True -PasswordNeverExpires $True -AccountPassword (ConvertTo-SecureString "@@{USER_CRED.secret}@@" -AsPlainText -force) -passThru
  
  Add-ADGroupMember -Identity "NKPProjectAdminGp" -Members $userNameNKPProjectAdmin -passThru
  
  New-AdUser -Name $userNameNKPWorkspaceAdmin -UserPrincipalName $userPrincipalNameNKPWorkspaceAdmin -DisplayName $userNameNKPWorkspaceAdmin -Enabled $True -CannotChangePassword $True -PasswordNeverExpires $True -AccountPassword (ConvertTo-SecureString "@@{USER_CRED.secret}@@" -AsPlainText -force) -passThru
  
  Add-ADGroupMember -Identity "NKPWorkspaceAdminGp" -Members $userNameNKPWorkspaceAdmin -passThru
}