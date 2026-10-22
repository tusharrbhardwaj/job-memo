# Job-Memo — Same job, less time.

**Job-Memo** is an AI-powered job application assistant designed to eliminate repetitive work, accelerate job applications, and help users apply to more relevant positions without sacrificing personalization or control.

## 1. The Problem
Job seekers repeatedly enter the same personal information, education, work experience, skills, and documents across LinkedIn, company career portals, and other recruitment platforms. They also spend time answering similar application questions, uploading resumes, and writing tailored responses. This process is tedious, time-consuming, and especially difficult for students and job seekers balancing work, studies, and personal projects.

## 2. The Solution
Job-Memo combines AI, browser automation, and a reusable professional profile to automate the repetitive parts of applying for jobs. Users provide a job or application URL, and the system analyzes the opportunity, identifies application fields and questions, retrieves relevant profile information, generates personalized answers, and fills the form automatically. Users review and edit the completed application before submitting it themselves.

## 3. Core Workflow
1. **Enter a job URL:** The user provides a link to a job listing or application page.
2. **Open the website:** Playwright launches a browser and reuses an authenticated browser session when available.
3. **Analyze the opportunity:** The system extracts the job description, requirements, application fields, questions, dropdowns, checkboxes, and document-upload fields.
4. **Retrieve profile information:** Job-Memo accesses the user's saved professional profile, including personal details, education, experience, skills, projects, preferences, and relevant documents.
5. **Generate personalized answers:** The AI uses the job description, application questions, and relevant profile information to produce tailored, structured responses.
6. **Autofill the application:** Browser automation fills supported fields, selects appropriate options, and uploads designated documents.
7. **Review and edit:** The user checks every field and AI-generated response, corrects errors, and approves the application.
8. **Submit manually:** The user makes the final submission decision.
9. **Track the application:** Job-Memo records application details and status for future reference.

## 4. Main Features
- Reusable professional profile and personal-information storage.
- Resume, cover-letter, certificate, and other document management.
- Job-description analysis and requirement matching.
- Automatic detection of application fields and questions.
- AI-generated, personalized answers grounded in the user's actual background.
- Automated form filling, dropdown selection, checkbox handling, and file uploads where supported.
- Persistent browser sessions to avoid repeatedly logging in.
- Human review and editing before submission.
- Application history, statuses, and future response/interview tracking.
- Extensible architecture for supporting different recruitment websites.

## 5. Technology Stack
- **Python:** Core application logic and automation.
- **Playwright:** Browser control, page analysis, navigation, and form filling.
- **FastAPI:** Local backend API connecting application components.
- **OpenAI API:** Job analysis and personalized answer generation.
- **SQLite:** Local storage for profile information, questions, answers, and application history.
- **Pydantic:** Validation of structured data and AI outputs.
- **HTML, CSS, and JavaScript:** Optional dashboard or user interface as the project develops.
- **Chrome Extension:** A possible future interface for launching Job-Memo directly from job websites.

## 6. System Architecture
Job-Memo is divided into independent modules: a user interface, browser automation engine, application-page parser, profile and document manager, AI engine, autofill engine, review workflow, and application-history database. The parser converts webpage information into structured fields; the AI generates structured answers; and the autofill engine maps those answers back to the appropriate browser elements. This separation makes the system easier to debug, maintain, and extend to new websites.

## 7. Security and Reliability
Sensitive profile information and documents should remain local wherever possible. API keys must be stored securely, and unnecessary personal data must not be sent to the AI provider. Job-Memo should reuse browser-managed sessions rather than store website passwords in plaintext. AI-generated information must be checked against the user's actual profile; unknown answers must be flagged rather than invented. Browser automation must handle missing fields, validation errors, dynamic pages, and unsupported application flows gracefully. The user retains control over document sharing, sensitive declarations, and final submission.

## 8. Development Roadmap
**MVP:** Accept a URL, open a browser, extract page content and supported form fields, generate answers using a profile, autofill the form, and stop for human review.

**Next versions:** Add persistent sessions, structured profile editing, document uploads, multi-step forms, application history, improved website compatibility, and a dashboard.

**Long-term vision:** Develop Job-Memo into a reliable, extensible job-application platform, potentially combining a Chrome extension with a Python backend and support for multiple recruitment platforms.

## 9. Project Objective
The objective is not to submit applications indiscriminately or replace the applicant's judgment. It is to reduce repetitive administrative work, improve application consistency, personalize responses, and give job seekers more time to focus on studying, developing skills, preparing for interviews, and building their careers.

**Job-Memo — Same job, less time.**