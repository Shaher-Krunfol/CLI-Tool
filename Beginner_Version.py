import os

print(f"Current working directory: {os.getcwd()}")


def filtering():
    file_name = input("Please, enter the file name: ").strip()
    line_number = 0
    filtered_lines = []
    first_timestamp = None
    last_timestamp = None

    try:
        with open(file_name, 'r') as file:
            for line in file:
                line_number += 1
                line_lower = line.lower()

                # Filter lines
                if 'error' in line_lower or 'warning' in line_lower:
                    print(f"Line {line_number}: {line.strip()}")
                    filtered_lines.append(line)

                # Timestamp detection
                if line.startswith('[') and len(line) >= 20:
                    timestamp = line.split(']')[0].strip('[]')
                    if not first_timestamp:
                        first_timestamp = timestamp
                    last_timestamp = timestamp

        print(f"\nTotal lines in file: {line_number}")

        if filtered_lines:
            print(f"Found {len(filtered_lines)} lines with 'error' or 'warning'.")
        else:
            print("No 'error' or 'warning' found in the file.")

        if first_timestamp and last_timestamp:
            print(f"\nFirst timestamp: {first_timestamp}")
            print(f"Last timestamp:  {last_timestamp}")
        else:
            print("No valid timestamps found.")

    except FileNotFoundError:
        print("File not found. Please try again.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    # Ask to save
    choice = input("Do you want to save the filtered results to a file? (yes/no): ").strip().lower()
    if choice == "yes":
        try:
            with open("filtered_results.txt", 'w') as output_file:
                output_file.writelines(filtered_lines)
            print("Filtered results saved to 'filtered_results.txt'.")
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")


if __name__ == "__main__":
    filtering()
