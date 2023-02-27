# Bulk_mail_sender
This python script can be used to send emails to multiple ids using Gmail services.

# Working 
It is a simple script that uses the smtplib library services to connect the local system to Gmail services and hence
send the same email to multiple ids in a bulk. It requires a predefined csv or excel file with the email ids in a single 
coloumn for them to be accessed. 
The data access location needs to be changed as per the schema of the csv file.
Moreover the for loop is placed so that the id does not get classified as spam, hence it is a necessity for not to be removed.
Additonaly a sleep function can be used to increase the times between outgoing-mails as well.

## Run Locally
Clone the project

```bash
  git clone https://github.com/Demogorgon24242/bulk_mail_sender.git
```

Go to the project directory

```bash
  cd main1.py
```
