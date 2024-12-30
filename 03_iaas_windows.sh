echo "Windows VM"
calm update cache
# Single Windows VM with VPC
sed -i 's/administrator@ntnxlab.local/administrator@ntnxlab1.local/g' windows-single-vm/blueprint.py
sed -i 's/Primary_OTC/Calm_Secondary_OTC/g' windows-single-vm/blueprint.py
sed -i 's/DM3-POC035/DM3-POC088/g' windows-single-vm/blueprint.py
sed -i 's/PP Cluster/NTNX_LOCAL_AZ_OTC/g' windows-single-vm/blueprint.py
sed -i 's/ntnxlab.local/ntnxlab1.local/g' windows-single-vm/blueprint.py
sed -i 's/10.55.88.64/10.55.88.59/g' windows-single-vm/blueprint.py

calm compile bp --file windows-single-vm/blueprint.py
calm create bp --file windows-single-vm/blueprint.py --name Windows2022AD --force
calm launch bp "Windows2022AD" --app_name Windows2022 -p "Default" --environment ITC

sed -i 's/administrator@ntnxlab.local/administrator@ntnxlab1.local/g' win-multi-vm/blueprint.py
sed -i 's/Primary_OTC/Calm_Secondary_OTC/g' win-multi-vm/blueprint.py
sed -i 's/DM3-POC035/DM3-POC088/g' win-multi-vm/blueprint.py
sed -i 's/PP Cluster/NTNX_LOCAL_AZ_OTC/g' win-multi-vm/blueprint.py
sed -i 's/ntnxlab.local/ntnxlab1.local/g' win-multi-vm/blueprint.py
sed -i 's/10.55.35.56/10.55.88.59/g' win-multi-vm/blueprint.py

calm compile bp --file win-multi-vm/blueprint.py
calm create bp --file win-multi-vm/blueprint.py --name Windows2022AD --force
calm launch bp "Windows2022AD" --app_name Windows2022-3 -p "Small" --environment OTC
calm launch bp "Windows2022AD" --app_name Windows2022-Medium -p "Medium" --environment OTC
calm launch bp "Windows2022AD" --app_name Windows2022-Large -p "Large" --environment OTC
calm publish bp -v "1.0" -n "Windows 2022" -w -pm -aa -p "BP Design Project" -c "BI-Productivity" "Windows2022AD"
calm launch marketplace item -a "Windows2022-2" -pj "BP Design Project" -e "ITC" -p "Small" "Windows 2022" 