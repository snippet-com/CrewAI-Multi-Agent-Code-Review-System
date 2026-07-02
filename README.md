# 🤖 CrewAI Multi-Agent Code Review System

A modular AI-powered code review system built using **CrewAI**, **OpenAI GPT-4**, and **Python**.

This project demonstrates how multiple AI agents can collaborate to perform a comprehensive software code review. Each specialized agent is responsible for a different aspect of software quality, working together to generate a detailed review report.

---

## 🚀 Features

- Multi-Agent Architecture using CrewAI
- Automated Code Review Workflow
- Bug Detection
- Security Analysis
- Performance Review
- Code Style Review
- Refactoring Recommendations
- Executive Summary Generation
- JSON Report Export
- Modular Python Architecture
- Environment Variable Support (.env)

---

## 🏗️ Project Architecture

```
code-review-system/
│
├── main.py
├── config.py
├── code_review_system.py
├── review_agents.py
├── review_tasks.py
├── review_tools.py
├── utils.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🤖 AI Agents

### 1. Lead Code Reviewer
- Coordinates the entire review process
- Produces the executive summary
- Assigns an overall quality score
- Generates the final report

---

### 2. Bug Detection Specialist
Responsibilities:

- Detect logical errors
- Identify runtime issues
- Discover missing validation
- Review error handling

---

### 3. Code Style Expert

Reviews:

- Python best practices
- Naming conventions
- Readability
- Maintainability
- Code organization

---

### 4. Performance Analyst

Analyzes:

- Algorithm efficiency
- Time complexity
- Resource utilization
- Performance bottlenecks
- Optimization opportunities

---

### 5. Security Auditor

Checks for:

- Security vulnerabilities
- Hardcoded credentials
- Unsafe coding patterns
- Injection risks
- Sensitive data exposure

---

### 6. Refactoring Advisor

Suggests:

- Code improvements
- Better architecture
- Cleaner design
- Modularization opportunities
- Long-term maintainability

---

## ⚙️ Technologies Used

- Python
- CrewAI
- OpenAI GPT-4
- LangChain
- Python Dotenv
- JSON

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/code-review-system.git

cd code-review-system
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
OPENAI_API_KEY=your_openai_api_key
```

Run the project

```bash
python main.py
```

---

## 📋 Example Workflow

```
Input Source Code
        │
        ▼
Lead Reviewer
        │
        ▼
────────────────────────────
│      │      │      │     │
▼      ▼      ▼      ▼     ▼

Bug   Style  Security Performance Refactoring
Review Review Review Review Review

────────────────────────────
        │
        ▼
Final Executive Report
        │
        ▼
JSON Export
```

---

## 📄 Output

The system generates:

- Executive Summary
- Overall Code Quality Score
- Bug Report
- Security Audit
- Performance Analysis
- Style Review
- Refactoring Recommendations
- Final Review Report

Results are automatically exported as JSON files.

---

## 🔒 Environment Variables

The project uses environment variables to securely manage API keys.

Create a `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
```

Never commit your `.env` file to GitHub.

---

## 🎯 Future Improvements

- Support multiple programming languages
- Real linter integration (Pylint, Flake8, Ruff)
- GitHub Pull Request reviews
- PDF report generation
- Docker support
- CI/CD integration
- Multi-LLM support
- Web dashboard

---

## 📜 License

This project is available under the MIT License.

---

## 👨‍💻 Author

Developed as a portfolio project demonstrating:

- CrewAI
- Multi-Agent AI Systems
- Python Development
- Generative AI
- Software Architecture
- Prompt Engineering
