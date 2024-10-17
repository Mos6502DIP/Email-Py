from emailpy import emails as ep

sending_address = '<EMAIL>'  # The email address you are sending from
password = '<PASSWORD>'  # Get passkey for the email address more info in README

receiving_address = '<EMAIL>'  # Email address your sending to
subject = 'Test email'
message = 'This is a test email Hello world!'

ep.send_email(sending_address, password, receiving_address, subject, message)

