echo "RHEL VM"
calm update cache
calm compile bp --file rhel-multi-vm/blueprint.py
calm create bp --file rhel-multi-vm/blueprint.py --name RHELAD --force
calm launch bp "RHELAD" --app_name RHELAD -p "Small" --environment OTC_RH
calm publish bp -v "1.0" -n "RHEL 9 Linux" -w -pm -aa -p "BP Design Project" -c "BI-Productivity" "RHELAD"
calm launch marketplace item -a "RHEL9-2" -pj "BP Design Project" -e "ITC_RH" -p "Small" "RHEL 9 Linux" 
