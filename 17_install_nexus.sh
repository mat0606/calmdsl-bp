
sed -i 's/administrator@ntnxlab.local/administrator@ntnxlab1.local/g' nexus-ad/blueprint.py
sed -i 's/Calm_Primary_OTC/Calm_Primary_ITC/g' nexus-ad/blueprint.py
sed -i 's/PHX-POC070/PHX-POC155/g' nexus-ad/blueprint.py
sed -i 's/NTNX_LOCAL_AZ_70/NTNX_LOCAL_AZ_ITC/g' nexus-ad/blueprint.py
sed -i 's/ntnxlab.local/ntnxlab1.local/g' nexus-ad/blueprint.py
sed -i 's/10.42.70.60/10.55.88.59/g' nexus-ad/blueprint.py
sed -i 's/centos7-calm-20240703.qcow2/rocky94-calm-template.qcow2/g' nexus-ad/blueprint.py
sed -i 's/BP_CRED_CENTOS_KEY/BP_CRED_ROCKY_KEY/g' nexus-ad/blueprint.py
sed -i 's/BP_CRED_Centos2Credential_PASSWORD/BP_CRED_ROCKY2Credential_PASSWORD/g' nexus-ad/blueprint.py
sed -i 's/BP_CRED_CENTOS/BP_CRED_ROCKY/g' nexus-ad/blueprint.py
sed -i 's/CENTOS/ROCKY/g' nexus-ad/blueprint.py
sed -i 's/BP_CRED_Centos2Credential/BP_CRED_ROCKY2Credential/g' nexus-ad/blueprint.py
sed -i 's/Centos 2 Credential/ROCKY 2 Credential/g' nexus-ad/blueprint.py

calm compile bp --file nexus-ad/blueprint.py
calm create bp --file nexus-ad/blueprint.py --name nexus-ad --force
calm launch bp "nexus-ad" --app_name "Nexus-OSS" --environment ITC