# 🧠 AI Log Root Cause Analyzer

An AI-powered log analysis system that uses Large Language Models (LLMs)
to automatically detect failure patterns, correlate distributed errors,
and infer probable root causes from application and infrastructure logs.

Designed for scalable backend systems where manual debugging is slow,
noisy, and cognitively expensive.

------------------------------------------------------------------------

# 🚀 Problem Statement

Modern distributed architectures generate high-volume logs from:

-   Microservices
-   Containers
-   CI/CD pipelines
-   Kubernetes clusters
-   Telecom / networking systems
-   Cloud infrastructure

Root cause identification becomes difficult due to:

-   Log noise
-   Cascading failures
-   Symptom vs root cause confusion
-   Distributed service dependencies

This project automates root cause detection using:

-   Structured preprocessing
-   Intelligent chunking
-   Prompt-engineered LLM reasoning
-   Context-aware analysis

------------------------------------------------------------------------

# 🏗 System Architecture

Raw Logs → Preprocessing → Token-Aware Chunking → LLM Reasoning Engine →
Structured Root Cause Output

------------------------------------------------------------------------

## Core Components

### 1️⃣ Log Ingestion Layer

-   Accepts `.log`, `.txt`, JSON logs
-   Preserves stack traces
-   Handles multi-line exceptions
-   Supports CLI or API input

### 2️⃣ Preprocessing Engine

-   Timestamp removal (optional)
-   Noise filtering
-   Deduplication
-   Log level classification
-   Error extraction via regex
-   Stack trace grouping

### 3️⃣ Chunking Strategy

-   Token-aware segmentation
-   Maintains semantic grouping
-   Prevents LLM context overflow
-   Chronological ordering preserved

### 4️⃣ LLM Reasoning Engine

Default Model: - GPT-4 / GPT-4o via OpenAI API

Capabilities: - Identify earliest failure signal - Detect cascading
impact - Differentiate symptom vs root cause - Provide fix
recommendations - Summarize log context

### 5️⃣ Output Generator

Structured response includes: - Root Cause - Supporting Evidence -
Contributing Factors - Suggested Fix - Prevention Strategy - Confidence
Score

------------------------------------------------------------------------

# 📦 Tech Stack

-   Python 3.10+
-   OpenAI API
-   FastAPI
-   Regex parsing
-   tiktoken (token counting)
-   Docker

------------------------------------------------------------------------

# ⚙️ Configuration

Set environment variables:

export OPENAI_API_KEY=your_api_key\
export MODEL_NAME=gpt-4o\
export MAX_TOKENS=4096\
export TEMPERATURE=0.2

------------------------------------------------------------------------

# 🛠 Installation

git clone git@github.com:kavin2207/ai-log-root-cause-analyzer.git\
cd ai-log-root-cause-analyzer\
pip install -r requirements.txt

------------------------------------------------------------------------

# ▶ Usage

## CLI Mode

python main.py --log-file sample.log

## API Mode

uvicorn app:app --host 0.0.0.0 --port 8000

POST /analyze

{ "log_data": "raw log content here" }

------------------------------------------------------------------------

# 📊 Example Output

Root Cause: Database connection timeout due to misconfigured DB_HOST.

Evidence: ERROR at line 245: connection refused\
Timeout after 30s while connecting to db-service

Suggested Fix: Verify DB_HOST configuration and ensure DB service is
reachable.

Confidence: 82%

------------------------------------------------------------------------

# 🔐 Security Considerations

-   No persistent log storage
-   In-memory processing
-   API key secured via environment variables
-   Sensitive data redaction recommended before upload

------------------------------------------------------------------------

# ⚠ Limitations

-   Dependent on LLM reasoning quality
-   Large logs increase API cost
-   No persistent historical learning (yet)

------------------------------------------------------------------------

# 🚧 Roadmap

-   Vector DB integration (RAG-based analysis)
-   Historical incident learning
-   Local LLM support
-   Kubernetes operator integration
-   Slack alert integration

------------------------------------------------------------------------

# 📜 License

MIT License
