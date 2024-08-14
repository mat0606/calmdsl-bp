echo "Install MetalLB in NKE Cluster"
calm update cache
calm compile bp --file metal-lb/blueprint.py
calm create bp --file metal-lb/blueprint.py --name install-metallb-nke --force
calm launch bp "install-metallb-nke" --app_name "Install MetalLB on mo-dev cluster" -p "Default" --environment OTC
calm publish bp -v "1.0" -n "Install MetalLB in NKE Cluster" -w -pm -aa -p "BP Design Project" -c "Containers" "install-metallb-nke"
calm launch marketplace item -a "Install MetalLB in NKE Cluster" -pj "BP Design Project" -e "OTC" -p "Single Master" "Install MetalLB in NKE Cluster" 