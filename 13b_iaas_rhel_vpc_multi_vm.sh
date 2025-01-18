echo "RHEL Multi VM in VPC"
calm update cache

sed -i 's/rhel92-calm-template.qcow2/rhel95-calm-template.qcow2/g' rhel-vpc-multi-vm/blueprint.py
sed -i 's/testvpc1/SingaporeVPC/g' rhel-vpc-multi-vm/blueprint.py
sed -i 's/subnet1/SG-AMK/g' rhel-vpc-multi-vm/blueprint.py

calm compile bp --file rhel-vpc-multi-vm/blueprint.py
calm create bp --file rhel-vpc-multi-vm/blueprint.py --name RHEL_VPC_Multi_VM --force
calm launch bp "RHEL_VPC_Multi_VM" --app_name "RHEL 9 in SingaporeVPC" -p "Small" --environment ITC_RH
calm publish bp -v "1.0" -n "RHEL 9 Multi VM in VPC" -w -pm -aa -p "BP Design Project" -c "BI-Productivity" "RHEL_VPC_Multi_VM"
calm launch marketplace item -a "RHEL9-2 in Singapore VPC" -pj "BP Design Project" -e "ITC_RH" -p "Default" "RHEL 9 Multi VM in VPC" 
