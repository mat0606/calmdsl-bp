echo "Install Tunnel VM"
calm update cache
# Replace CalmVM_IP
sed -i 's/10.42.155.63/10.55.88.50/g' tunnelvm/blueprint.py

calm compile bp --file tunnelvm/blueprint.py
calm create bp --file tunnelvm/blueprint.py --name TunnelVM --force
calm launch bp "TunnelVM" --app_name "Install Tunnel VM into VPC testvpc" --environment ITC
calm publish bp -v "1.0" -n "Install Tunnel VM" -w -pm -aa -p "BP Design Project" -c "Networking" "TunnelVM"
calm launch marketplace item -a "Install Tunnel VM into VPC 01" -pj "BP Design Project" -e "ITC" -p "Default" "Install Tunnel VM" 
