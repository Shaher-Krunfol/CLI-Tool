class LogParser:

    def __init__(self, fileName):
        self.fileName = fileName
        self.logs = []

    def load_file(self):
        try:
            with open(self.fileName, 'r') as file:
                self.logs = file.readlines()
        except PermissionError:
            print(f"Permission denied while trying to read {self.fileName}.")
            return False
        except FileNotFoundError:
            print(f"File {self.fileName} not found.")
            return False
        return True
    
    def filter_lines(self, errors_only=False):
        filtered_lines = []
        lineNumber = 0
        firstTimestamp = None
        lastTimestamp = None

        for line in self.logs:
            lineNumber += 1
            lower_line = line.lower()

            # Filter lines
            if errors_only:
                if 'error' in lower_line:
                    filtered_lines.append(line)
            else:
                if 'error' in lower_line or 'warning' in lower_line:
                    filtered_lines.append(line)


            # Timestamp detection
            if line.startswith('[') and len(line) >= 20:
                timestamp = line.split(']')[0].strip('[]')
                if not firstTimestamp:
                    firstTimestamp = timestamp
                lastTimestamp = timestamp

        return filtered_lines, firstTimestamp, lastTimestamp
    
    def get_summary(self, filtered_lines, first_timestamp, last_timestamp):
        print(f"\n Total lines in file: {len(self.logs)}")

        if filtered_lines:
            print(f"Found {len(filtered_lines)} matching lines:\n")
            print("--- Filtered Lines ---")
            for line in filtered_lines:
                print(line.strip())
            print("--- End of Filtered Lines ---\n")
        else:
            print("No matching lines found in the file.")

        if first_timestamp and last_timestamp:
            print(f"First timestamp: {first_timestamp}")
            print(f"Last timestamp:  {last_timestamp}")
        else:
            print("No valid timestamps found.")

    def save_filtered_results(self, filtered_lines, auto_save=False, output_file="filteredResults.txt"):
        if not filtered_lines:
            print("No filtered lines to save.")
            return

        if auto_save:
            choice = "yes"
        else:
            choice = input("Do you want to save the filtered results to a file? (yes/no): ").strip().lower()

        if choice == "yes":
            try:
                with open(output_file, 'w') as output:
                    output.writelines(filtered_lines)
                print(f"Filtered results saved to '{output_file}'.")
            except Exception as e:
                print(f"An error occurred while saving the file: {e}")
        else:
            print("Save cancelled.")

    def run(self, errors_only=False, auto_save=False, output_file="filteredResults.txt"):
        if not self.load_file():
            return

        filtered_lines, first_timestamp, last_timestamp = self.filter_lines(errors_only)
        self.get_summary(filtered_lines, first_timestamp, last_timestamp)
        self.save_filtered_results(filtered_lines, auto_save=auto_save, output_file=output_file)

if __name__ == "__main__":
    import argparse
    parser_cli = argparse.ArgumentParser(description="Log Inspector CLI Tool")
    parser_cli.add_argument("file", help="The log file to analyze")
    parser_cli.add_argument("--save", action="store_true", help="Automatically save filtered results")
    parser_cli.add_argument("--errors-only", action="store_true", help="Show only 'error' lines")
    parser_cli.add_argument("--output", default="filteredResults.txt", help="Custom output file name")

    args = parser_cli.parse_args()

    parser = LogParser(args.file)
    parser.run(errors_only=args.errors_only, auto_save=args.save, output_file=args.output)


