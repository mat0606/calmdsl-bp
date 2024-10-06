echo "Install SNOW Mid Server"
calm update cache
calm compile bp --file snow_mid_server/blueprint.py
calm create bp --file snow_mid_server/blueprint.py --name SNOWMidServer --force
calm launch bp "SNOWMidServer" --app_name "Install SNOW Mid Server" --environment OTC
calm publish bp -v "1.0" -n "Install SNOW Mid Server" -w -pm -aa -p "BP Design Project" -c "BI-Productivity" "SNOWMidServer"
calm launch marketplace item -a "Install SNOW Mid Server" -pj "BP Design Project" -e "OTC" -p "Default" "Install SNOW Mid Server" 
