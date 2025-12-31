import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)

def process_data():
    try:
        logging.info("Event triggered: Data received")

        # Sample incoming data
        data = [5, 15, 25, 35, 45]

        # Processing logic
        total = sum(data)
        count = len(data)
        average = total / count

        # Generate summary report
        report = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "records_count": count,
            "total_value": total,
            "average_value": average
        }

        logging.info(f"Daily Summary Report: {report}")
        logging.info("Data processing completed successfully")

    except Exception as e:
        logging.error(f"Error during data processing: {e}")

if __name__ == "__main__":
    process_data()
