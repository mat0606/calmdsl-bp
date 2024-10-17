echo "RHEL Single VM in VPC"
calm update cache

sed -i 's/administrator@ntnxlab.local/administrator@ntnxlab1.local/g' rhel-vpc-single-vm/blueprint.py
sed -i 's/SG-AMK/test-subnet/g' rhel-vpc-single-vm/blueprint.py
sed -i 's/SingaporeVPC/testvpc/g' rhel-vpc-single-vm/blueprint.py
sed -i 's/PHX-POC071/PHX-POC155/g' rhel-vpc-single-vm/blueprint.py
sed -i 's/ntnxlab.local/ntnxlab1.local/g' rhel-vpc-single-vm/blueprint.py
sed -i 's/NTNX_LOCAL_AZ_71/PP Cluster/g' rhel-vpc-single-vm/blueprint.py
sed -i 's/10.42.70.60/10.55.88.64/g' rhel-vpc-single-vm/blueprint.py


calm compile bp --file rhel-vpc-single-vm/blueprint.py
calm create bp --file rhel-vpc-single-vm/blueprint.py --name RHEL_SingleVM --force
calm launch bp "RHEL_SingleVM" --app_name "RHEL 9 in testvpc" -p "Default" --environment ITC_RH
calm publish bp -v "1.0" -n "RHEL 9 Single VM in VPC" -w -pm -aa -p "BP Design Project" -c "BI-Productivity" "RHEL_SingleVM"
calm launch marketplace item -a "RHEL9-2" -pj "BP Design Project" -e "ITC_RH" -p "Default" "RHEL 9 Single VM in VPC" 
