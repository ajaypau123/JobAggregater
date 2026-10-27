# Step-by-Step Guide: Getting Your Affiliate & Payment Links

This guide gives you the exact direct links and steps to get your own affiliate IDs and payment links for **JobsForIndia**.

---

## 1. ATS Resume Checker: Resume Worded & Jobscan

### Option A: Resume Worded (Recommended - 20% Lifetime Recurring Commission)
- **Direct Sign-up Link:** [https://resumeworded.com/affiliates](https://resumeworded.com/affiliates)
- **What they ask for:** Your name, email, website URL (`https://ajaypau123.github.io/JobAggregater/`).
- **How it works:** Once registered, you will get a unique tracking link like `https://resumeworded.com/?ref=YOUR_CODE`.
- **Payout:** Paid monthly via PayPal or direct bank transfer. You earn ~$10 to $20 (~₹800 to ₹1,600) for every user who upgrades to Pro.

### Option B: Jobscan (15% - 30% Commission)
- **Direct Sign-up Link:** [https://www.jobscan.co/affiliates](https://www.jobscan.co/affiliates)
- **What they ask for:** Fill out a short form explaining you run a curated tech job board for Indian engineers.

---

## 2. Employer Payment Link: Razorpay (Accept ₹1,999 via UPI & Card)

You do **not** need complex code or a server to accept payments. Razorpay lets you generate a direct **Payment Link** in 2 minutes.

- **Direct Sign-up Link:** [https://razorpay.com/](https://razorpay.com/)
- **Steps:**
  1. Create a free Razorpay account (choose Freelancer / Individual or Business).
  2. Complete your basic KYC (Aadhaar / PAN card and bank account details so money gets deposited into your bank).
  3. In the left menu, click **"Payment Links"** ➔ Click **"Create Payment Link"**.
  4. Set:
     - **Amount:** `₹1,999`
     - **Purpose / Description:** `JobsForIndia Featured Job (30 Days Pin)`
  5. Click **Create Link** — you will get a clean URL like:  
     `https://rzp.io/l/YOUR_UNIQUE_LINK`
  6. Paste that link into `dashboard/affiliates-config.js` under `employerPayment.paymentUrl`.

*Whenever an employer clicks "Pay ₹1,999 to Feature Job", they can pay using Google Pay, PhonePe, Paytm, UPI, or Credit/Debit Card, and the ₹1,999 lands straight in your bank account.*

---

## 3. 1-on-1 Mentorship & Mock Interviews: Topmate.io (Instant - Takes 2 Mins)

Topmate is extremely popular in the Indian tech community for booking mock interviews with senior developers from Google, Amazon, CRED, etc.

- **Direct Sign-up Link:** [https://topmate.io/](https://topmate.io/)
- **Steps:**
  1. Sign in with your Google account.
  2. On your Topmate dashboard, click on **"Refer and Earn"** in the sidebar.
  3. Copy your unique referral invite link (e.g., `https://topmate.io/join/YOUR_NAME`).
  4. Paste it into `dashboard/affiliates-config.js` under `mentorship.url`.
- **Earnings:** You earn **40% of Topmate's platform commission** on all sales made through your link!

---

## 4. Tech Interview Courses: Educative.io

Educative is famous for *"Grokking the Coding Interview"* and *"Grokking the System Design Interview"* which tech candidates love.

- **Direct Sign-up Link:** [https://www.educative.io/affiliates](https://www.educative.io/affiliates)
- **Commission:** **20% flat commission** on every subscription (~₹1,200 to ₹2,500 per sale).
- **Steps:** Apply via their partner network (handled through Impact or PostAffiliatePro).

---

## 5. Instant Job Alerts: Telegram Channel (Takes 1 Min)

- **Steps:**
  1. Open Telegram on your phone or PC.
  2. Click the pencil icon / Menu ➔ **New Channel**.
  3. Name it: **JobsForIndia | Tech & Remote Job Alerts**.
  4. Set the channel to **Public** and pick a username, e.g., `t.me/jobsforindia_alerts`.
  5. Copy your invite link and paste it into `dashboard/affiliates-config.js` under `alertsCommunity.telegramChannelUrl`.
- **Why this is powerful:** Every time you drop a hot new opening, all your channel members get an instant mobile notification!

---

## Where to Put Your Links:
Open [`dashboard/affiliates-config.js`](file:///c:/Users/Ajay%20Paul/JobAggregater/dashboard/affiliates-config.js) and replace the sample URLs with your real links.
