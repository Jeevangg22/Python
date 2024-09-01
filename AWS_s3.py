#import boto3

#Access_AWS:(AKIATG6MGG3HEOJNL3VZ)
#Secret_AWS:(mAjsUS1MNABaQbRkhV2vgSS+Od/ziuUL75mi9w9)

"""
# Using client finding the bucket name using method
aws_management_console = boto3.session.Session(profile_name="default")
iam_console_client = aws_management_console.client('s3')

for user_group_list in iam_console_client.list_buckets()['Buckets']:
    print(user_group_list['Name'])

"""

"""
# using resource finding the bucket name 
aws_management_console = boto3.session.Session(profile_name="default")
iam_console_resource = aws_management_console.resource('s3')

for each in iam_console_resource.buckets.all():
    print(each.name)

"""

"""
# to get creation date of bucket
aws_management_console = boto3.session.Session(profile_name="default")
iam_console_client = aws_management_console.client('s3')

for user_group_list in iam_console_client.list_buckets()['Buckets']:
    print(user_group_list['CreationDate'])

"""

"""
# creating s3 bucket if not present with the specific name 

aws_management_console = boto3.session.Session(profile_name="default")
iam_console_client = aws_management_console.client('s3')

for user_group_list in iam_console_client.list_buckets()['Buckets']:
    if user_group_list['Name'] == 'for-practise-session':
        print("file found")
    else:
        response = iam_console_client.create_bucket(ACL='private',Bucket='for-practise-session')
        print(response)
        break
"""

# aws_management_console = boto3.session.Session(profile_name="default")
# iam_console_client = aws_management_console.client('s3')
# response = iam_console_client.get_object( Bucket='for-practise-session')
# print(response)

