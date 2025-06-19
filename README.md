# 📬 AWS SES Email Sender using AWS SAM

This is a simple serverless project using **AWS Lambda**, **Amazon SES**, and **AWS SAM CLI** to send transactional emails.

---

## 🛠 Tech Stack

- Python 3.12
- AWS Lambda
- Amazon SES
- AWS SAM CLI
- CloudFormation

---

## 🚀 Features

- Send transactional emails with AWS SES
- Written in Python
- Easily deployable via SAM
- Configurable via environment variables

---

## 📦 Setup Instructions

### 1. Clone this repo

```bash
git clone https://github.com/minalisahu/ses-sam-aws.git
cd ses-sam-aws

```
### 2. Install dependencies

Make sure you have:

- ✅ AWS CLI configured (`aws configure`)
- ✅ AWS SAM CLI installed (`sam --version`)


### 3. Set sender/recipient emails in `template.yaml`

Update the environment variables section:

```yaml
Environment:
  Variables:
    SENDER_EMAIL: "your_verified_sender@example.com"
    RECIPIENT_EMAIL: "your_verified_recipient@example.com"
```
✅ Make sure both emails are verified in Amazon SES if you’re in sandbox mode.
### 4. Build and Deploy the app

```bash
sam build
sam deploy --guided
```

🧪 Important

Amazon SES starts in sandbox mode.
You must verify both sender and recipient email addresses in the AWS SES Console.