opt=input("Enter your E-mail id :: ").strip()
username=opt[:opt.index('@')]
domain=opt[opt.index('@')+1:]
print("User name :: ",username)
print("Domain name :: ",domain)