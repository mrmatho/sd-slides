import logging

# Configure basic logging: set level to INFO, add format with time, levelname, and message
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def read_file(file_path: str) -> list[str]:
    with open(file_path, 'r') as f:
        return f.readlines()

def validate_sales_data(input_data: list[str]) -> list[float]:
    sales_data = []
    for line in input_data:
        try:
            sales = float(line.strip())
            if sales < 0:
                logging.error(f"Error: Negative sales value '{line.strip()}' skipped.")
                continue
            sales_data.append(sales)
        except ValueError:
            logging.error(f"Error: Non-numeric value '{line.strip()}' skipped.")
    return sales_data


def calculate_summary(sales_data: list[float]) -> dict[str, float]:
    # Existence check to avoid dividing by zero or calling max() on an empty list
    if not sales_data:
        return {"total": 0.0, "average": 0.0, "max": 0.0}
    # C
    total_sales = sum(sales_data)
    average_sales = total_sales / len(sales_data)
    max_sales = max(sales_data)
    
    return {"total": total_sales, "average": average_sales, "max": max_sales}

def write_summary(file_path: str, summary: dict[str, float]) -> bool:
    try:
        with open(file_path, 'w') as f:
        
            f.write(f"Total Sales: {summary['total']:.2f}\n")
            f.write(f"Average Sales: {summary['average']:.2f}\n")
            f.write(f"Max Sales: {summary['max']:.2f}\n")
    except Exception as e:
        logging.error(f"Error writing to file: {e}")
        return False
    return True

# Read data from file (As strings)
input_data = read_file('input_sales.txt')
logging.info(f"Read {len(input_data)} lines from input_sales.txt")
# Validate input data and convert to list of floats
sales_data = validate_sales_data(input_data)
logging.info(f"Validated sales data contains {len(sales_data)} entries")
# Calculate summary statistics
summary = calculate_summary(sales_data)
logging.info(f"Calculated summary: Total={summary['total']:.2f}, Average={summary['average']:.2f}, Max={summary['max']:.2f}")

# Write summary to output file
success = write_summary('output_summary.txt', summary)

if success:
    logging.info("Summary successfully written to output_summary.txt")
else:
    logging.error("Failed to write summary to output_summary.txt")