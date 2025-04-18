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

BP_CRED_WIN_VM_CRED_PASSWORD = read_local_file("BP_CRED_WIN_VM_CRED_PASSWORD")
BP_CRED_DOMAIN_CRED_PASSWORD = read_local_file("BP_CRED_DOMAIN_CRED_PASSWORD")
BP_CRED_USER_CRED_PASSWORD = read_local_file("BP_CRED_USER_CRED_PASSWORD")

# Credentials
BP_CRED_WIN_VM_CRED = basic_cred(
    "Administrator",
    BP_CRED_WIN_VM_CRED_PASSWORD,
    name="WIN_VM_CRED",
    type="PASSWORD",
    default=True,
    editables={"username": True, "secret": True},
)
BP_CRED_DOMAIN_CRED = basic_cred(
    "administrator@ntnxlab2.local",
    BP_CRED_DOMAIN_CRED_PASSWORD,
    name="DOMAIN_CRED",
    type="PASSWORD",
    editables={"username": True, "secret": True},
)
BP_CRED_USER_CRED = basic_cred(
    "tenant",
    BP_CRED_USER_CRED_PASSWORD,
    name="USER_CRED",
    type="PASSWORD",
)


class Service1(Service):
    @action
    def InstallADandDNS(name="Install AD and DNS"):

        CalmTask.Exec.powershell(
            name="Install AD",
            filename=os.path.join(
                "scripts", "Service_Service1_Action_InstallADandDNS_Task_InstallAD.ps1"
            ),
            cred=ref(BP_CRED_WIN_VM_CRED),
            target=ref(Service1),
        )

        CalmTask.Exec.powershell(
            name="Import ADDS Deployment",
            filename=os.path.join(
                "scripts",
                "Service_Service1_Action_InstallADandDNS_Task_ImportADDSDeployment.ps1",
            ),
            cred=ref(BP_CRED_WIN_VM_CRED),
            target=ref(Service1),
        )

        CalmTask.Exec.powershell(
            name="Install Domain Controller and Forest",
            filename=os.path.join(
                "scripts",
                "Service_Service1_Action_InstallADandDNS_Task_InstallDomainControllerandForest.ps1",
            ),
            cred=ref(BP_CRED_WIN_VM_CRED),
            target=ref(Service1),
        )

        CalmTask.Delay(
            name="Reboot and Post installation", delay_seconds=300, target=ref(Service1)
        )

        CalmTask.Exec.powershell(
            name="Add DNS Primary Zone",
            filename=os.path.join(
                "scripts",
                "Service_Service1_Action_InstallADandDNS_Task_AddDNSPrimaryZone.ps1",
            ),
            cred=ref(BP_CRED_WIN_VM_CRED),
            target=ref(Service1),
        )

    @action
    def InstallADFS(name="Install ADFS"):

        CalmTask.Exec.powershell(
            name="Install ADFS",
            filename=os.path.join(
                "scripts", "Service_Service1_Action_InstallADFS_Task_InstallADFS.ps1"
            ),
            cred=ref(BP_CRED_DOMAIN_CRED),
            target=ref(Service1),
        )

        CalmTask.Exec.powershell(
            name="Reboot VM",
            filename=os.path.join(
                "scripts", "Service_Service1_Action_InstallADFS_Task_RebootVM.ps1"
            ),
            cred=ref(BP_CRED_DOMAIN_CRED),
            target=ref(Service1),
        )

        CalmTask.Delay(name="Delay for 8 mins", delay_seconds=480, target=ref(Service1))

        CalmTask.Exec.powershell(
            name="Start Service",
            filename=os.path.join(
                "scripts", "Service_Service1_Action_InstallADFS_Task_StartService.ps1"
            ),
            cred=ref(BP_CRED_DOMAIN_CRED),
            target=ref(Service1),
        )

        CalmTask.Exec.powershell(
            name="Verify SSO",
            filename=os.path.join(
                "scripts", "Service_Service1_Action_InstallADFS_Task_VerifySSO.ps1"
            ),
            cred=ref(BP_CRED_DOMAIN_CRED),
            target=ref(Service1),
        )

        Service1.RunADFSDiagnostic(name="Run ADFS Diagnostic")

    @action
    def RunADFSDiagnostic(name="Run ADFS Diagnostic"):

        CalmTask.Exec.powershell(
            name="Verify ADFS Health",
            filename=os.path.join(
                "scripts",
                "Service_Service1_Action_RunADFSDiagnostic_Task_VerifyADFSHealth.ps1",
            ),
            cred=ref(BP_CRED_DOMAIN_CRED),
            target=ref(Service1),
        )

        CalmTask.Delay(name="Delay for 2 min", delay_seconds=120, target=ref(Service1))

        CalmTask.Exec.powershell(
            name="Export Diagnostic Report",
            filename=os.path.join(
                "scripts",
                "Service_Service1_Action_RunADFSDiagnostic_Task_ExportDiagnosticReport.ps1",
            ),
            cred=ref(BP_CRED_DOMAIN_CRED),
            target=ref(Service1),
        )

    @action
    def ConfigureNTPServer(name="Configure NTP Server"):

        CalmTask.Exec.powershell(
            name="Enable NTP Server",
            filename=os.path.join(
                "scripts",
                "Service_Service1_Action_ConfigureNTPServer_Task_EnableNTPServer.ps1",
            ),
            cred=ref(BP_CRED_WIN_VM_CRED),
            target=ref(Service1),
        )

        CalmTask.Exec.powershell(
            name="Configure Announce Flag",
            filename=os.path.join(
                "scripts",
                "Service_Service1_Action_ConfigureNTPServer_Task_ConfigureAnnounceFlag.ps1",
            ),
            cred=ref(BP_CRED_WIN_VM_CRED),
            target=ref(Service1),
        )

        CalmTask.Exec.powershell(
            name="Restart NTP Server",
            filename=os.path.join(
                "scripts",
                "Service_Service1_Action_ConfigureNTPServer_Task_RestartNTPServer.ps1",
            ),
            cred=ref(BP_CRED_WIN_VM_CRED),
            target=ref(Service1),
        )

        CalmTask.Exec.powershell(
            name="Open UDP Port 123",
            filename=os.path.join(
                "scripts",
                "Service_Service1_Action_ConfigureNTPServer_Task_OpenUDPPort123.ps1",
            ),
            cred=ref(BP_CRED_WIN_VM_CRED),
            target=ref(Service1),
        )

    @action
    def InstallEdgeBrowser(name="Install Edge Browser"):

        CalmTask.Exec.powershell(
            name="Install Edge Browser",
            filename=os.path.join(
                "scripts",
                "Service_Service1_Action_InstallEdgeBrowser_Task_InstallEdgeBrowser.ps1",
            ),
            cred=ref(BP_CRED_WIN_VM_CRED),
            target=ref(Service1),
        )

    @action
    def ChangeComputerName(name="Change Computer Name"):

        CalmTask.Exec.powershell(
            name="Change Computer Name",
            filename=os.path.join(
                "scripts",
                "Service_Service1_Action_ChangeComputerName_Task_ChangeComputerName.ps1",
            ),
            cred=ref(BP_CRED_WIN_VM_CRED),
            target=ref(Service1),
        )

        CalmTask.Delay(name="Reboot", delay_seconds=120, target=ref(Service1))

    @action
    def Onboardusers(name="Onboard users"):

        CalmTask.Exec.powershell(
            name="Create users",
            filename=os.path.join(
                "scripts", "Service_Service1_Action_Onboardusers_Task_Createusers.ps1"
            ),
            cred=ref(BP_CRED_DOMAIN_CRED),
            target=ref(Service1),
        )


