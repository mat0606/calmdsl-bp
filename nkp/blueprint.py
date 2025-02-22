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
BP_CRED_ROCKY2Credential_PASSWORD = read_local_file("BP_CRED_ROCKY2Credential_PASSWORD")
BP_CRED_PCCredential_PASSWORD = read_local_file("BP_CRED_PCCredential_PASSWORD")
BP_CRED_CalmVMCredential_PASSWORD = read_local_file("BP_CRED_CalmVMCredential_PASSWORD")

# Credentials
BP_CRED_ROCKY = basic_cred(
    "nutanix",
    BP_CRED_ROCKY_KEY,
    name="ROCKY",
    type="KEY",
    default=True,
    editables={"username": True, "secret": True},
)
BP_CRED_ROCKY2Credential = basic_cred(
    "nutanix",
    BP_CRED_ROCKY2Credential_PASSWORD,
    name="ROCKY 2 Credential",
    type="PASSWORD",
    editables={"username": True, "secret": True},
)
BP_CRED_PCCredential = basic_cred(
    "admin",
    BP_CRED_PCCredential_PASSWORD,
    name="PC Credential",
    type="PASSWORD",
    editables={"username": True, "secret": True},
)
BP_CRED_CalmVMCredential = basic_cred(
    "admin",
    BP_CRED_CalmVMCredential_PASSWORD,
    name="CalmVM Credential",
    type="PASSWORD",
    editables={"username": True, "secret": True},
)


class Rocky(Service):
    @action
    def __delete__():
        """System action for deleting an application. Deletes created VMs as well"""

        Rocky.DeleteNKP(name="Delete NKP")

    @action
    def InstallNKP(name="Install NKP"):

        CalmTask.Exec.ssh(
            name="Download NKP Binary",
            filename=os.path.join(
                "scripts", "Service_Rocky_Action_InstallNKP_Task_DownloadNKPBinary.sh"
            ),
            cred=ref(BP_CRED_ROCKY2Credential),
            target=ref(Rocky),
        )

        CalmTask.Exec.ssh(
            name="Install NKP",
            filename=os.path.join(
                "scripts", "Service_Rocky_Action_InstallNKP_Task_InstallNKP.sh"
            ),
            cred=ref(BP_CRED_ROCKY2Credential),
            target=ref(Rocky),
        )

        CalmTask.Exec.ssh(
            name="Get User Credential",
            filename=os.path.join(
                "scripts", "Service_Rocky_Action_InstallNKP_Task_GetUserCredential.sh"
            ),
            cred=ref(BP_CRED_ROCKY2Credential),
            target=ref(Rocky),
        )

    @action
    def DeleteNKP(name="Delete NKP"):

        CalmTask.Exec.ssh(
            name="Delete NKP Management Cluster",
            filename=os.path.join(
                "scripts",
                "Service_Rocky_Action_DeleteNKP_Task_DeleteNKPManagementCluster.sh",
            ),
            cred=ref(BP_CRED_ROCKY2Credential),
            target=ref(Rocky),
        )

    @action
    def InstallPrerequisites(name="Install Prerequisites"):

        CalmTask.Exec.ssh(
            name="Install Docker",
            filename=os.path.join(
                "scripts",
                "Service_Rocky_Action_InstallPrerequisites_Task_InstallDocker.sh",
            ),
            cred=ref(BP_CRED_ROCKY2Credential),
            target=ref(Rocky),
        )

        CalmTask.Exec.ssh(
            name="Install bash completion",
            filename=os.path.join(
                "scripts",
                "Service_Rocky_Action_InstallPrerequisites_Task_Installbashcompletion.sh",
            ),
            cred=ref(BP_CRED_ROCKY2Credential),
            target=ref(Rocky),
        )

        CalmTask.Exec.ssh(
            name="Install k9s",
            filename=os.path.join(
                "scripts",
                "Service_Rocky_Action_InstallPrerequisites_Task_Installk9s.sh",
            ),
            cred=ref(BP_CRED_ROCKY2Credential),
            target=ref(Rocky),
        )


