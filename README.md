# CertificateMailer

An automated e-certificate generation and email distribution system built with Python.

CertificateMailer generates personalised PDF certificates from participant data and automatically distributes them via email. It is designed to simplify certificate distribution for events, workshops, hackathons, competitions, and college festivals.

## Features

- **Automated PDF Generation:** Generate individual certificates using participant information.
- **Personalised Certificates:** Dynamically insert participant names and unique certificate IDs.
- **Bulk Email Distribution:** Send individual emails with the corresponding PDF certificate attached.
- **Email Tracking:** Maintain records of successfully sent and failed emails.
- **Resume Support:** Skip successfully processed participants when restarting the application.
- **CSV Integration:** Import participant details from CSV files.
- **Batch Processing:** Distribute certificates in controlled batches.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application |
| Pandas | CSV data processing |
| ReportLab | PDF certificate generation |
| Brevo API | Email delivery |
| Requests | HTTP API communication |
| Python-dotenv | Environment variable management |

## Project Structure

```text
CertificateMailer/
│
├── certificates/          # Certificate assets and templates
│
├── templates/             # Certificate design templates
│
├── output/                # Generated PDF certificates
│
├── data/
│   └── participants.csv   # Participant information
│
├── .env                   # API credentials and configuration
├── .gitignore
├── requirements.txt
├── main.py                # Application entry point
└── README.md
```

## Requirements

- Python 3.10+
- Brevo account
- Verified sender email address
- Participant CSV file

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd CertificateMailer
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
BREVO_API_KEY=your_brevo_api_key
SENDER_EMAIL=your_verified_email@example.com
SENDER_NAME=Certificate Team
```

Never commit API keys or credentials to version control.

## Participant Data

Prepare a CSV file at `data/participants.csv`.

Example:

```csv
name,email,certificate_id
John Doe,john@example.com,CERT001
Jane Doe,jane@example.com,CERT002
Alex Smith,alex@example.com,CERT003
```

### Required Fields

| Field | Description |
|---|---|
| name | Participant's full name |
| email | Participant's email address |
| certificate_id | Unique certificate identifier |

## Usage

Run the application:

```bash
python main.py
```

The application will:

1. Read participant information from CSV.
2. Generate individual PDF certificates.
3. Save generated certificates in the output directory.
4. Distribute certificates through email.
5. Record email delivery results.

*Email distribution functionality is planned for implementation.*

## Development Roadmap

- [x] Project structure and initial setup
- [x] CSV-based participant data format
- [x] Basic PDF certificate generation
- [ ] Custom certificate templates
- [ ] Brevo API integration
- [ ] Personalised email templates
- [ ] PDF email attachments
- [ ] Email delivery logging
- [ ] Failed email retry mechanism
- [ ] Duplicate sending prevention
- [ ] Batch processing and rate limiting
- [ ] Final testing with 1,500+ participants

## Email Distribution

Brevo will be used as the email delivery provider.

The system will send individual emails rather than exposing participants' email addresses through CC or BCC.

Email delivery limits depend on the selected Brevo plan.

## Security

- API credentials are stored in environment variables.
- `.env` is excluded from Git.
- Participant information is handled locally.
- Successful deliveries are tracked to prevent accidental duplicate sending.

## License

This project is currently under development.