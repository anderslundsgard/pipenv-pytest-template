import boto3
from datetime import datetime, timezone

client = boto3.client('iam')

response = client.list_users()

for user in response['Users']:
    user_name = user['UserName']
    print(user_name)

    resp_access_keys = client.list_access_keys(UserName=user_name)
    for access_key in resp_access_keys['AccessKeyMetadata']:
        access_key_id = access_key['AccessKeyId']
        created_date = access_key['CreateDate']
        days_since_created = (datetime.now(timezone.utc) - created_date).days

        resp_last_used = client.get_access_key_last_used(AccessKeyId=access_key_id)
        days_since_used = -1
        if 'LastUsedDate' in resp_last_used['AccessKeyLastUsed']:
            last_used_date = resp_last_used['AccessKeyLastUsed']['LastUsedDate']
            days_since_used = (datetime.now(timezone.utc) - last_used_date).days

        tags = [f'user_name:{user_name}', f'access_key_id:{access_key_id}', f'']

        print(f' - {access_key_id}: {resp_last_used}')

    print('-----')

