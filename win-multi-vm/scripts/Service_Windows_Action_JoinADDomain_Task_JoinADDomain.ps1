function JointoDomain {
    [CmdletBinding()]
    Param(
        [parameter(Mandatory=$true)]
        [string]$DomainName,
        [parameter(Mandatory=$false)]
        [string]$OU,
        [parameter(Mandatory=$true)]
        [string]$Username,
        [parameter(Mandatory=$true)]
        [string]$Password,
        [parameter(Mandatory=$true)]
        [string]$Server
    )
    $adapter = Get-NetAdapter | ? {$_.Status -eq "up"}
    $adapter | Set-DnsClientServerAddress -ServerAddresses $Server

    if ($env:computername  -eq $env:userdomain) {
        Write-Host "Not in domain"
        $adminname = "$DomainName\$Username"
        $adminpassword = ConvertTo-SecureString -asPlainText -Force -String "$Password"
        Write-Host "$adminname , $password"
        $credential = New-Object System.Management.Automation.PSCredential($adminname,$adminpassword)
        Add-computer -DomainName $DomainName -Credential $credential -force -Options JoinWithNewName,AccountCreate -PassThru -ErrorAction Stop
    } else {
        Write-Host "Already in domain"
    }
}

JointoDomain -DomainName "@@{DOMAIN_NAME}@@" -Username "@@{DOMAIN_CRED.username}@@" -Password "@@{DOMAIN_CRED.secret}@@" -Server "@@{AD}@@"