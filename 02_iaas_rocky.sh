echo "Rocky VM"
calm update cache
sed -i 's/administrator@ntnxlab.local/administrator@ntnxlab1.local/g' rocky-multi-vm/blueprint.py
sed -i 's/Primary_OTC/Calm_Secondary_OTC/g' rocky-multi-vm/blueprint.py
sed -i 's/DM3-POC035/DM3-POC088/g' rocky-multi-vm/blueprint.py
sed -i 's/NTNX_LOCAL_AZ_OTC/PP Cluster/g' rocky-multi-vm/blueprint.py
sed -i 's/ntnxlab.local/ntnxlab1.local/g' rocky-multi-vm/blueprint.py
sed -i 's/10.55.35.56/10.55.88.64/g' rocky-multi-vm/blueprint.py


calm compile bp --file rocky-multi-vm/blueprint.py
calm create bp --file rocky-multi-vm/blueprint.py --name RockyAD --force
calm launch bp "RockyAD" --app_name RockyAD --environment OTC
calm publish bp -v "1.0" -n "Rocky 9 Linux" -w -pm -aa -p "BP Design Project" -c "BI-Productivity" "RockyAD"
calm launch marketplace item -a "Rocky9-3" -pj "BP Design Project" -e "ITC" -p "Small" "Rocky 9 Linux" 
