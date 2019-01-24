e_mail_list = []
while True:
    local_part = input("Enter local part: ")
    domain = input("Enter domain: ")
    e_mail = "{}@{}".format(local_part, domain)
    if e_mail not in e_mail_list:
        print(e_mail)
    else:
        print("This address is already on the list")
    e_mail_list.append(e_mail)