class vmcalm_array_indexcalm_timeResources(AhvVmResources):

    memory = 2
    vCPUs = 2
    cores_per_vCPU = 1
    disks = [
        AhvVmDisk.Disk.Scsi.cloneFromImageService(
            "windows-2022-calm-ad-template.qcow2", bootable=True
        )
    ]
    nics = [AhvVmNic.NormalNic.ingress("Primary", cluster="PHX-POC155")]

    guest_customization = AhvVmGC.Sysprep.PreparedScript.withoutDomain(
        filename=os.path.join(
            "specs", "vmcalm_array_indexcalm_time_sysprep_unattend_xml.xml"
        )
    )

    power_state = "ON"
    boot_type = "LEGACY"


class vmcalm_array_indexcalm_time(AhvVm):

    name = "vm-@@{calm_array_index}@@-@@{calm_time}@@"
    resources = vmcalm_array_indexcalm_timeResources
    cluster = Ref.Cluster(name="PHX-POC155")


class VM1_2(Substrate):

    account = Ref.Account("NTNX_LOCAL_AZ_ITC")
    os_type = "Windows"
    provider_type = "AHV_VM"
    provider_spec = vmcalm_array_indexcalm_time

    readiness_probe = readiness_probe(
        connection_type="POWERSHELL",
        disabled=False,
        retries="5",
        connection_port=5985,
        address="@@{platform.status.resources.nic_list[0].ip_endpoint_list[0].ip}@@",
        delay_secs="60",
        credential=ref(BP_CRED_WIN_VM_CRED),
    )


