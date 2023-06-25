
email =  input('Enter your email: ')

username,domain = email.split('@')
domain,extention = domain.split('.')

print("username: " + username)
print(f"Domain: {domain}")
print(f"Extension: {extention}")
