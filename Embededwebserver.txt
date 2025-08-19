You're asking to implement a **PHP-equivalent** system that:

1. **Dumps HTML and photo files** (i.e., creates a basic static website) to a **router**.
2. **Provides access via email** — possibly meaning it **emails the link** or **allows terminal-based email access**.
3. Needs to be done in **C and Python**, as a replacement for the PHP script.

---

## ✅ Overview of the Task

We will:

* Write a **C** and **Python** program that:

  * Creates/dumps `index.html` and image files to `/www` (or equivalent) on the router.
  * Optionally compresses files (if needed).
  * Uses an email API or SMTP to send a message (with access info).
* Provide **email access via terminal** (like sending or viewing via `mailx`, `mutt`, `sendmail`, or raw SMTP).

---

## 📦 Assumptions

* Router runs **embedded Linux** (OpenWRT/LEDE/DD-WRT).
* You have **root access**.
* Basic **file system** access (`/www/` for web hosting).
* **Email system** installed or accessible via SMTP or a CLI tool.
* The router has **internet access** (to send email).

---

## 🐍 Python Version

### ✔️ Python script to:

* Dump HTML + image
* Send email via SMTP (e.g., Gmail)

```python
import os
import shutil
import smtplib
from email.message import EmailMessage

# Step 1: Write HTML content
web_dir = "/www"
os.makedirs(web_dir, exist_ok=True)

html_content = "<html><body><h1>Welcome to Your Router Website</h1><img src='image.jpg'></body></html>"
html_path = os.path.join(web_dir, "index.html")

with open(html_path, "w") as f:
    f.write(html_content)

# Step 2: Copy image to web folder
shutil.copy("local_image.jpg", os.path.join(web_dir, "image.jpg"))

# Step 3: Send email with access info
def send_email():
    msg = EmailMessage()
    msg['Subject'] = "Your Router Website is Live"
    msg['From'] = "your_email@gmail.com"
    msg['To'] = "recipient@example.com"
    msg.set_content("Your website is now live at http://192.168.1.1\n\nLogin via terminal if needed.")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login("your_email@gmail.com", "your_app_password")
            smtp.send_message(msg)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Email failed: {e}")

send_email()
```

> **Note:** Use Gmail App Passwords if 2FA is enabled. You could also use a local SMTP server if available on the router.

---

## 👨‍💻 C Version

Here’s a basic version that:

* Writes `index.html`
* Copies an image
* Sends an email via CLI tool (`sendmail` or `mailx`)

### ✔️ C Code:

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    // Create index.html
    FILE *html = fopen("/www/index.html", "w");
    if (!html) {
        perror("Failed to open index.html");
        return 1;
    }
    fprintf(html, "<html><body><h1>Welcome to Your Router Website</h1><img src='image.jpg'></body></html>");
    fclose(html);

    // Copy image (ensure local_image.jpg is present)
    if (system("cp local_image.jpg /www/image.jpg") != 0) {
        perror("Image copy failed");
        return 1;
    }

    // Send email via sendmail (requires pre-configured sendmail/postfix)
    FILE *mail = popen("/usr/sbin/sendmail -t", "w");
    if (mail) {
        fprintf(mail, "To: recipient@example.com\n");
        fprintf(mail, "From: router@example.com\n");
        fprintf(mail, "Subject: Router Website is Live\n\n");
        fprintf(mail, "Website is live at http://192.168.1.1\n");
        fprintf(mail, "You can access it via browser or terminal.\n");
        pclose(mail);
        printf("Email sent.\n");
    } else {
        perror("Failed to send email");
        return 1;
    }

    return 0;
}
```

Compile with:

```bash
gcc router_site.c -o router_site
```

---

## 📫 Email Access from Terminal (Options)

1. **With `mailx` or `mutt` installed**:

   ```bash
   echo "Website live at http://192.168.1.1" | mail -s "Router Site" recipient@example.com
   ```

2. **Using Python `smtplib`** (as above) on routers with Python.

3. **Custom raw SMTP via `netcat`** (for very minimal routers):

   ```bash
   (echo "EHLO router"; sleep 1; echo "MAIL FROM:<me@example.com>"; sleep 1; echo "RCPT TO:<you@example.com>"; sleep 1; echo "DATA"; sleep 1; echo "Subject: Router Site"; echo ""; echo "Your site is live at http://192.168.1.1"; echo "."; echo "QUIT") | nc smtp.example.com 25
   ```

---

## 🧰 Deployment Suggestions

* Add these scripts to `/etc/rc.local` to run at boot.
* Or create a custom init script (if using OpenWRT):
  `/etc/init.d/router_site`

---

## 🚀 Final Notes

* **Python** is better for emailing via Gmail or modern SMTP APIs.
* **C** is more portable but limited to router’s existing tools (no SMTP libs).
* Test sending emails via CLI **before scripting**.
* Make sure `ssmtp`, `msmtp`, or `sendmail` is installed/configured on the router.

---

Would you like:

* A version using Gmail API instead of SMTP?
* A script that pulls website content from a USB?
* Email attachment with image included?

Let me know your exact use case and router model (OpenWRT/DD-WRT/etc.) for a tailored solution.