class nkpbootstrapcalm_timeResources(AhvVmResources):

    memory = 4
    vCPUs = 2
    cores_per_vCPU = 1
    disks = [
        AhvVmDisk.Disk.Scsi.cloneFromImageService(
            "nkp-rocky-9.5-release-1.30.5-20241125163629.qcow2", bootable=True
        ),
       # AhvVmDisk.Disk.Scsi.allocateOnStorageContainer(128),
    ]
    nics = [AhvVmNic.NormalNic.ingress("Calm_Primary_ITC", cluster="PHX-POC155")]

    guest_customization = AhvVmGC.CloudInit(
        filename=os.path.join("specs", "nkpbootstrapcalm_time_cloud_init_data.yaml")
    )

    power_state = "ON"


class nkpbootstrapcalm_time(AhvVm):

    name = "nkp-bootstrap-@@{calm_time}@@"
    resources = nkpbootstrapcalm_timeResources
    cluster = Ref.Cluster(name="PHX-POC155")
    categories = {
        "AppType": "Default",
        "Owner": "Matthew"
    }


class Rocky_VM(Substrate):

    account = Ref.Account("NTNX_LOCAL_AZ_ITC")
    os_type = "Linux"
    provider_type = "AHV_VM"
    provider_spec = nkpbootstrapcalm_time
    provider_spec_editables = read_spec(
        os.path.join("specs", "Rocky_VM_create_spec_editables.yaml")
    )
    readiness_probe = readiness_probe(
        connection_type="SSH",
        disabled=False,
        retries="5",
        connection_port=22,
        address="@@{platform.status.resources.nic_list[0].ip_endpoint_list[0].ip}@@",
        delay_secs="60",
        credential=ref(BP_CRED_ROCKY2Credential),
    )


class UpdateVMSpec_Update_ConfigAttrsa6e059d9(AhvUpdateConfigAttrs):

    memory = PatchField.Ahv.memory(
        value="2", operation="equal", max_val=4, min_val=2, editable=True
    )
    vcpu = PatchField.Ahv.vcpu(value="1", operation="equal", editable=False)
    numsocket = PatchField.Ahv.numsocket(
        value="2", operation="equal", max_val=4, min_val=2, editable=True
    )

    disks = [
        PatchField.Ahv.Disks.modify(
            index=0, editable=False, operation="equal", value="0"
        ),
        PatchField.Ahv.Disks.add(AhvVmDisk.Disk.Scsi.allocateOnStorageContainer(100)),
    ]


class Package1(Package):

    services = [ref(Rocky)]

    @action
    def __install__():

        Rocky.InstallPrerequisites(name="Install Prerequisities")

        Rocky.InstallNKP(name="Install NKP Management Cluster")


class b1a5673a_deployment(Deployment):

    min_replicas = "1"
    max_replicas = "1"
    default_replicas = "1"

    packages = [ref(Package1)]
    substrate = ref(Rocky_VM)


