Enable-WSManCredSSP -Role Server -Force
Install-windowsfeature -name AD-Domain-Services -IncludeManagementTools