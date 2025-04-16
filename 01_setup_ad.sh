echo "Updating CalmDSL cache"
calm update cache

sed -i 's/DM3-POC088/PHX-POC155/g' install-ad-multi-vm/blueprint.py
sed -i 's/NTNX_LOCAL_AZ_OTC/NTNX_LOCAL_AZ_ITC/g' install-ad-multi-vm/blueprint.py
sed -i 's/ntnxlab1.local/ntnxlab2.local/g' install-ad-multi-vm/blueprint.py

echo "Setting up AD and DNS"
calm compile bp --file install-ad-multi-vm/blueprint.py
calm create bp --file install-ad-multi-vm/blueprint.py --name Install-AD-DNS
calm launch bp "Install-AD-DNS" --app_name AD-DNS --environment OTC



