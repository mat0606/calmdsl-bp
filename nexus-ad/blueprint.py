# THIS FILE IS AUTOMATICALLY GENERATED.
# Disclaimer: Please test this file before using in production.
"""
Generated blueprint DSL (.py)
"""

import json  # no_qa
import os  # no_qa

from calm.dsl.builtins import *  # no_qa
from calm.dsl.runbooks import CalmEndpoint as Endpoint

# Secret Variables

BP_CRED_ROCKY_KEY = read_local_file("BP_CRED_ROCKY_KEY")
BP_CRED_DomainAdministrator_PASSWORD = read_local_file(
    "BP_CRED_DomainAdministrator_PASSWORD"
)
BP_CRED_ROCKY2Credential_PASSWORD = read_local_file(
    "BP_CRED_ROCKY2Credential_PASSWORD"
)
BP_CRED_ROOT2Credential_PASSWORD = read_local_file("BP_CRED_ROOT2Credential_PASSWORD")

# Credentials
BP_CRED_ROCKY = basic_cred(
    "nutanix",
    BP_CRED_ROCKY_KEY,
    name="ROCKY",
    type="KEY",
    default=True,
)
BP_CRED_DomainAdministrator = basic_cred(
    "administrator@ntnxlab1.local",
    BP_CRED_DomainAdministrator_PASSWORD,
    name="Domain Administrator",
    type="PASSWORD",
)
BP_CRED_ROCKY2Credential = basic_cred(
    "nutanix",
    BP_CRED_ROCKY2Credential_PASSWORD,
    name="ROCKY 2 Credential",
    type="PASSWORD",
)
BP_CRED_ROOT2Credential = basic_cred(
    "root",
    BP_CRED_ROOT2Credential_PASSWORD,
    name="ROOT 2 Credential",
    type="PASSWORD",
)


