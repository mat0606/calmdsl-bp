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

BP_CRED_RHEL_KEY = read_local_file("BP_CRED_RHEL_KEY")
BP_CRED_RHEL2Credential_PASSWORD = read_local_file("BP_CRED_RHEL2Credential_PASSWORD")
BP_CRED_DOMAIN_CRED_PASSWORD = read_local_file("BP_CRED_DOMAIN_CRED_PASSWORD")

# Credentials
BP_CRED_RHEL = basic_cred(
    "nutanix",
    BP_CRED_RHEL_KEY,
    name="RHEL",
    type="KEY",
    default=True,
    editables={"username": True, "secret": True},
)
BP_CRED_RHEL2Credential = basic_cred(
    "nutanix",
    BP_CRED_RHEL2Credential_PASSWORD,
    name="RHEL 2 Credential",
    type="PASSWORD",
    editables={"username": True, "secret": True},
)
BP_CRED_DOMAIN_CRED = basic_cred(
    "administrator@ntnxlab1.local",
    BP_CRED_DOMAIN_CRED_PASSWORD,
    name="DOMAIN_CRED",
    type="PASSWORD",
)


class Service1(Service):

    pass


class vmcalm_timeResources(AhvVmResources):

    memory = 2
    vCPUs = 2
    cores_per_vCPU = 1
    disks = [
        AhvVmDisk.Disk.Scsi.cloneFromImageService(
            "rhel92-calm-template.qcow2", bootable=True
        )
    ]
    nics = [AhvVmNic.NormalNic.ingress("SG-AMK", vpc="SingaporeVPC")]

    guest_customization = AhvVmGC.CloudInit(
        filename=os.path.join("specs", "vmcalm_time_cloud_init_data.yaml")
    )

    power_state = "ON"
    boot_type = "LEGACY"


class vmcalm_time(AhvVm):

    name = "vm-@@{calm_time}@@"
    resources = vmcalm_timeResources
    cluster = Ref.Cluster(name="PHX-POC155")


class VM1(Substrate):

    account = Ref.Account("NTNX_LOCAL_AZ_ITC")
    os_type = "Linux"
    provider_type = "AHV_VM"
    provider_spec = vmcalm_time
    provider_spec_editables = read_spec(
        os.path.join("specs", "VM1_create_spec_editables.yaml")
    )
    readiness_probe = readiness_probe(
        connection_type="SSH",
        disabled=False,
        retries="5",
        connection_port=22,
        address="@@{platform.status.resources.nic_list[0].ip_endpoint_list[0].ip}@@",
        delay_secs="90",
        credential=ref(BP_CRED_RHEL),
    )


class UpdateVMConfig_Update_ConfigAttrs2df8a7cf(AhvUpdateConfigAttrs):

    memory = PatchField.Ahv.memory(
        value="2", operation="equal", max_val=16, min_val=1, editable=True
    )

    numsocket = PatchField.Ahv.numsocket(
        value="2", operation="equal", max_val=8, min_val=1, editable=True
    )

    disks = [
        PatchField.Ahv.Disks.modify(index=0, editable=False),
        PatchField.Ahv.Disks.add(AhvVmDisk.Disk.Scsi.allocateOnStorageContainer(20)),
    ]


