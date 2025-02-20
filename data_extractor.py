import re
import argparse  # For command-line arguments

def extract_data(text):
    # ... (Existing regex extraction code from the previous response remains the same)

def process_large_dataset(filepath):
    all_data = []
    try:  # Handle file reading errors gracefully
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                extracted = extract_data(line)
                all_data.append(extracted)
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None  # Indicate failure
    except Exception as e: # Catch other potential errors during file reading
        print(f"An error occurred: {e}")
        return None
    return all_data

def main():
    parser = argparse.ArgumentParser(description="Extract data using regular expressions.")
    parser.add_argument("filepath", help="Path to the input file")
    args = parser.parse_args()

    filepath = args.filepath
    extracted_data_from_file = process_large_dataset(filepath)

    if extracted_data_from_file is not None:  # Check if file processing was successful
        # You can either print the results or save them to a file
        # For demonstration, let's print the counts of each data type
        for data_set in extracted_data_from_file:
            for key, value in data_set.items():
                print(f"{key.upper()}: {len(value)}")  # Show the count
            print("-" * 20)  # Separator between data sets
    else:
        print("Data extraction failed.")


if __name__ == "__main__":
    main()