class Nexus(Service):
    @action
    def __create__():
        """System action for creating an application"""

        CalmTask.Delay(
            name="Wait for Nexus to start up", delay_seconds=60, target=ref(Nexus)
        )

        CalmTask.Exec.ssh(
            name="Verify Installation",
            filename=os.path.join(
                "scripts", "Service_Nexus_Action___create___Task_VerifyInstallation.sh"
            ),
            cred=ref(BP_CRED_ROCKY),
            target=ref(Nexus),
        )

        CalmTask.Exec.ssh(
            name="Output password",
            filename=os.path.join(
                "scripts", "Service_Nexus_Action___create___Task_Outputpassword.sh"
            ),
            cred=ref(BP_CRED_ROCKY),
            target=ref(Nexus),
        )

    @action
    def __delete__():
        """System action for deleting an application. Deletes created VMs as well"""

        Nexus.UnjoinADDomain(name="Unjoin AD Domain")

    @action
    def JoinADDomain(name="Join AD Domain"):

        CalmTask.Exec.ssh(
            name="Installed OS Packages",
            filename=os.path.join(
                "scripts",
                "Service_Nexus_Action_JoinADDomain_Task_InstalledOSPackages.sh",
            ),
            cred=ref(BP_CRED_ROCKY),
            target=ref(Nexus),
        )

        CalmTask.Exec.ssh(
            name="Join DNS",
            filename=os.path.join(
                "scripts", "Service_Nexus_Action_JoinADDomain_Task_JoinDNS.sh"
            ),
            cred=ref(BP_CRED_ROCKY),
            target=ref(Nexus),
        )

        Nexus.Prerequisites(name="Validate Prerequisites")

        CalmTask.Exec.ssh(
            name="Join AD Domain",
            filename=os.path.join(
                "scripts", "Service_Nexus_Action_JoinADDomain_Task_JoinADDomain.sh"
            ),
            cred=ref(BP_CRED_ROCKY),
            target=ref(Nexus),
        )

    @action
    def UnjoinADDomain(name="Unjoin AD Domain"):

        CalmTask.Exec.ssh(
            name="Unjoin AD Domain",
            filename=os.path.join(
                "scripts", "Service_Nexus_Action_UnjoinADDomain_Task_UnjoinADDomain.sh"
            ),
            cred=ref(BP_CRED_ROCKY),
            target=ref(Nexus),
        )
    
    @action
    def Prerequisites():

        CalmTask.Exec.ssh(
            name="Validate DNS Lookup",
            filename=os.path.join(
                "scripts",
                "Service_Nexus_Action_Prerequisites_Task_ValidateDNSLookup.sh",
            ),
            cred=ref(BP_CRED_ROCKY),
            target=ref(Nexus),
        )

        CalmTask.Exec.ssh(
            name="Validate connection to AD",
            filename=os.path.join(
                "scripts",
                "Service_Nexus_Action_Prerequisites_Task_ValidateconnectiontoAD.sh",
            ),
            cred=ref(BP_CRED_ROCKY),
            target=ref(Nexus),
        )

        CalmTask.Exec.ssh(
            name="Synchronize time with AD",
            filename=os.path.join(
                "scripts",
                "Service_Nexus_Action_Prerequisites_Task_SynchronizetimewithAD.sh",
            ),
            cred=ref(BP_CRED_ROCKY),
            target=ref(Nexus),
        )

    @action
    def ConfigureNexusOSSDataDisk(name="Configure Nexus OSS Data Disk"):

        CalmTask.Exec.ssh(
            name="Current Disk Information",
            filename=os.path.join(
                "scripts",
                "Service_Nexus_Action_ConfigureNexusOSSDataDisk_Task_CurrentDiskInformation.sh",
            ),
            cred=ref(BP_CRED_ROOT2Credential),
            target=ref(Nexus),
        )

        CalmTask.Exec.ssh(
            name="Configure to use 2nd disk",
            filename=os.path.join(
                "scripts",
                "Service_Nexus_Action_ConfigureNexusOSSDataDisk_Task_Configuretouse2nddisk.sh",
            ),
            cred=ref(BP_CRED_ROOT2Credential),
            target=ref(Nexus),
        )

        CalmTask.Exec.ssh(
            name="Mount the drive",
            filename=os.path.join(
                "scripts",
                "Service_Nexus_Action_ConfigureNexusOSSDataDisk_Task_Mountthedrive.sh",
            ),
            cred=ref(BP_CRED_ROOT2Credential),
            target=ref(Nexus),
        )

        CalmTask.Exec.ssh(
            name="Configure fstab",
            filename=os.path.join(
                "scripts",
                "Service_Nexus_Action_ConfigureNexusOSSDataDisk_Task_Configurefstab.sh",
            ),
            cred=ref(BP_CRED_ROOT2Credential),
            target=ref(Nexus),
        )

        CalmTask.Exec.ssh(
            name="Verify fstab mount",
            filename=os.path.join(
                "scripts",
                "Service_Nexus_Action_ConfigureNexusOSSDataDisk_Task_Verifyfstabmount.sh",
            ),
            cred=ref(BP_CRED_ROOT2Credential),
            target=ref(Nexus),
        )

        Nexus.__restart__(name="Restart the VM")

        CalmTask.Exec.ssh(
            name="Verify Mount information",
            filename=os.path.join(
                "scripts",
                "Service_Nexus_Action_ConfigureNexusOSSDataDisk_Task_VerifyMountinformation.sh",
            ),
            cred=ref(BP_CRED_ROOT2Credential),
            target=ref(Nexus),
        )

    @action
    def InstallNexus(name="Install Nexus"):

        CalmTask.Exec.ssh(
            name="Install Nexus",
            filename=os.path.join(
                "scripts", "Service_Nexus_Action_InstallNexus_Task_InstallNexus.sh"
            ),
            cred=ref(BP_CRED_ROCKY),
            target=ref(Nexus),
        )

        CalmTask.Exec.ssh(
            name="Configure Environment",
            filename=os.path.join(
                "scripts",
                "Service_Nexus_Action_InstallNexus_Task_ConfigureEnvironment.sh",
            ),
            cred=ref(BP_CRED_ROCKY),
            target=ref(Nexus),
        )

        CalmTask.Exec.ssh(
            name="Configure Nexus VM option",
            filename=os.path.join(
                "scripts",
                "Service_Nexus_Action_InstallNexus_Task_ConfigureNexusVMoption.sh",
            ),
            cred=ref(BP_CRED_ROCKY),
            target=ref(Nexus),
        )

        CalmTask.Exec.ssh(
            name="Configure Nexus App Host",
            filename=os.path.join(
                "scripts",
                "Service_Nexus_Action_InstallNexus_Task_ConfigureNexusAppHost.sh",
            ),
            cred=ref(BP_CRED_ROCKY),
            target=ref(Nexus),
        )

        CalmTask.Exec.ssh(
            name="Generate SSL Certificate",
            filename=os.path.join(
                "scripts",
                "Service_Nexus_Action_InstallNexus_Task_GenerateSSLCertificate.sh",
            ),
            cred=ref(BP_CRED_ROCKY),
            target=ref(Nexus),
        )

        CalmTask.Exec.ssh(
            name="Import Cert into Truststore",
            filename=os.path.join(
                "scripts",
                "Service_Nexus_Action_InstallNexus_Task_ImportCertintoTruststore.sh",
            ),
            cred=ref(BP_CRED_ROCKY),
            target=ref(Nexus),
        )

        CalmTask.Exec.ssh(
            name="Enable HTTPS",
            filename=os.path.join(
                "scripts", "Service_Nexus_Action_InstallNexus_Task_EnableHTTPS.sh"
            ),
            cred=ref(BP_CRED_ROCKY),
            target=ref(Nexus),
        )

        CalmTask.Exec.ssh(
            name="Create System D Account",
            filename=os.path.join(
                "scripts",
                "Service_Nexus_Action_InstallNexus_Task_CreateSystemDAccount.sh",
            ),
            cred=ref(BP_CRED_ROCKY),
            target=ref(Nexus),
        )

        CalmTask.Exec.ssh(
            name="Start Nexus Service",
            filename=os.path.join(
                "scripts", "Service_Nexus_Action_InstallNexus_Task_StartNexusService.sh"
            ),
            cred=ref(BP_CRED_ROCKY),
            target=ref(Nexus),
        )


