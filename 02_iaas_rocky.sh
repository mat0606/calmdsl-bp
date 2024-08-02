echo "Rocky VM"
calm update cache
calm compile bp --file rocky-multi-vm/blueprint.py
calm create bp --file rocky-multi-vm/blueprint.py --name RockyAD --force
calm launch bp "RockyAD" --app_name RockyAD --environment OTC
calm publish bp -v "1.0" -n "Rocky 9 Linux" -w -pm -aa -p "BP Design Project" -c "BI-Productivity" "RockyAD"
