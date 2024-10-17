echo "RHEL Single VM in VPC"
calm update cache
calm compile bp --file rhel-vpc-single-vm/blueprint.py
calm create bp --file rhel-vpc-single-vm/blueprint.py --name RHEL_SingleVM --force
calm launch bp "RHEL_SingleVM" --app_name "RHEL 9 in testvpc" -p "Default" --environment ITC_RH
calm publish bp -v "1.0" -n "RHEL 9 Linux in VPC" -w -pm -aa -p "BP Design Project" -c "BI-Productivity" "RHEL_SingleVM"
calm launch marketplace item -a "RHEL9-2" -pj "BP Design Project" -e "ITC_RH" -p "Default" "RHEL 9 Linux in VPC" 
