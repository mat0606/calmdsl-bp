sed -i 's/10.55.88.50/10.42.155.60/g' rb_list_vm_metric_v4/runbook.py

calm compile runbook --file rb_list_vm_metric_v4/runbook.py
calm create runbook --file rb_list_vm_metric_v4/runbook.py --name "ListVMMetricv4" --force
