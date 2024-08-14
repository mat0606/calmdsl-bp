echo "Create VPC and Subnet"
calm update cache
calm compile bp --file create-vpc-subnet/blueprint.py
calm create bp --file create-vpc-subnet/blueprint.py --name CreateVPCSubnet --force
calm launch bp "CreateVPCSubnet" --app_name "Create Test VPC 01" --environment ITC
calm publish bp -v "1.0" -n "Create VPC and Subnet" -w -pm -aa -p "BP Design Project" -c "Networking" "CreateVPCSubnet"
calm launch marketplace item -a "Create vPC 02" -pj "BP Design Project" -e "ITC" -p "Default" "Create VPC and Subnet" 
