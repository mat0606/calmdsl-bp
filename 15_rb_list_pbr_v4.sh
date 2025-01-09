sed -i 's/10.55.88.50/10.42.155.60/g' rb_list_pbr_v4/runbook.py

calm compile runbook --file rb_list_pbr_v4/runbook.py
calm create runbook --file rb_list_pbr_v4/runbook.py --name "ListPBRv4" --force
