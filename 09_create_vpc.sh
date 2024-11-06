echo "Create VPC and Subnet"
calm update cache
# Replace PC_IP
sed -i 's/10.55.22.40/10.42.155.39/g' create-vpc-subnet/blueprint.py
# Replace AD
sed -i 's/10.55.88.64/10.55.88.59/g' create-vpc-subnet/blueprint.py

calm compile bp --file create-vpc-subnet/blueprint.py
calm create bp --file create-vpc-subnet/blueprint.py --name CreateVPCSubnet --force
calm launch bp "CreateVPCSubnet" --app_name "Create Dev VPC" --environment ITC
calm publish bp -v "1.0" -n "Create VPC and Subnet" -w -pm -aa -p "BP Design Project" -c "Networking" "CreateVPCSubnet"
calm launch marketplace item -a "Create VPC 03" -pj "BP Design Project" -e "ITC" -p "Default" "Create VPC and Subnet" 
