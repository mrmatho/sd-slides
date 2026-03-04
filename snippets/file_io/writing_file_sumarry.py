import logging

# Configure basic logging: set level to DEBUG to start, add format with time, levelname, and message
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def read_file(file_path: str) -> list[str]:
    with open(file_path, 'r') as f:
        logging.info(f"Opened file {file_path} for reading")
        return f.readlines() # we don't even store the lines in a variable": just return the result of readlines()

def validate_sales_data(input_data):
    sales_data = []
    for line in input_data:
        try:
            sales = float(line.strip())
            if sales < 0:
                logging.info(f"Error: Negative sales value '{line.strip()}' skipped.")
                continue
            sales_data.append(sales)
        except ValueError:
            logging.error(f"Error: Non-numeric value '{line.strip()}' skipped.")
    return sales_data

def calculate_summary(sales_data: list[float]) -> dict[str, float]:
    # Implementation to calculate total, average and max sales  
    if len(sales_data) == 0:
        logging.info("Empty Sales Data")
        return {"total": 0.0, "average": 0.0, "max": 0.0}
    total = sum(sales_data)
    average = total / len(sales_data)
    max_val = max(sales_data)
    return {"total": total, "average": average, "max": max_val}

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


input_data = read_file('input_sales.txt')
logging.debug(f"Read {len(input_data)} lines from file")
sales_data = validate_sales_data(input_data)
logging.debug(f"Validated Sales Data: {sales_data}")
summary = calculate_summary(sales_data)
logging.debug(f"Summary Data: {summary}")
success = write_summary('output_summary.txt', summary)