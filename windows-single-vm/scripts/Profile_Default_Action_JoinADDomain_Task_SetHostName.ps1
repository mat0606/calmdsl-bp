$HOSTNAME = "@@{name}@@"

function Set-Hostname{
  [CmdletBinding()]
  Param(
      [parameter(Mandatory=$true)]
      [string]$Hostname
)
  if ($Hostname -eq  $(hostname)){
    Write-Host "Hostname already set."
  } else{
    Rename-Computer -NewName $HOSTNAME -ErrorAction Stop
  }
}

if ($HOSTNAME -ne $Null){
  Write-Host "Setting Hostname"
  Set-Hostname -Hostname $HOSTNAME
}

Restart-Computer -Force -AsJob
exit 0
