echo "Create NKP Cluster"
calm update cache

sed -i 's/Calm_Primary_ITC/Calm_Primary_OTC/g' nkp/blueprint.py
sed -i 's/PHX-POC155/DM3-POC088/g' nkp/blueprint.py
sed -i 's/NTNX_LOCAL_AZ_ITC/PP Cluster/g' nkp/blueprint.py
sed -i 's/10.42.155.60/10.55.35.50/g' nkp/blueprint.py



calm compile bp --file nkp/blueprint.py
calm create bp --file nkp/blueprint.py --name NKP --force
calm launch bp "NKP" --app_name "Install NKP" -p "Default" --environment ITC_VLAN
calm publish bp -v "1.0" -n "Provision NKP Management Cluster" -w -pm -aa -p "BP Design Project" -c "Containers" "NKP"
calm launch marketplace item -a "Install NKP2" -pj "BP Design Project" -e "OTC" -p "Default" "Provision NKP Management Cluster" 