class Package1(Package):

    services = [ref(Service1)]

    @action
    def __install__():

        CalmTask.Exec.ssh(
            name="Installed OS Packages",
            filename=os.path.join(
                "scripts",
                "Package_Package1_Action___install___Task_InstalledOSPackages.sh",
            ),
            cred=ref(BP_CRED_RHEL),
            target=ref(Service1),
        )

        CalmTask.Exec.ssh(
            name="Join DNS",
            filename=os.path.join(
                "scripts", "Package_Package1_Action___install___Task_JoinDNS.sh"
            ),
            cred=ref(BP_CRED_RHEL),
            target=ref(Service1),
        )

        CalmTask.Exec.ssh(
            name="Validate DNS Lookup",
            filename=os.path.join(
                "scripts",
                "Package_Package1_Action___install___Task_ValidateDNSLookup.sh",
            ),
            cred=ref(BP_CRED_RHEL),
            target=ref(Service1),
        )

        CalmTask.Exec.ssh(
            name="Validate Connection to AD",
            filename=os.path.join(
                "scripts",
                "Package_Package1_Action___install___Task_ValidateConnectiontoAD.sh",
            ),
            cred=ref(BP_CRED_RHEL),
            target=ref(Service1),
        )

        CalmTask.Exec.ssh(
            name="Synchronize time to AD",
            filename=os.path.join(
                "scripts",
                "Package_Package1_Action___install___Task_SynchronizetimetoAD.sh",
            ),
            cred=ref(BP_CRED_RHEL),
            target=ref(Service1),
        )

        CalmTask.Exec.ssh(
            name="Join AD Domain",
            filename=os.path.join(
                "scripts", "Package_Package1_Action___install___Task_JoinADDomain.sh"
            ),
            cred=ref(BP_CRED_RHEL),
            target=ref(Service1),
        )

    @action
    def __uninstall__():

        CalmTask.Exec.ssh(
            name="Unjoin AD Domain",
            filename=os.path.join(
                "scripts",
                "Package_Package1_Action___uninstall___Task_UnjoinADDomain.sh",
            ),
            cred=ref(BP_CRED_RHEL),
            target=ref(Service1),
        )


class _2a3092de_deployment(Deployment):

    name = "2a3092de_deployment"
    min_replicas = "1"
    max_replicas = "1"
    default_replicas = "1"

    packages = [ref(Package1)]
    substrate = ref(VM1)


class Default(Profile):

    deployments = [_2a3092de_deployment]
    patch_list = [
        AppEdit.UpdateConfig(
            name="UpdateVMConfig",
            target=ref(_2a3092de_deployment),
            patch_attrs=UpdateVMConfig_Update_ConfigAttrs2df8a7cf,
        )
    ]
    restore_configs = [
        AppProtection.RestoreConfig.Ahv(
            name="Restore_ConfigRHEL9_Snapshot",
            target=ref(_2a3092de_deployment),
            delete_vm_post_restore=True,
        )
    ]
    snapshot_configs = [
        AppProtection.SnapshotConfig.Ahv(
            name="Snapshot_ConfigRHEL9_Snapshot",
            target=ref(_2a3092de_deployment),
            num_of_replicas="ONE",
            restore_config=ref(restore_configs[0]),
            snapshot_location_type="LOCAL",
        )
    ]

    domain_name = CalmVariable.Simple(
        "ntnxlab1.local",
        label="",
        is_mandatory=False,
        is_hidden=False,
        runtime=False,
        description="",
    )

    Domain_Server_IP = CalmVariable.Simple(
        "10.55.88.59",
        label="",
        is_mandatory=False,
        is_hidden=False,
        runtime=False,
        description="",
    )

    Domain_Server = CalmVariable.Simple(
        "WIN-2U3E71T1COI",
        label="",
        is_mandatory=False,
        is_hidden=False,
        runtime=False,
        description="",
    )

    @action
    def Snapshot_RHEL9_Snapshot():

        CalmTask.ConfigExec(
            name="Snapshot_ConfigRHEL9_Snapshot_Task",
            config=ref(Default.snapshot_configs[0]),
        )

    @action
    def Restore_RHEL9_Snapshot():

        CalmTask.ConfigExec(
            name="Restore_ConfigRHEL9_Snapshot_Task",
            config=ref(Default.restore_configs[0]),
        )


class RHELSingleVPC(Blueprint):

    services = [Service1]
    packages = [Package1]
    substrates = [VM1]
    profiles = [Default]
    credentials = [BP_CRED_RHEL, BP_CRED_RHEL2Credential, BP_CRED_DOMAIN_CRED]


class BpMetadata(Metadata):

    categories = {"TemplateType": "Vm"}
    project = Ref.Project("BP Design Project")
