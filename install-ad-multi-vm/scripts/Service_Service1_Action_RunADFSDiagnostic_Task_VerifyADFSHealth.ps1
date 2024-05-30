Write-Host "Installing ADFS Diagnostic to perform health check"
#Install-Module ADFSDiagnostics -Force
#Import-Module ADFSDiagnostics -Force
#Test-AdfsServerHealth | ft Name,Result -AutoSize
Install-Module -Name ADFSToolbox -Force

