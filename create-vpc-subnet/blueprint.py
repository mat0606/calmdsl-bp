# THIS FILE IS AUTOMATICALLY GENERATED.
# Disclaimer: Please test this file before using in production.
"""
Generated blueprint DSL (.py)
"""

import json  # no_qa
import os  # no_qa

from calm.dsl.builtins import *  # no_qa


# Secret Variables

BP_CRED_PCCredential_PASSWORD = read_local_file("BP_CRED_PCCredential_PASSWORD")

# Credentials
BP_CRED_PCCredential = basic_cred(
    "admin",
    BP_CRED_PCCredential_PASSWORD,
    name="PC Credential",
    type="PASSWORD",
    default=True,
)


class Service1(Service):
    @action
    def CreateVPC(name="Create VPC"):

        CalmTask.SetVariable.escript.py2(
            name="GetNetworkUUID",
            filename=os.path.join(
                "scripts", "Service_Service1_Action_CreateVPC_Task_GetNetworkUUID.py"
            ),
            target=ref(Service1),
            variables=["pe_network_UUID"],
        )

        CalmTask.SetVariable.escript.py2(
            name="Split external routable ip",
            filename=os.path.join(
                "scripts",
                "Service_Service1_Action_CreateVPC_Task_Splitexternalroutableip.py",
            ),
            target=ref(Service1),
            variables=["ext_routable_ip", "ext_routable_ip_prefix"],
        )

        CalmTask.SetVariable.escript.py2(
            name="Invoke API to create VPC",
            filename=os.path.join(
                "scripts",
                "Service_Service1_Action_CreateVPC_Task_InvokeAPItocreateVPC.py",
            ),
            target=ref(Service1),
            variables=["vpc_uuid"],
        )

        CalmTask.Exec.escript.py2(
            name="Check for VPC",
            filename=os.path.join(
                "scripts", "Service_Service1_Action_CreateVPC_Task_CheckforVPC.py"
            ),
            target=ref(Service1),
        )

    @action
    def DeleteVPC(name="Delete VPC"):

        CalmTask.SetVariable.escript.py2(
            name="Get VPC UUID",
            filename=os.path.join(
                "scripts", "Service_Service1_Action_DeleteVPC_Task_GetVPCUUID.py"
            ),
            target=ref(Service1),
            variables=["vpc_uuid"],
        )

        CalmTask.Exec.escript.py2(
            name="Invoke API to delete VPC",
            filename=os.path.join(
                "scripts",
                "Service_Service1_Action_DeleteVPC_Task_InvokeAPItodeleteVPC.py",
            ),
            target=ref(Service1),
        )

        CalmTask.Exec.escript.py2(
            name="Check for VPC",
            filename=os.path.join(
                "scripts", "Service_Service1_Action_DeleteVPC_Task_CheckforVPC.py"
            ),
            target=ref(Service1),
        )

    @action
    def CreateSubnetinVPC(name="Create Subnet in VPC"):

        CalmTask.SetVariable.escript.py2(
            name="Get VPC UUID",
            filename=os.path.join(
                "scripts",
                "Service_Service1_Action_CreateSubnetinVPC_Task_GetVPCUUID.py",
            ),
            target=ref(Service1),
            variables=[],
        )

        CalmTask.SetVariable.escript.py2(
            name="Split Network IP Prefix",
            filename=os.path.join(
                "scripts",
                "Service_Service1_Action_CreateSubnetinVPC_Task_SplitNetworkIPPrefix.py",
            ),
            target=ref(Service1),
            variables=["network_ip", "network_ip_prefix"],
        )

        CalmTask.Exec.escript.py2(
            name="Create Subnet in VPC",
            filename=os.path.join(
                "scripts",
                "Service_Service1_Action_CreateSubnetinVPC_Task_CreateSubnetinVPC.py",
            ),
            target=ref(Service1),
        )

        CalmTask.Exec.escript.py2(
            name="Check Subnet",
            filename=os.path.join(
                "scripts",
                "Service_Service1_Action_CreateSubnetinVPC_Task_CheckSubnet.py",
            ),
            target=ref(Service1),
        )

    @action
    def DeleteSubnetinVPC(name="Delete Subnet in VPC"):

        CalmTask.SetVariable.escript.py2(
            name="Get Subnet UUID",
            filename=os.path.join(
                "scripts",
                "Service_Service1_Action_DeleteSubnetinVPC_Task_GetSubnetUUID.py",
            ),
            target=ref(Service1),
            variables=["subnet_uuid"],
        )

        CalmTask.Exec.escript.py2(
            name="Delete Subnet",
            filename=os.path.join(
                "scripts",
                "Service_Service1_Action_DeleteSubnetinVPC_Task_DeleteSubnet.py",
            ),
            target=ref(Service1),
        )


