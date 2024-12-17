def read_file(file_path):
    """Reads data from a file and returns its content."""
    with open(file_path, 'r') as file:
        return file.readlines()

def extract_mobile_numbers(data):
    """Extracts valid 10-digit mobile numbers from data."""
    mobile_numbers = []
    for line in data:
        words = line.split()
        for word in words:
            if len(word) == 10 and word.isdigit():
                mobile_numbers.append(word)
    return mobile_numbers

def extract_email_ids(data):
    """Extracts valid email IDs from data."""
    email_ids = []
    for line in data:
        words = line.split()
        for word in words:
            if '@' in word and '.' in word:
                parts = word.split('@')
                if len(parts) == 2 and '.' in parts[1]:
                    email_ids.append(word)
    return email_ids

def write_to_file(file_path, data):
    """Writes data to a file, one item per line."""
    with open(file_path, 'w') as file:
        for item in data:
            file.write(item + '\n')

def main():
    input_file = 'tttt.txt'  # Input file name
    mobile_file = 'mobile_no.txt'  # Output file for mobile numbers
    email_file = 'email_ids.txt'  # Output file for email IDs
    raw_file = 'raw_data.txt'  # Output file for raw data

    # Step 1: Read data from the input file
    data = read_file(input_file)

    # Step 2: Extract mobile numbers and email IDs
    mobile_numbers = extract_mobile_numbers(data)
    email_ids = extract_email_ids(data)

    # Step 3: Write extracted data to respective files
    write_to_file(mobile_file, mobile_numbers)
    write_to_file(email_file, email_ids)
    write_to_file(raw_file, data)  # Raw data written as-is

    print("Extraction completed successfully!")

# Run the program
if __name__ == "__main__":
    main()
