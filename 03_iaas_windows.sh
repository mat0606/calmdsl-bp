echo "Windows VM"
calm update cache
calm compile bp --file windows-single-vm/blueprint.py
calm create bp --file windows-single-vm/blueprint.py --name Windows2022AD --force
calm launch bp "Windows2022AD" --app_name Windows2022 -p "Default" --environment ITC


calm compile bp --file win-multi-vm/blueprint.py
calm create bp --file win-multi-vm/blueprint.py --name Windows2022AD --force
calm launch bp "Windows2022AD" --app_name Windows2022-3 -p "Small" --environment OTC
calm launch bp "Windows2022AD" --app_name Windows2022-Medium -p "Medium" --environment OTC
calm launch bp "Windows2022AD" --app_name Windows2022-Large -p "Large" --environment OTC
calm publish bp -v "1.0" -n "Windows 2022" -w -pm -aa -p "BP Design Project" -c "BI-Productivity" "Windows2022AD"
calm launch marketplace item -a "Windows2022-2" -pj "BP Design Project" -e "ITC" -p "Small" "Windows 2022" 