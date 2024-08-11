echo "Create Bucket"
calm update cache
calm compile bp --file create-bucket/blueprint.py
calm create bp --file create-bucket/blueprint.py --name create-bucket --force
calm launch bp "create-bucket" --app_name create-bucket -p "Default" --environment OTC
calm publish bp -v "1.0" -n "Create Objects Bucket" -w -pm -aa -p "BP Design Project" -c "BI-Productivity" "create-bucket"
calm launch marketplace item -a "Create Objects Bucket" -pj "BP Design Project" -e "OTC" -p "Default" "Create Objects Bucket" 