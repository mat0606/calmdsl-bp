# Temporary approach for multi-clusters managed by PC.  Synchronize the password for all PE clusters and get rid of this.

if "@@{nutanix_cluster}@@ == PHX-POC080":
  print ("pe_sc_credential=@@{PE_SC_Creds.secret}@@")
elif "@@{nutanix_cluster}@@ == PHX-POC027":
  print ("pe_sc_credential=@@{PE_SC_Creds2.secret}@@")
elif "@@{nutanix_cluster}@@ == PHX-POC169":
  print ("pe_sc_credential=@@{PE_SC_Creds3.secret}@@")
elif "@@{nutanix_cluster}@@ == PHX-POC171":
  print ("pe_sc_credential=@@{PE_SC_Creds4.secret}@@")
elif "@@{nutanix_cluster}@@  == PHX-POC296":
  print ("pe_sc_credential=@@{PE_SC_Creds5.secret}@@")
else:
  print ("No credential matches the selected Nutanix cluster.  Please look and change the source code")
  exit(1)