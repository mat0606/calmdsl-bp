cred_uuid = "@@{cred_uuid}@@"
cred2_uuid = "@@{cred2_uuid}@@"
cred_win_uuid = "@@{cred_win_uuid}@@"
cred_win_domain_uuid = "@@{cred_win_domain_uuid}@@"
cred_pe_uuid = "{}".format(str(uuid.uuid4())) # Prism Element Creential uuid
cred_pe_sc_uuid = "{}".format(str(uuid.uuid4())) # Prism Element Storage Class Creential uuid
cred_pc_uuid = "{}".format(str(uuid.uuid4())) # Prism Central Class Creential uuid
cred_calmvm_uuid =  "{}".format(str(uuid.uuid4())) # Calm VM Credential uuid

def getCredentialJSON(cred_name, cred_type, cred_user_name, cred_class, cred_is_secret, cred_value, cred_uuid):
  credential = {
    "name": cred_name,
    "type": cred_type,
    "username": cred_user_name,
    "cred_class": cred_class,
    "secret": {
      "attrs": {
        "is_secret_modified": cred_is_secret,
        "secret_reference": {}
      },
      "value": cred_value
    },
    "uuid": cred_uuid
    
  }
  return credential
  
credential_list = []

credential_list.append(getCredentialJSON(
    "Centos Credential",
    "KEY",
    "centos",
    "static",
    True,
    "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAii7qFDhVadLx5lULAG/ooCUTA/ATSmXbArs+GdHxbUWd/bNGZCXnaQ2L1mSVVGDxfTbSaTJ3En3tVlMtD2RjZPdhqWESCaoj2kXLYSiNDS9qz3SK6h822je/f9O9CzCTrw2XGhnDVwmNraUvO5wmQObCDthTXc72PcBOd6oa4ENsnuY9HtiETg29TZXgCYPFXipLBHSZYkBmGgccAeY9dq5ywiywBJLuoSovXkkRJk3cd7GyhCRIwYzqfdgSmiAMYgJLrz/UuLxatPqXts2D8v1xqR9EPNZNzgd4QHK4of1lqsNRuz2SxkwqLcXSw0mGcAL8mIwVpzhPzwmENC5OrwIBJQKCAQB++q2WCkCmbtByyrAp6ktiukjTL6MGGGhjX/PgYA5IvINX1SvtU0NZnb7FAntiSz7GFrODQyFPQ0jL3bq0MrwzRDA6x+cPzMb/7RvBEIGdadfFjbAVaMqfAsul5SpBokKFLxU6lDb2CMdhS67c1K2Hv0qKLpHL0vAdEZQ2nFAMWETvVMzl0o1dQmyGzA0GTY8VYdCRsUbwNgvFMvBj8T/svzjpASDifa7IXlGaLrXfCH584zt7y+qjJ05O1G0NFslQ9n2wi7F93N8rHxglJDE4OhfyaDyLL1UdBlBpjYPSUbX7D5NExLggWEVFEwx4JRaK6+aDdFDKbSBIidHfh45NAoGBANjANRKLBtcxmW4foK5ILTuFkOaowqj+2AIgT1ezCVpErHDFg0bkuvDkQVdsAJRX5//luSO30dI0OWWGjgmIUXD7iej0sjAPJjRAv8ai+MYyaLfkdqv1Oj5coDC3KjmSdXTuWSYNvarsW+Uf2v7zlZlWesTnpV6gkZH3tX86iuiZAoGBAKM0mKX0EjFkJH65Ym7gIED2CUyuFqq4WsCUD2RakpYZyIBKZGr8MRni3I4z6Hqm+rxVW6DjuFGQe5GhgPvO23UG1Y6nm0VkYgZq81TraZc/oMzignSC95w7OsLaLn6qp32Fje1MEz2Yn0T3dDcu1twY8OoDuvWx5LFMJ3NoRJaHAoGBAJ4rZP+xj17DVElxBo0EPK7k7TKygDYhwDjnJSRSN0HfFg0agmQqXucjGuzEbyAkeN1Um9vLU+xrTHqEyIN/JqxkhztKxzfTtBhK7M84p7M5iq+0jfMau8ykdOVHZAB/odHeXLrnbrr/gVQsAKw1NdDCkPCNXP/c9JrzB+c4juEVAoGBAJGPxmp/vTL4c5OebIxnCAKWP6VBUnyWliFhdYMErECvNkjoZ2ZWjKhijVw8Il+OAjlFNgwJXzP9Z0qJIAMuHa2QeUfhmFKlo4ku9LOF2rdUbNJpKD5m+IRsLX1az4W6zLwPVRHp56WjzFJEfGiRjzMBfOxkMSBSjbLjDm3ZiUf7AoGBALjvtjapDwlEa5/CFvzOVGFq4L/OJTBEBGx/SA4HUc3TFTtlY2hvTDPZdQr/JBzLBUjCOBVuUuH3uW7hGhW+DnlzrfbfJATaRR8Ht6VU651T+Gbrr8EqNpCPgmznERCNf9Kaxl/hlyV5dZBe/2LIK+/jLGNu9EJLoraaCBFshJKF\n-----END RSA PRIVATE KEY-----\n",
    cred_uuid))
    
credential_list.append(getCredentialJSON(
    "Centos 2 Credential",
    "PASSWORD",
    "@@{Centos 2 Credential.username}@@",
    "static",
    True,
    "@@{Centos 2 Credential.secret}@@",
    cred2_uuid))

credential_list.append(getCredentialJSON(
    "WIN_VM_CRED",
    "PASSWORD",
    "@@{WIN_CRED.username}@@",
    "static",
    True,
    "@@{WIN_CRED}@@",
    cred_win_uuid))
credential_list.append(getCredentialJSON(
    "DOMAIN_CRED",
    "PASSWORD",
    "@@{DOMAIN_CRED.username}@@",
    "static",
    True,
    "@@{DOMAIN_CRED.secret}@@",
    cred_win_domain_uuid))
credential_list.append(getCredentialJSON( 
    "PE_SC_Creds",
    "PASSWORD",
    "@@{PE_SC_Creds.username}@@",
    "static",
    True,
    "@@{PE_SC_Creds.secret}@@",
    cred_pe_sc_uuid))
credential_list.append(getCredentialJSON(
    "PE_Creds",
    "PASSWORD",
    "@@{PE Credential.username}@@",
    "static",
    True,
    "@@{PE Credential.secret}@@",
    cred_pe_uuid))
credential_list.append(getCredentialJSON(
    "PC_Creds",
    "PASSWORD",
    "@@{PC Credential.username}@@",
    "static",
    True,
    "@@{PC Credential.secret}@@",
    cred_pc_uuid))  
credential_list.append(getCredentialJSON(
    "CalmVM Credential",
    "PASSWORD",
    "@@{CalmVM Credential.username}@@",
    "static",
    True,
    "@@{CalmVM Credential.secret}@@",
    cred_calmvm_uuid))       
  
print ("credential_list=" + credential_list)
