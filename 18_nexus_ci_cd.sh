calm compile bp --file nexus_ci_cd/blueprint.py
calm create bp --file nexus_ci_cd/blueprint.py --name nexus-ci-cd --force
calm launch bp "nexus-ci-cd" --app_name "MRP_DEV_ENV_GP1" --environment ITC_VLAN