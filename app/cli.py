import argparse
import os

from app.normalization.normalizer import normalize_json
from app.validation.validator import validate_financials
from app.analysis.ratios import compute_ratios
from app.visualization.plotter import save_financial_graphs
from app.insights.gemini_insights import generate_insights
from app.reporting.pdf_report import generate_pdf_report
from app.risk.scoring import calculate_risk_score
from app.utils.json_loader import load_json_file
from app.utils.logger import setup_logger


def process_file(file_path, output_path, args, logger):

    logger.info(f"Processing file: {file_path}")

    raw_data = load_json_file(file_path)

    logger.info("Normalizing financial data...")
    normalized = normalize_json(raw_data)

    logger.info("Running validation checks...")
    validation_errors = validate_financials(normalized)

    logger.info("Computing financial ratios...")
    ratios = compute_ratios(normalized)

    logger.info("Generating AI insights...")
    insights = generate_insights(ratios, validation_errors)

    logger.info("Calculating risk score...")
    risk_score, risk_level = calculate_risk_score(ratios, validation_errors)

    graph_paths = None
    if not args.no_graphs:
        logger.info("Generating financial graphs...")
        graph_paths = save_financial_graphs(normalized)
    else:
        logger.info("Graph generation skipped.")

    if not args.no_pdf:
        logger.info(f"Generating PDF report at {output_path}")
        generate_pdf_report(
            output_path,
            normalized,
            ratios,
            validation_errors,
            insights,
            graph_paths,
            risk_score,
            risk_level
        )
    else:
        logger.info("PDF generation skipped.")

    logger.info(f"Finished processing: {file_path}")


def main():

    parser = argparse.ArgumentParser(
        description="AI Financial Statement Analyzer"
    )

    parser.add_argument("--input", type=str, default="input.json",
                        help="Path to input JSON file")

    parser.add_argument("--output", type=str,
                        default="reports/financial_report.pdf",
                        help="Path to output PDF report")

    parser.add_argument("--no-pdf", action="store_true",
                        help="Disable PDF generation")

    parser.add_argument("--no-graphs", action="store_true",
                        help="Disable graph generation")

    parser.add_argument("--batch", type=str,
                        help="Path to folder containing multiple JSON files")

    args = parser.parse_args()

    logger = setup_logger()

    try:

        if args.batch:

            if not os.path.isdir(args.batch):
                raise ValueError("Batch path must be a valid folder.")

            logger.info(f"Starting batch processing in folder: {args.batch}")
            os.makedirs("reports", exist_ok=True)

            for filename in os.listdir(args.batch):
                if filename.endswith(".json"):
                    file_path = os.path.join(args.batch, filename)
                    output_name = filename.replace(".json", "_report.pdf")
                    output_path = os.path.join("reports", output_name)

                    try:
                        process_file(file_path, output_path, args, logger)
                    except Exception as e:
                        logger.error(f"Failed processing {filename}: {str(e)}")

            logger.info("Batch processing completed.")

        else:
            os.makedirs("reports", exist_ok=True)
            process_file(args.input, args.output, args, logger)

        logger.info("Program finished successfully.")

    except Exception as e:
        logger.error(f"Critical failure: {str(e)}")


if __name__ == "__main__":
    main()