echo "Onboard Tenant VPC"
calm update cache
calm compile bp --file onboard-project-vpc/blueprint.py
calm create bp --file onboard-project-vpc/blueprint.py --name OnboardTenantVPC --force
calm launch bp "OnboardTenantVPC" --app_name "Onboard Tenant Test Tenant" --environment ITC
calm publish bp -v "1.0" -n "Onboard Tenant VPC" -w -pm -aa -p "BP Design Project" -c "BI-Productivity" "OnboardTenantVPC"
calm launch marketplace item -a "Onboard Tenant 1" -pj "BP Design Project" -e "ITC" -p "Default" "Onboard Tenant VPC" 