class ncalm_timeResources(AhvVmResources):

    memory = 10
    vCPUs = 4
    cores_per_vCPU = 1
    disks = [
        AhvVmDisk.Disk.Scsi.cloneFromImageService(
            "rocky95-calm-template.qcow2", bootable=True
        ),
        AhvVmDisk.Disk.Scsi.allocateOnStorageContainer(5000),
    ]
    nics = [AhvVmNic.NormalNic.ingress("Calm_Primary_ITC", cluster="PHX-POC155")]

    guest_customization = AhvVmGC.CloudInit(
        filename=os.path.join("specs", "ncalm_time_cloud_init_data.yaml")
    )

    power_state = "ON"


class ncalm_time(AhvVm):

    name = "n@@{calm_time}@@"
    resources = ncalm_timeResources
    cluster = Ref.Cluster(name="PHX-POC155")
    categories = {"AppType": "Default", "Owner": "Matthew"}


class Nexus_VM(Substrate):

    account = Ref.Account("NTNX_LOCAL_AZ_ITC")
    os_type = "Linux"
    provider_type = "AHV_VM"
    provider_spec = ncalm_time
    provider_spec_editables = read_spec(
        os.path.join("specs", "Nexus_VM_create_spec_editables.yaml")
    )
    readiness_probe = readiness_probe(
        connection_type="SSH",
        disabled=False,
        retries="5",
        connection_port=22,
        address="@@{platform.status.resources.nic_list[0].ip_endpoint_list[0].ip}@@",
        delay_secs="70",
        credential=ref(BP_CRED_ROCKY),
    )


class Package1(Package):

    services = [ref(Nexus)]

    @action
    def __install__():

        Nexus.ConfigureNexusOSSDataDisk(name="Configure VM to use 2nd disk")

        Nexus.JoinADDomain(name="Join AD Domain")

        CalmTask.Exec.ssh(
            name="Install OpenJDK",
            filename=os.path.join(
                "scripts", "Package_Package1_Action___install___Task_InstallOpenJDK.sh"
            ),
            cred=ref(BP_CRED_ROCKY),
            target=ref(Nexus),
        )

        Nexus.InstallNexus(name="Install Nexus")

        CalmTask.Exec.ssh(
            name="Change Mount Drive owner",
            filename=os.path.join(
                "scripts",
                "Package_Package1_Action___install___Task_ChangeMountDriveowner.sh",
            ),
            cred=ref(BP_CRED_ROOT2Credential),
            target=ref(Nexus),
        )


class b1a5673a_deployment(Deployment):

    min_replicas = "1"
    max_replicas = "1"
    default_replicas = "1"

    packages = [ref(Package1)]
    substrate = ref(Nexus_VM)


class Default(Profile):

    deployments = [b1a5673a_deployment]

    domain_name = CalmVariable.Simple(
        "ntnxlab1.local",
        label="",
        is_mandatory=False,
        is_hidden=False,
        runtime=True,
        description="",
    )

    Domain_Server_IP = CalmVariable.Simple(
        "10.55.88.59",
        label="",
        is_mandatory=False,
        is_hidden=False,
        runtime=True,
        description="",
    )

    Domain_Server = CalmVariable.Simple(
        "WIN-2U3E71T1COI",
        label="",
        is_mandatory=False,
        is_hidden=False,
        runtime=True,
        description="",
    )
    
    device_name = CalmVariable.Simple(
        "sdb",
        label="Device Name for the extended drive",
        is_mandatory=False,
        is_hidden=True,
        runtime=False,
        description="",
    )

    jdk_path = CalmVariable.Simple(
        "/usr/lib/jvm/java-17-openjdk",
        label="Device Name for the extended drive",
        is_mandatory=False,
        is_hidden=True,
        runtime=False,
        description="",
    )

    jre_path = CalmVariable.Simple(
        "/usr/lib/jvm/jre-17-openjdk",
        label="Device Name for the extended drive",
        is_mandatory=False,
        is_hidden=True,
        runtime=False,
        description="",
    )

class NexusADhttps20240703(Blueprint):
    """Nexus-OSS: https://@@{Nexus_VM.address}@@:8443/"""

    services = [Nexus]
    packages = [Package1]
    substrates = [Nexus_VM]
    profiles = [Default]
    credentials = [
        BP_CRED_ROCKY,
        BP_CRED_DomainAdministrator,
        BP_CRED_ROCKY2Credential,
        BP_CRED_ROOT2Credential,
    ]


class BpMetadata(Metadata):

    project = Ref.Project("BP Design Project")
