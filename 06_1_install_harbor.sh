calm compile bp --file harbor/blueprint.py
calm create bp --file harbor/blueprint.py --name Harbor --force
calm launch bp "Harbor" --app_name "Install Harbor" -p "Default" --environment ITC_VLAN