class VM1(Substrate):

    os_type = "Linux"
    provider_type = "EXISTING_VM"
    provider_spec = read_provider_spec(os.path.join("specs", "VM1_provider_spec.yaml"))

    readiness_probe = readiness_probe(
        connection_type="SSH",
        disabled=True,
        retries="5",
        connection_port=22,
        address="@@{ip_address}@@",
        delay_secs="60",
        credential=ref(BP_CRED_PCCredential),
    )


class Package1(Package):

    services = [ref(Service1)]

    @action
    def __install__():

        Service1.CreateVPC(name="Create VPC")

        Service1.CreateSubnetinVPC(name="Create Subnet in VPC")

        CalmTask.Exec.escript.py2(
            name="Create Static Route for VPC",
            filename=os.path.join(
                "scripts",
                "Package_Package1_Action___install___Task_CreateStaticRouteforVPC.py",
            ),
            target=ref(Service1),
        )

    @action
    def __uninstall__():

        Service1.DeleteSubnetinVPC(name="Delete Subnet in VPC")

        Service1.DeleteVPC(name="Delete VPC")


class ab0869f2_deployment(Deployment):

    min_replicas = "1"
    max_replicas = "1"
    default_replicas = "1"

    packages = [ref(Package1)]
    substrate = ref(VM1)


class Default(Profile):

    deployments = [ab0869f2_deployment]

    PC_IP = CalmVariable.Simple(
        "10.42.110.39",
        label="",
        is_mandatory=True,
        is_hidden=False,
        runtime=True,
        description="",
    )

    End_IP = CalmVariable.Simple(
        "192.168.1.125",
        label="Please key in the end address for this network",
        is_mandatory=True,
        is_hidden=False,
        runtime=True,
        description="",
    )

    Start_IP = CalmVariable.Simple(
        "192.168.1.10",
        label="Please key in the start address for this network",
        is_mandatory=True,
        is_hidden=False,
        runtime=True,
        description="",
    )

    Network_IP_Prefix = CalmVariable.Simple(
        "192.168.1.0/24",
        label="Please key in the Network IP Prefix for the Subnet",
        is_mandatory=True,
        is_hidden=False,
        runtime=True,
        description="",
    )

    Gateway_IP = CalmVariable.Simple(
        "192.168.1.1",
        label="Please key in the Gateway IP for the Subnet in VPC",
        is_mandatory=True,
        is_hidden=False,
        runtime=True,
        description="",
    )

    subnet_name = CalmVariable.Simple(
        "",
        label="Please key in the Subnet Name for this VPC",
        is_mandatory=True,
        is_hidden=False,
        runtime=True,
        description="",
    )

    dns = CalmVariable.Simple(
        "10.38.178.52",
        label="Please key in the DNS.  ",
        is_mandatory=True,
        is_hidden=False,
        runtime=True,
        description="DNS is advertised to Guest VMs via DHCP.",
    )

    external_routable_ip = CalmVariable.Simple(
        "",
        label="Please key in the external routable IP",
        is_mandatory=False,
        is_hidden=True,
        runtime=False,
        description="",
    )

    external_subnet = CalmVariable.WithOptions.FromTask(
        CalmTask.Exec.escript.py2(
            name="",
            filename=os.path.join(
                "scripts", "Profile_Default_variable_external_subnet_Task_SampleTask.py"
            ),
        ),
        label="Please select external subnet",
        is_mandatory=True,
        is_hidden=False,
        description="",
    )

    vpc_name = CalmVariable.Simple(
        "",
        label="Please key in the VPC name",
        is_mandatory=True,
        is_hidden=False,
        runtime=True,
        description="",
    )

    @action
    def CreateVPC(name="Create VPC"):

        Service1.CreateVPC(name="Create VPC")

    @action
    def DeleteVPC(name="Delete VPC"):

        Service1.DeleteVPC(name="Delete VPC")


class CreateVPCandSubnet20240228(Blueprint):

    services = [Service1]
    packages = [Package1]
    substrates = [VM1]
    profiles = [Default]
    credentials = [BP_CRED_PCCredential]