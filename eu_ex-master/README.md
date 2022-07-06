English | [简体中文](README_sc.md)
# eu_ex

eu_ex means EUserv_extend. A Python script which can help you renew your free EUserv IPv6 VPS.

This Script can check the VPS amount in your account automatically and renew the VPS if it can be renewed.

## How to Use

1. Install Python3 and dependences, the following command is used in debian/ubuntu for example,

   ```bash
   #Install Python3
   apt install python3 python3-pip -y
   #Intstall dependences
   pip install requests beautifulsoup4
   ```

2. It is not recommended to replace the `USERNAME` & `PASSWORD` parameters with yours in `main.py` Line 37-38 directly. Pass them in from environment variables.

   Your can add multiple accounts with single space separated.

3. Your can add multiple mailparser.io parsed data download URL id with single space separated. The download URL id is in `https://files.mailparser.io/d/<download_url_id>`.

4. Pass the **Actions secrets** into the environment variable of your GitHub Action runtime environment. For example, the following environment variables are required.

   ```
   env:
       USERNAME: ${{ secrets.USERNAME }}
       PASSWORD: ${{ secrets.PASSWORD }}
       # https://mailparser.io   
       MAILPARSER_DOWNLOAD_URL_ID: ${{ secrets.MAILPARSER_DOWNLOAD_URL_ID }}
   ```

## Mail forwarding and mailparser settings
### Mail forwarding

Take gmail as an example, forward emails to [mailparser](https://mailparser.io). It is possible for non-gmail mailboxes to receive emails from euserv, provided that they can be received. Currently outlook/hotmail does not receive it.

- ![gmail_filter_keys](./images/gmail_filter_keys.png)

- ![gmail_filter_setting](./images/gmail_filter_setting.png)

- ![gmail_forward_setting](./images/gmail_forward_setting.png)

### Mailparser settings

- Create new inbox firstly.
- Create data parsing rules.
  - mailparser_data_parsing_rules
   ![mailparser_data_parsing_rules](./images/mailparser_data_parsing_rules.png)
  - mailparser_data_parsing_rules_pin
  ![mailparser_data_parsing_rules_pin](./images/mailparser_data_parsing_rules_pin.png)
  - mailparser_data_parsing_rules_subject
  ![mailparser_data_parsing_rules_subject](./images/mailparser_data_parsing_rules_subject.png)
  - mailparser_data_parsing_rules_sender
  ![mailparser_data_parsing_rules_sender](./images/mailparser_data_parsing_rules_sender.png)
  - mailparser_data_parsing_rules_receiver
  ![mailparser_data_parsing_rules_receiver](./images/mailparser_data_parsing_rules_receiver.png)
- Create parsed data download url
  - mailparser_parsed_data_downloads
  ![mailparser_parsed_data_downloads](./images/mailparser_parsed_data_downloads.png)
- mailparser_parsed_data_downloads_setting
  ![mailparser_parsed_data_downloads_setting](./images/mailparser_parsed_data_downloads_setting.png)
- Settings
  - mailparser_inbox_setting_1
  ![mailparser_inbox_setting_1](./images/mailparser_inbox_setting_1.png)
  - mailparser_inbox_setting_2
  ![mailparser_inbox_setting_2](./images/mailparser_inbox_setting_2.png)

## Final result
The effect is as shown,

![mailparser_inbox_setting_2](./images/the_final_effect.png)

## TODO

- [x] ~~Validate the `receiver` field parsed by mailparser to reduce malicious email interference.~~ Won't do due to mailparser *Inbox Settings - Email Reception*.
- [ ] Open pre-trained models to solve the problem of CAPTCHA recognition locally.
- [ ] Log internationalization and localization.

## Acknowledgement

- Thanks EUserv provides us free IPv6 VPS for learning.
- Thanks CokeMine & its repository contributors provides us the original *EUserv_extend* script .The internet never forgets, but people do.

## Q&A

1. **Q**: It can be non-gmail mailbox?

   **A**: Can be a non-gmail mailbox，the prerequisite is to receive emails from euserv. Currently outlook/hotmail does not receive it.

2. **Q**: Can n mailboxes use the same mailparser or do I need to apply for n mailparsers to correspond with one?

   **A**: The mailparser free account can set up to 10 inboxes, and these 10 inboxes can correspond to 10 euserv accounts, and there are 10 mailparser parsed data download URLs(ids). So, it depends on whether you have n>10, or n<10. n<10, one mailparsed account is enough, and then the parsed data download URL ids correspond to the registered email accounts of euserv.

3. **Q**: How eu_ex script works?

   **A**: EUserv set the first threshold from the end of September 2021, that is, the login verification code (successful verification status maintained for 24 hours), so from now on, we use the API provided by TrueCaptcha (there is a free amount every day) to identify. Not long after, about the beginning of November 2021, EUserv set a second threshold, which is the email PIN verification when renewing, and here the solution is about two kinds: a. Login to the mailbox to get the email containing EUserv PIN. b. Convert the email into HTTP REST API to get it automatically. Option b is adopted here. It seems that only [Mailparser](https://mailparser.io) and [Zapier Emails Parser](https://parser.zapier.com/) are available in option b for free quota. Option b is clearly better than option a.

## References

### EUserv "PIN for the Confirmation of a Security Check" original mail

```
From：	     EUserv Support <support@euserv.de>
To：	         xyz@example.com
Subject：	 EUserv - PIN for the Confirmation of a Security Check
Content-Type: text/plain; charset = utf-8
Dear XYZ,

you have just requested a PIN for confirmation of a security check at EUserv. If you have not requested the PIN then ignore this email.

PIN:
123456

PLEASE NOTE: If you already have requested a new PIN for the same process this PIN is invalid. Also this PIN is only valid within the session in which it has been requested. This means the PIN is invalid if you for example change the browser or if you logout and perform a new login.


Sincerely,
Your customer support EUserv

--
Web ................: http://www.euserv.com
Login control panel.: https://support.euserv.com
FAQ ................: http://faq.euserv.com
Help & Guides.......: http://wiki.euserv.com
Community / Forum...: http://forum.euserv.com
Mailing-Liste ......: http://www.euserv.com/en/?show_contact=mailinglist
Twitter ............: http://twitter.com/euservhosting
Facebook ...........: http://www.facebook.com/euservhosting
--

EUserv Internet
is a division of
ISPpro Internet KG

Postal address:
ISPpro Internet KG
Division EUserv Internet
P.O. Box 2224
07622 Hermsdorf
GERMANY

Support-Phone: +49 (0) 3641 3101011 (English speaking)

Administration:
ISPpro Internet KG
Neue Str. 4
D-07639 Bad Klosterlausnitz
GERMANY

Management...............: Dirk Seidel
Register.................: AG Jena, HRA 202638
VAT Number...............: 162/156/36600
Tax office ..............: Jena
International VAT Number.: DE813856317
```

