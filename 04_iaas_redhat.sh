echo "RHEL VM"
calm update cache
sed -i 's/administrator@ntnxlab.local/administrator@ntnxlab1.local/g' rhel-multi-vm/blueprint.py
sed -i 's/Primary_OTC/Calm_Secondary_OTC/g' rhel-multi-vm/blueprint.py
sed -i 's/DM3-POC035/DM3-POC088/g' rhel-multi-vm/blueprint.py 
sed -i 's/ntnxlab.local/ntnxlab1.local/g' rhel-multi-vm/blueprint.py
sed -i 's/10.55.35.56/10.55.88.59/g' rhel-multi-vm/blueprint.py

calm compile bp --file rhel-multi-vm/blueprint.py
calm create bp --file rhel-multi-vm/blueprint.py --name RHELAD --force
calm launch bp "RHELAD" --app_name RHELAD -p "Small" --environment OTC_RH
calm publish bp -v "1.0" -n "RHEL 9 Linux" -w -pm -aa -p "BP Design Project" -c "BI-Productivity" "RHELAD"
calm launch marketplace item -a "RHEL9-2" -pj "BP Design Project" -e "OTC_RH" -p "Small" "RHEL 9 Linux" 
