echo "Rocky VM"
calm update cache
sed -i 's/administrator@ntnxlab.local/administrator@ntnxlab1.local/g' rocky-single-vm/blueprint.py
sed -i 's/test-subnet/SG-AMK/g' rocky-single-vm/blueprint.py
sed -i 's/testvpc/SingaporeVPC/g' rocky-single-vm/blueprint.py
sed -i 's/DM3-POC035/DM3-POC088/g' rocky-single-vm/blueprint.py
sed -i 's/PP Cluster/NTNX_LOCAL_AZ_ITC/g' rocky-single-vm/blueprint.py
sed -i 's/ntnxlab.local/ntnxlab1.local/g' rocky-single-vm/blueprint.py
sed -i 's/10.55.88.64/10.55.88.59/g' rocky-single-vm/blueprint.py


calm compile bp --file rocky-single-vm/blueprint.py
calm create bp --file rocky-single-vm/blueprint.py --name "Rocky 9 in VPC" --force
calm launch bp "Rocky 9 in VPC" --app_name "Rocky 9 in VPC" --environment ITC
calm publish bp -v "1.0" -n "Rocky 9 Linux in VPC" -w -pm -aa -p "BP Design Project" -c "BI-Productivity" "Rocky 9 in VPC"
calm launch marketplace item -a "Rocky9-3" -pj "BP Design Project" -e "ITC" -p "Small" "Rocky 9 Linux in VPC" 
