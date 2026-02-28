# AI Financial Analyzer

AI-powered CLI tool for analyzing financial statements, generating ratios, risk scores, visualizations, and PDF reports.

Built with:
- Python
- Google Gemini (AI insights)
- Matplotlib (graphs)
- ReportLab (PDF generation)

---

## Features

- Financial ratio analysis
- Risk scoring system
- AI-generated financial insights
- PDF report generation
- Financial graph visualization
- Batch processing support

---

## Installation

```bash
pip install ai-financial-analyzer-v1
```

---

## Usage

### Analyze a single file:

```bash
financial-analyzer --input input.json
```

### Custom output path:

```bash
financial-analyzer --input input.json --output reports/my_report.pdf
```

### Disable PDF generation:

```bash
financial-analyzer --no-pdf
```

### Disable graphs:

```bash
financial-analyzer --no-graphs
```

### Batch processing:

```bash
financial-analyzer --batch folder_path
```

---

## Environment Setup

Create a `.env` file in project root or Save the Google gemini api key as an system environment variable and name it as GEMINI_API_KEY:

```
GOOGLE_API_KEY=your_api_key_here
```

---

## Project Structure

```
app/
│
├── analysis/
├── insights/
├── normalization/
├── reporting/
├── risk/
├── utils/
├── validation/
├── visualization/
├── cli.py
```

---

## Author

Pranav Khatade  
Computer Science & Engineering Student  
AI + Finance + Systems

---

## License

MIT License