class Config1_Update_ConfigAttrs66802504(AhvUpdateConfigAttrs):

    memory = PatchField.Ahv.memory(
        value="32", operation="equal", max_val=32, min_val=8, editable=True
    )

    numsocket = PatchField.Ahv.numsocket(
        value="2", operation="equal", max_val=8, min_val=2, editable=True
    )

    disks = [PatchField.Ahv.Disks.modify(index=0, editable=False)]


class Package2(Package):

    services = [ref(Service1)]

    @action
    def __install__():

        Service1.ChangeComputerName(name="Change Computer Name")

        Service1.InstallADandDNS(name="Install AD and DNS")

        Service1.ConfigureNTPServer(name="Configure NTP Server")

        Service1.InstallEdgeBrowser(name="Install Edge Browser")


class d1683190_deployment(Deployment):

    min_replicas = "1"
    max_replicas = "1"
    default_replicas = "1"

    packages = [ref(Package2)]
    substrate = ref(VM1_2)


class Profile2(Profile):

    name = "Profile 2"

    deployments = [d1683190_deployment]
    patch_list = [
        AppEdit.UpdateConfig(
            name="Config1",
            target=ref(d1683190_deployment),
            patch_attrs=Config1_Update_ConfigAttrs66802504,
        )
    ]
    restore_configs = [
        AppProtection.RestoreConfig.Ahv(
            name="Restore_Configvm_snapshot",
            target=ref(d1683190_deployment),
            delete_vm_post_restore=False,
        )
    ]
    snapshot_configs = [
        AppProtection.SnapshotConfig.Ahv(
            name="Snapshot_Configvm_snapshot",
            target=ref(d1683190_deployment),
            num_of_replicas="ONE",
            restore_config=ref(restore_configs[0]),
            snapshot_location_type="LOCAL",
        )
    ]

    edge_download_url = CalmVariable.Simple(
        "https://msedge.sf.dl.delivery.mp.microsoft.com/filestreamingservice/files/0fe5ee25-0f55-4163-a68c-b6b20c8ace7d/MicrosoftEdgeEnterpriseX64.msi",
        label="Microsoft Edge Download URL",
        is_mandatory=False,
        is_hidden=False,
        runtime=False,
        description="Get the download url from https://www.microsoft.com/en-us/edge/business/download?form=MA13FJ",
    )

    DOMAIN_NAME = CalmVariable.Simple(
        "ntnxlab2.local",
        label="",
        is_mandatory=True,
        is_hidden=False,
        runtime=True,
        description="",
    )

    subnet = CalmVariable.Simple(
        "10.38.142.128/25",
        label="",
        is_mandatory=True,
        is_hidden=False,
        runtime=True,
        description="",
    )

    computer_name = CalmVariable.Simple(
        "WIN-2U3E71T1COI",
        label="Please key in the computer name",
        is_mandatory=True,
        is_hidden=False,
        runtime=True,
        description="",
    )

    @action
    def InstallADFS(name="Install ADFS"):

        Service1.InstallADFS(name="Install ADFS")

    @action
    def RunADFSDiagnostic(name="Run ADFS Diagnostic"):

        Service1.RunADFSDiagnostic(name="Run ADFS Diagnostic")

    @action
    def OnboardDemoUsers(name="Onboard Demo Users"):

        Service1.Onboardusers(name="Onboard Demo Users")

    @action
    def TakeSnapshot(name="Take Snapshot"):

        CalmTask.ConfigExec(
            name="Take Snapshot", config=ref(Profile2.snapshot_configs[0])
        )

    @action
    def RestoreSnapshot(name="Restore Snapshot"):

        CalmTask.ConfigExec(name="Action1", config=ref(Profile2.restore_configs[0]))


class InstallADDNS(Blueprint):

    services = [Service1]
    packages = [Package2]
    substrates = [VM1_2]
    profiles = [Profile2]
    credentials = [BP_CRED_WIN_VM_CRED, BP_CRED_DOMAIN_CRED, BP_CRED_USER_CRED]


class BpMetadata(Metadata):

    project = Ref.Project("BP Design Project")
