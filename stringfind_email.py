print "Hi! What is your email address?"
email_add = raw_input()
at_symbol_index = email_add.find("@")
print "I found the snail at: {0}".format(at_symbol_index)
email_handle = email_add[0:at_symbol_index]
print "The email handle is: {0}".format(email_handle)
email_domain = email_add[at_symbol_index + 1:]
print "The email_domain is: {0}".format(email_domain)
