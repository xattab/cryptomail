# InstallL

You need two dependencies:

    # pip install gnupg pysocks

# Usage

You need to either modify or create a YAML config file. Each file contains the details
of the mail account and the recipients. You can make one config file for each "newsletter"
so to speak. Here's an example:

    tor: yes
    host: mail.yourdomain.com
    port: 587
    user: you@yourdomain.com
    pwd: yourpassword
    from: noreply@yourdomain.com
    recipients:
        - someone@youknow.com
        - someone.else@youknow.com

Then you need to create an email file:

    Subject: This is the email subject

    This is the email body, starts after a line break.

You can now send the emails like this:

    $ python cryptoletter.py --config news.yaml /tmp/email.txt

If no --config is specified, it will attempt to use `config.yaml` in the local folder.

