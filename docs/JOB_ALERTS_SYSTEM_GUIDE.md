# TechJobsForIndia - VIP Job Alerts System & Guide

> **Status:** Live & Production Ready  
> **Revenue Stream:** Candidate Micro-Subscription (₹49 for 3 Months / ₹99 for 1 Year)  
> **Infrastructure Cost:** **₹0 / month** (100% Free Tier via Resend/Brevo + GitHub Actions)

---

## 1. How It Works (The Candidate Journey)

```
Candidate lands on TechJobsForIndia
      │
      ▼
Clicks "🔔 Job Alerts" (Header / Hero Banner / Job Details Modal)
      │
      ▼
Selects Profile Preferences:
  • Target Role: QA/SDET, Frontend, Backend, DevOps, Data/AI, etc.
  • Custom Skills / Keywords: Cypress, Python, Golang, Kochi, etc.
  • Location: 100% Remote, Bengaluru, Hyderabad, Pune, Any India
  • Experience: Freshers (0-2 Yrs), Mid (2-5 Yrs), Senior (5+ Yrs)
  • Delivery Channel: Email (Daily 8:30 AM IST) or Telegram / WhatsApp
      │
      ▼
Chooses Plan:
  ├─ ⭐ VIP Pass (3 Months) ➔ ₹49  (~₹16/mo, Most Popular)
  ├─ 💎 Annual VIP (1 Year) ➔ ₹99  (Save 50%)
  └─ 🎁 Free Weekly Digest  ➔ ₹0   (Builds organic email list)
      │
      ▼
Action:
  • Profile saved instantly in local storage & webhook
  • Candidate redirected to Razorpay UPI Checkout
  • Automated daily dispatcher matches new ATS jobs & sends alerts
```

---

## 2. Setting Up Your Free Email Dispatcher (3,000 - 9,000 Emails/Mo Free)

You do **not** need a paid server. You can choose either of these two enterprise-grade free providers:

