from pathlib import Path

readme = r'''<div align="center">

# AI Financial Analyzer

### Turn structured financial data into ratios, risk signals, visualizations, and reports.

A Python command-line tool for automating key parts of financial statement analysis with deterministic calculations and AI-assisted insights.

<p>
  <a href="https://github.com/Pranav-Khatade/Financial-Analyzer"><img src="https://img.shields.io/badge/Project-Financial%20Analyzer-2563eb?style=for-the-badge" alt="Financial Analyzer"></a>
  <a href="https://pypi.org/project/ai-financial-analyzer-v1/"><img src="https://img.shields.io/pypi/v/ai-financial-analyzer-v1?style=for-the-badge&logo=pypi&logoColor=white" alt="PyPI version"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.9+"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-16a34a?style=for-the-badge" alt="MIT License"></a>
</p>

<p>
  <a href="#-features">Features</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-configuration">Configuration</a> •
  <a href="#-contributing">Contributing</a>
</p>

</div>

---

## Overview

**AI Financial Analyzer** is a command-line application that helps streamline financial statement analysis. It processes structured financial input, validates and normalizes data, computes financial ratios, generates risk-oriented summaries, creates charts, and can export a PDF report.

The project combines conventional Python data processing with Google Gemini-powered insight generation. The aim is to make financial data easier to inspect and communicate without treating AI output as a substitute for verified calculations or professional financial judgment.

### At a glance

| Item | Details |
|---|---|
| Project type | Python command-line application |
| Package | `ai-financial-analyzer-v1` |
| Current package version documented in the project | `1.0.1` |
| Python requirement | Python 3.9 or newer |
| AI integration | Google Gemini via `google-genai` |
| Visualization | Matplotlib |
| PDF reports | ReportLab |
| Input example | JSON (`input.json`) |
| Main command | `financial-analyzer` |
| Distribution | PyPI |
| License | MIT |

## Why this project?

Financial information is often spread across raw figures that need to be checked, organized, compared, and explained. This project brings several steps into one repeatable workflow:

1. Accept structured financial data.
2. Validate and normalize the input.
3. Calculate supported financial ratios.
4. Generate risk-oriented results and AI-assisted explanations.
5. Produce visualizations and, optionally, a PDF report.
6. Support processing more than one input through batch mode.

The exact conclusions depend on the quality and completeness of the supplied data. The tool is intended as an analysis aid, not as an audit or a source of guaranteed investment advice.

## ✨ Features

| Capability | What it does | Benefit |
|---|---|---|
| Financial ratio analysis | Calculates supported financial ratios from the supplied data | Makes important relationships easier to inspect |
| Input validation | Checks input data before analysis | Helps identify malformed or incomplete input |
| Data normalization | Structures financial data for downstream processing | Creates a more consistent analysis workflow |
| Risk scoring | Produces a risk-oriented score using the project's implemented logic | Offers a compact signal for further review |
| AI-assisted insights | Uses Google Gemini to generate explanatory insights | Helps make numerical results easier to interpret |
| Visualizations | Generates financial graphs with Matplotlib | Makes trends and comparisons easier to understand |
| PDF reporting | Exports a report with ReportLab | Creates a shareable analysis artifact |
| Batch processing | Supports analyzing a folder of inputs | Helps repeat the workflow across multiple files |
| CLI options | Allows output location and optional report/graph generation to be controlled | Fits different workflows |

> **Interpretation note:** AI-generated explanations and risk scores can be incomplete or incorrect. Review the underlying data, formulas, and assumptions before acting on any result.

## 🧰 Technology stack

| Technology | Role |
|---|---|
| Python | Core language and application logic |
| Google GenAI SDK (`google-genai`) | Gemini API integration for AI-assisted insights |
| Matplotlib | Chart and graph generation |
| ReportLab | PDF report generation |
| `setuptools` / `wheel` | Python package build and distribution |

## 🚀 Quick Start

### Option A — Install from PyPI

The package is published as `ai-financial-analyzer-v1`.

```bash
python -m pip install --upgrade pip
python -m pip install ai-financial-analyzer-v1==1.0.1
```

Verify that the command is available:

```bash
financial-analyzer --help
```

If Windows cannot find `financial-analyzer`, check that Python's **Scripts** directory is on your `PATH`, then open a new terminal.

### Option B — Run from source

```bash
git clone https://github.com/Pranav-Khatade/Financial-Analyzer.git
cd Financial-Analyzer

python -m venv .venv
```

Activate the environment:

**Windows PowerShell**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows Command Prompt**
```bat
.venv\Scripts\activate.bat
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

Install the project:

```bash
python -m pip install --upgrade pip
python -m pip install -e .
```

Set up the API key as described in [Configuration](#-configuration), then run:

```bash
financial-analyzer --input input.json
```

## 🔑 Configuration

The application uses a Google Gemini API key for AI-assisted insights.

1. Create an API key through [Google AI Studio](https://aistudio.google.com/).
2. Copy the example environment file:

   **Windows PowerShell**
   ```powershell
   Copy-Item .env.example .env
   ```

   **macOS / Linux**
   ```bash
   cp .env.example .env
   ```
3. Edit `.env` and set the key:

   ```dotenv
   GOOGLE_API_KEY=your_api_key_here
   ```

4. Ensure the key is loaded into the process environment when running the CLI. If your current setup does not load `.env` automatically, set the environment variable in your shell before launching the application.

**Windows PowerShell**
```powershell
$env:GOOGLE_API_KEY = "your_api_key_here"
financial-analyzer --input input.json
```

**macOS / Linux**
```bash
export GOOGLE_API_KEY="your_api_key_here"
financial-analyzer --input input.json
```

### Security checklist

- Never commit `.env` or a real API key.
- Do not paste API keys into issues, screenshots, or public logs.
- Use `.env.example` only as a template containing a placeholder.
- If a key is exposed, revoke it and create a replacement.

## 🖥️ Usage

The commands below reflect the CLI options documented by the project. Run `financial-analyzer --help` in your installed environment to confirm the options supported by your installed version.

### Analyze one input file

```bash
financial-analyzer --input input.json
```

### Choose a PDF report location

```bash
financial-analyzer --input input.json --output reports/my_report.pdf
```

Make sure the destination directory exists if your environment or version does not create it automatically.

### Disable PDF generation

```bash
financial-analyzer --input input.json --no-pdf
```

### Disable graph generation

```bash
financial-analyzer --input input.json --no-graphs
```

### Process a folder in batch mode

```bash
financial-analyzer --batch folder_path
```

### CLI reference

| Option | Purpose |
|---|---|
| `--input <file>` | Select an input file for a single analysis |
| `--output <path>` | Specify the report output path |
| `--no-pdf` | Disable PDF generation |
| `--no-graphs` | Disable graph generation |
| `--batch <folder>` | Process inputs from a folder |

## 📄 Input data

The repository includes an `input.json` example. Use it as the starting point for preparing your own data, and preserve the structure expected by the version of the application you are running.

Example workflow:

```text
Your JSON input
      │
      ▼
Validation and normalization
      │
      ▼
Financial calculations and risk logic
      │
      ├──────────────► Visualizations
      │
      ├──────────────► AI-assisted insights
      │
      ▼
PDF report (unless disabled)
```

Before running an analysis, check that:
- Numeric fields contain valid numbers rather than formatted strings where numbers are expected.
- Required fields are present.
- Values use consistent units and reporting periods.
- The input is based on reliable source information.

For the precise schema, refer to [`input.json`](./input.json) and the validation/normalization modules in [`app/`](./app/).

## 🏗️ Architecture

The codebase is organized into focused modules. At a high level, the responsibilities are:

| Module | Responsibility |
|---|---|
| `app/analysis/` | Financial analysis logic |
| `app/insights/` | AI-assisted insight generation |
| `app/normalization/` | Data normalization |
| `app/reporting/` | PDF/report output |
| `app/risk/` | Risk scoring logic |
| `app/utils/` | Shared utilities |
| `app/validation/` | Input validation |
| `app/visualization/` | Graph and chart generation |
| `app/cli.py` | Command-line entry point |

### Design principles

- **Repeatability:** keep data preparation and numerical calculations in application code.
- **Separation of concerns:** organize validation, analysis, insights, visualization, and reporting into distinct areas.
- **Usability:** expose common workflows through a command-line interface.
- **Transparency:** make results reviewable rather than presenting AI-generated text as unquestionable truth.

### Repository layout

```text
Financial-Analyzer/
├── .github/
│   └── workflows/
├── app/
│   ├── analysis/
│   ├── insights/
│   ├── normalization/
│   ├── reporting/
│   ├── risk/
│   ├── utils/
│   ├── validation/
│   ├── visualization/
│   └── cli.py
├── .env.example
├── input.json
├── pyproject.toml
└── README.md
```

Some files or subdirectories may change as the project evolves; the repository is the source of truth for the current layout.

## 📊 Output

Depending on the options and input provided, the workflow can produce:

| Output | Description |
|---|---|
| Analysis results | Computed financial metrics and ratios |
| Risk-oriented result | A score generated by the implemented risk logic |
| Visualizations | Graphs generated with Matplotlib, unless disabled |
| PDF report | A report generated with ReportLab, unless disabled |
| AI-assisted explanation | Natural-language insights generated through the configured Gemini API |

The exact fields and presentation depend on the current implementation and the supplied input. Do not interpret a risk score as a validated credit rating or investment recommendation.

## 🧪 Development and verification

To set up a local development environment:

```bash
git clone https://github.com/Pranav-Khatade/Financial-Analyzer.git
cd Financial-Analyzer

python -m venv .venv
```

Activate the environment using the instructions above, then install the project in editable mode:

```bash
python -m pip install --upgrade pip
python -m pip install -e .
```

Check the command interface:

```bash
financial-analyzer --help
```

For a basic smoke test, run the sample input:

```bash
financial-analyzer --input input.json
```

Review the generated files and console output. Confirm that the input is accepted, calculations are plausible, and the report and graphs are produced as expected.

> Automated test commands and coverage figures are intentionally not listed here because they should be added only after the corresponding test suite and results have been verified.

## 🗺️ Roadmap ideas

Potential areas for future improvement include:

- [ ] Add automated unit tests for financial formulas and input validation.
- [ ] Document each ratio, formula, and its interpretation.
- [ ] Add sample reports and screenshots generated from non-sensitive example data.
- [ ] Improve error messages for missing fields and API failures.
- [ ] Add structured logging and clearer exit codes for CLI automation.
- [ ] Add support for additional input formats and reporting periods.
- [ ] Add reproducible benchmarks for batch processing.
- [ ] Provide a configuration option for AI model selection.

These are possible next steps, not claims that the features are already implemented.

## ⚠️ Limitations and responsible use

- Output quality depends on the accuracy, completeness, and consistency of the input data.
- AI-generated insights may contain errors, omissions, or unsupported interpretations.
- Risk scoring reflects the project's implemented logic and should not be treated as a certified financial risk model.
- This project is for educational and analytical assistance. It is not financial, investment, tax, accounting, or legal advice.
- Verify results independently before using them in business, lending, investment, or compliance decisions.

## 🤝 Contributing

Contributions, bug reports, and thoughtful suggestions are welcome.

1. Fork the repository.
2. Create a focused branch.
   ```bash
   git checkout -b feature/your-change
   ```
3. Make a small, clearly scoped change.
4. Test the relevant behavior locally.
5. Open a pull request describing the problem, solution, and verification steps.

For bug reports, include a minimal reproducible example and remove confidential financial data and API keys before sharing logs or input files.

## 🐛 Issues and feedback

- **Source code:** [Pranav-Khatade/Financial-Analyzer](https://github.com/Pranav-Khatade/Financial-Analyzer)
- **Report a bug / request a feature:** [GitHub Issues](https://github.com/Pranav-Khatade/Financial-Analyzer/issues)
- **Package:** [ai-financial-analyzer-v1 on PyPI](https://pypi.org/project/ai-financial-analyzer-v1/)

## 📜 License

This project is distributed under the MIT License. See [`LICENSE`](./LICENSE) for the full license text.

## 👤 Author

**Pranav Khatade**

- GitHub: [@Pranav-Khatade](https://github.com/Pranav-Khatade)
- Project: [AI Financial Analyzer](https://github.com/Pranav-Khatade/Financial-Analyzer)

---

<div align="center">

**Built to make financial analysis workflows more structured, repeatable, and easier to inspect.**

If this project is useful to you, consider giving the repository a ⭐.

</div>
'''

path = Path("/mnt/data/README_Financial_Analyzer.md")
path.write_text(readme, encoding="utf-8")
print(f"Created {path} ({len(readme.splitlines())} lines, {path.stat().st_size:,} bytes)")
