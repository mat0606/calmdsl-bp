import re


TENANT_TAG = '@@{TENANT_TAG}@@'
username = '@@{calm_username}@@'

if 'admin' in username.lower() and TENANT_TAG:
    tenant_tag = TENANT_TAG

else:
    project_name = '@@{calm_project_name}@@'
    print('User "{}" running in Project "{}".'.format(username, project_name))

    iii_pattern = '[a-z]{2}\d{3}[a-z]'  # 2 letters, 3 digits, 1 letter
    username_search = re.findall(iii_pattern, username)

    if username_search:
        tenant_tag = username_search[0]
        user_source = 'iii'
    else:
        tenant_tag = project_name.replace('_onboarding_project', '')
        user_source = 'ooo'    

print('tenant_tag={}'.format(tenant_tag))
#print('user_source={}'.format(user_source))