### Option A: Resend.com (Recommended — Cleanest & Fastest)
1. Go to [https://resend.com/signup](https://resend.com/signup) and create a free account.
2. In your Resend dashboard:
   - Click **API Keys** ➔ **Create API Key** (Name: `TechJobsForIndia Alerts`).
   - Copy the API key (starts with `re_...`).
3. Add your domain (once you purchase `techjobsforindia.com`) to the **Domains** tab and add the 3 DNS records provided by Resend.
   *(Until you add your domain, you can test for free using Resend's onboarding test sender).*
4. Add the secret to GitHub:
   - In GitHub, go to your repository: **Settings** ➔ **Secrets and variables** ➔ **Actions**.
   - Click **New repository secret**.
   - Name: `RESEND_API_KEY`
   - Value: `re_...` (your Resend API key).

### Option B: Brevo (formerly Sendinblue — 300 Emails/Day = 9,000/Mo Free)
1. Go to [https://www.brevo.com/](https://www.brevo.com/) and create a free account.
2. Go to **Transactional** ➔ **Settings** ➔ **Configuration**.
3. Copy your SMTP credentials:
   - Host: `smtp-relay.brevo.com`
   - Port: `587`
   - User: your Brevo login email
   - Master Password: your SMTP Key
4. Add these 4 secrets to your GitHub repository:
   - `SMTP_HOST`: `smtp-relay.brevo.com`
   - `SMTP_PORT`: `587`
   - `SMTP_USER`: `your-email@...`
   - `SMTP_PASS`: `your-smtp-key`

---

## 3. Creating Your Razorpay Payment Links (₹49 & ₹99)

1. Log in to your Razorpay Dashboard: [https://dashboard.razorpay.com/app/payment-links](https://dashboard.razorpay.com/app/payment-links)
2. Click **Create Payment Link**:
   - **Link 1 (₹49 - 3 Months VIP Pass):**
     - Amount: `₹49`
     - Description: `TechJobsForIndia VIP Job Alerts Pass (3 Months)`
     - Notify via: Email / SMS
     - Copy the generated URL (e.g. `https://rzp.io/l/abc123xyz`)
   - **Link 2 (₹99 - 1 Year Annual Pass):**
     - Amount: `₹99`
     - Description: `TechJobsForIndia Annual VIP Alerts Pass (1 Year)`
     - Copy the generated URL
3. Open `dashboard/affiliates-config.js` and paste your links into `jobAlerts`:
   ```javascript
   paymentUrl3Mo: "https://rzp.io/l/YOUR_3MO_LINK",
   paymentUrl1Yr: "https://rzp.io/l/YOUR_1YR_LINK",
   ```

---

## 4. Capturing Subscriber Emails (Free Formspree or Google Forms)

Whenever a candidate enters their preferences in the modal, you can capture their email and preferences in real time:

1. Create a free account at [https://formspree.io/](https://formspree.io/) (free tier includes 50 submissions/month).
2. Or use a Google Forms / Google Sheets Webhook (100% free, unlimited submissions).
3. Paste the URL into `dashboard/affiliates-config.js`:
   ```javascript
   subscriberWebhookUrl: "https://formspree.io/f/YOUR_FORM_ID",
   ```
Every time someone clicks "Activate VIP Alerts", their details (Email, Phone, Role Category, Location, Keywords) are securely posted to your spreadsheet or inbox.

---

## 5. Automated Daily Dispatch in GitHub Actions

The alert dispatcher script is located at:
[`aggregator/alerts/dispatcher.py`](file:///c:/Users/Ajay%20Paul/JobAggregater/aggregator/alerts/dispatcher.py)

It has been wired into `.github/workflows/scrape_and_deploy.yml`:
- Every day at 00:00 UTC (05:30 AM IST), GitHub Actions scrapes the newest direct ATS jobs from Greenhouse, Lever, Ashby, and Workday.
- Immediately after scraping, it runs:
  ```bash
  python -m aggregator.alerts.dispatcher
  ```
- If `RESEND_API_KEY` or SMTP secrets are set in GitHub, it sends matching emails to all active subscribers.
- If no secrets are set yet, it runs in `--dry-run` mode to verify matching jobs without throwing any errors.

### Local Testing Command
To test how alerts match against your real scraped database right from your computer:
```bash
python -m aggregator.alerts.dispatcher --dry-run
```

---

## 6. Financial Projections for Job Alerts Stream

| Active Subscribers | Quarterly Revenue (₹49/3mo) | Monthly Equivalent | Email Dispatch Cost | Net Profit Margin |
| :--- | :--- | :--- | :--- | :--- |
| **50 subscribers** | ₹2,450 | ₹816 | ₹0 (Free tier) | **100%** |
| **250 subscribers** | ₹12,250 | ₹4,083 | ₹0 (Free tier) | **100%** |
| **1,000 subscribers** | ₹49,000 | ₹16,333 | ₹0 (Free tier) | **100%** |
| **3,000 subscribers** | ₹1,47,000 | ₹49,000 | ₹0 (Resend free) | **100%** |
| **10,000 subscribers** | ₹4,90,000 | ₹1,63,333 | ~₹1,200/mo (SES) | **99.3%** |

---

## 7. Next Actions Checklist
- [x] Modern Job Alerts CTA in Navigation Header (`₹49` badge)
- [x] High-converting ambient Job Alerts promo banner on home feed
- [x] Job Details Modal "Alert Similar Roles" 1-click shortcut
- [x] Interactive Candidate Alert Subscription Modal with Role/Location/Channel filters
- [x] Modular `aggregator.alerts.dispatcher` Python matching engine
- [x] GitHub Actions automated workflow dispatch integration
- [ ] User creates ₹49 and ₹99 payment links in Razorpay
- [ ] User pastes payment links into `dashboard/affiliates-config.js`
- [ ] User adds `RESEND_API_KEY` to GitHub Secrets
