echo "Updating CalmDSL cache"
calm update cache
echo "Setting up AD and DNS"
calm compile bp --file install-ad-multi-vm/blueprint.py
calm create bp --file install-ad-multi-vm/blueprint.py --name Install-AD-DNS
calm launch bp "Install-AD-DNS" --app_name AD-DNS --environment OTC



