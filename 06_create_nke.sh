echo "Create NKE Cluster"
calm update cache
calm compile bp --file create-nke/blueprint.py
calm create bp --file create-nke/blueprint.py --name create-nke --force
calm launch bp "create-nke" --app_name "create-nke-cluster mo-dev" -p "Single Master" --environment OTC
calm publish bp -v "1.0" -n "Create NKE Cluster" -w -pm -aa -p "BP Design Project" -c "Containers" "create-nke"
calm launch marketplace item -a "Create NKE Cluster" -pj "BP Design Project" -e "OTC" -p "Single Master" "Create NKE Cluster" 