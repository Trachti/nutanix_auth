from base64 import b64encode
username = 'username'
password = 'password'
encoded_credentials = b64encode(bytes(f'{username}:{password}',encoding='ascii')).decode('ascii')
auth_header = f'Basic {encoded_credentials}'
print(auth_header)