class Default(Profile):

    deployments = [b1a5673a_deployment]
    patch_list = [
        AppEdit.UpdateConfig(
            name="Update VM Spec",
            target=ref(b1a5673a_deployment),
            patch_attrs=UpdateVMSpec_Update_ConfigAttrsa6e059d9,
        )
    ]

    nkp_binary = CalmVariable.Simple(
        "nkp_v2.13.1_linux_amd64.tar.gz",
        label="",
        is_mandatory=False,
        is_hidden=True,
        runtime=False,
        description="",
    )

    nkp_machine_template_name = CalmVariable.Simple(
        "nkp-rocky-9.5-release-1.30.5-20241125163629.qcow2",
        label="",
        is_mandatory=False,
        is_hidden=True,
        runtime=False,
        description="",
    )

    nkp_binary_download_url = CalmVariable.Simple(
        "http://10.42.194.11/users/Matthew%20Ong/NKP2.13.1",
        label="Please key in the download path for NKP binary",
        is_mandatory=False,
        is_hidden=True,
        runtime=False,
        description="",
    )

    registry_mirror_url = CalmVariable.Simple(
        "registry.nutanixdemo.com/docker.io",
        label="Please key in the registry mirror url",
        is_mandatory=True,
        is_hidden=False,
        runtime=True,
        description="",
    )

    control_plane_endpoint = CalmVariable.Simple(
        "10.42.155.116",
        label="Please key in the control plane VIP",
        is_mandatory=True,
        is_hidden=False,
        runtime=True,
        description="",
    )

    lb_end_ip = CalmVariable.Simple(
        "10.42.155.115",
        label="Please key in the end IP of the load balancer",
        is_mandatory=True,
        is_hidden=False,
        runtime=True,
        description="",
    )

    lb_start_ip = CalmVariable.Simple(
        "10.42.155.115",
        label="Please key in the start IP of the load balancer",
        is_mandatory=True,
        is_hidden=False,
        runtime=True,
        description="",
    )

    nkp_version = CalmVariable.Simple(
        "2.13.1",
        label="Please key in the NKP version",
        is_mandatory=True,
        is_hidden=False,
        runtime=True,
        description="",
    )

    nkp_cluster_name = CalmVariable.Simple(
        "nkp2-13-1-mo-mgmt-cluster",
        label="Please key in the NKP Management Cluster Name",
        is_mandatory=True,
        is_hidden=False,
        runtime=True,
        description="",
    )

    subnet_name = CalmVariable.WithOptions.FromTask(
        CalmTask.Exec.escript.py3(
            name="",
            filename=os.path.join(
                "scripts", "Profile_Default_variable_subnet_name_Task_SampleTask.py"
            ),
        ),
        label="Please select the subnet",
        regex="^.*$",
        validate_regex=False,
        is_mandatory=True,
        is_hidden=False,
        description="",
    )

    cluster_name = CalmVariable.WithOptions.FromTask(
        CalmTask.Exec.escript.py3(
            name="",
            filename=os.path.join(
                "scripts", "Profile_Default_variable_cluster_name_Task_SampleTask.py"
            ),
        ),
        label="Please select the Nutanix Cluster",
        is_mandatory=True,
        is_hidden=False,
        description="",
    )

    PC_IP = CalmVariable.WithOptions.FromTask(
        CalmTask.Exec.escript.py3(
            name="",
            filename=os.path.join(
                "scripts", "Profile_Default_variable_PC_IP_Task_SampleTask.py"
            ),
        ),
        label="Please key in the Prism Central IP address",
        is_mandatory=True,
        is_hidden=False,
        description="",
    )

    account_name = CalmVariable.WithOptions.FromTask(
        CalmTask.Exec.escript.py3(
            name="",
            filename=os.path.join(
                "scripts", "Profile_Default_variable_account_name_Task_SampleTask.py"
            ),
        ),
        label="Please select the account name",
        is_mandatory=True,
        is_hidden=False,
        description="",
    )

    pc_calm_setup = CalmVariable.WithOptions(
        ["nutanix_pc", "nutanix"],
        label="",
        default="nutanix_pc",
        is_mandatory=False,
        is_hidden=True,
        runtime=False,
        description="",
    )

    CalmVM_IP = CalmVariable.Simple(
        "10.42.155.60",
        label="",
        is_mandatory=False,
        is_hidden=False,
        runtime=False,
        description="",
    )


class NKP(Blueprint):

    services = [Rocky]
    packages = [Package1]
    substrates = [Rocky_VM]
    profiles = [Default]
    credentials = [
        BP_CRED_ROCKY,
        BP_CRED_ROCKY2Credential,
        BP_CRED_PCCredential,
        BP_CRED_CalmVMCredential,
    ]


class BpMetadata(Metadata):

    project = Ref.Project("BP Design Project")
