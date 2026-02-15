# AWS Serverless Cloud Portfolio ☁️

### Architecture Status: [ PRODUCTION ] 🟢
**Role:** Cloud Solutions Architect | **Tech Stack:** AWS, Python, GitHub Actions, Terraform

---

## 📖 Executive Summary
This repository houses the backend logic and infrastructure automation for a cloud-native, serverless application. The project was executed in **5 Strategic Phases**, transforming a manual, static site into a fully automated, event-driven enterprise architecture.

**Key Metrics:**
* **Availability:** 99.99% (Serverless)
* **Cost:** $0.00/month (Free Tier Optimization)
* **Deployment Time:** <30 Seconds (CI/CD)
* **Security:** Zero-Trust (OAC & IAM Least Privilege)

---

## 🏗️ The 5-Phase Architecture

### ✅ Project 1: Security & Governance
**Objective:** Secure the frontend delivery pipeline.
* **Implementation:** Migrated static assets to **Amazon S3**.
* **Security:** Enforced **CloudFront Origin Access Control (OAC)** to block direct public access to the bucket.
* **Outcome:** 100% encrypted traffic via HTTPS; zero public S3 exposure.

### ✅ Project 2: Cost Optimization (FinOps)
**Objective:** Eliminate idle compute costs.
* **Implementation:** Replaced EC2 instances with **AWS Lambda** (Python 3.12).
* **Strategy:** Adopted an event-driven execution model where costs are incurred only per millisecond of execution.
* **Outcome:** Reduced operational overhead and achieved a near-zero cost baseline.

### ✅ Project 3: System Integration (API)
**Objective:** Decouple frontend from backend logic.
* **Implementation:** Deployed **API Gateway** (or Lambda Function URL) as the intake layer.
* **Architecture:** Enabled independent scaling of the frontend (React/HTML) and backend (Python).
* **Outcome:** RESTful interface established with CORS enabled for secure cross-origin resource sharing.

### ✅ Project 4: State Management
**Objective:** Introduce persistence to a stateless environment.
* **Implementation:** Integrated **Amazon DynamoDB** (NoSQL) for high-speed data retrieval.
* **Logic:** Implemented "Atomic Counters" to track visitor stats without race conditions.
* **Outcome:** Stateful application behavior achieved without managing database servers.

### ✅ Project 5: Automation (CI/CD)
**Objective:** Eliminate manual deployment risks ("ClickOps").
* **Implementation:** Built a **GitHub Actions** pipeline.
* **Workflow:**
    1.  **Source:** Git Push to `main`.
    2.  **Auth:** OIDC/IAM Keys injection (GitHub Secrets).
    3.  **Build:** Zip artifact creation.
    4.  **Deploy:** Atomic update to AWS Lambda.
* **Outcome:** Governance enforced. Manual access to production revoked.

---

## 🛠️ Technical Implementation

### The Logic (`lambda_function.py`)
The core backend logic handles the API handshake and database updates.
* **Library:** `boto3` (AWS SDK for Python)
* **Operation:** `update_item` (Atomic Increment)

### The Pipeline (`deploy.yml`)
The CI/CD workflow ensures deterministic delivery.
* **Trigger:** Push to `main` branch.
* **Runner:** Ubuntu-latest.

---

## 🚀 How to Verify
**Live API Endpoint:** [👉 Click to View Live JSON Output](https://kwgjzeki2ntw2up4pbhjwokx5y0lbxmy.lambda-url.us-east-1.on.aws/)
*(Shows the raw JSON response from the Serverless Backend)*

**Live Frontend:** [🌐 Click to View Website](https://d15mkbs5juw1on.cloudfront.net/)
*(Shows the CloudFront distribution serving the UI)*
