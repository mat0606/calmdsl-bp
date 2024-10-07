echo "Create NKP Cluster"
calm update cache
calm compile bp --file nkp/blueprint.py
calm create bp --file nkp/blueprint.py --name NKP --force
calm launch bp "NKP" --app_name "Install NKP" -p "Default" --environment OTC
calm publish bp -v "1.0" -n "Provision NKP Management Cluster" -w -pm -aa -p "BP Design Project" -c "Containers" "NKP"
calm launch marketplace item -a "Install NKP2" -pj "BP Design Project" -e "OTC" -p "Default" "Provision NKP Management Cluster" 