# log_parser.py (Advanced Streaming Version with --levels)

class LogParser:
    def __init__(self, file_name):
        self.file_name = file_name

    # Decorator to measure runtime
    def measure_time(func):
        def wrapper(*args, **kwargs):
            import time
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"\nFinished in {end - start:.2f} seconds")
            return result
        return wrapper

    # Generator: yields one line at a time (no big memory usage)
    def load_file(self):
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    yield line
        except PermissionError:
            print(f"Permission denied while trying to read {self.file_name}.")
            return
        except FileNotFoundError:
            print(f"File '{self.file_name}' not found.")
            return

    # Filters while streaming
    def filter_lines(self, levels=None, output_file="filteredResults.txt"):
        line_number = 0
        match_count = 0
        first_timestamp = None
        last_timestamp = None

        # Normalize levels to lowercase if provided
        if levels:
            levels = [lvl.lower() for lvl in levels]

        with open(output_file, 'w') as output:
            for line in self.load_file():
                line_number += 1
                lower_line = line.lower()

                # Match filter logic dynamically
                if levels:  
                    if any(level in lower_line for level in levels):
                        output.write(line)
                        match_count += 1
                else:  # default to error & warning
                    if 'error' in lower_line or 'warning' in lower_line:
                        output.write(line)
                        match_count += 1

                # Timestamp detection
                if line.startswith('[') and len(line) >= 20:
                    timestamp = line.split(']')[0].strip('[]')
                    if not first_timestamp:
                        first_timestamp = timestamp
                    last_timestamp = timestamp

        return line_number, match_count, first_timestamp, last_timestamp, output_file

    @measure_time
    def run(self, levels=None, output_file="filteredResults.txt"):
        # Process file directly with streaming
        line_number, match_count, first_timestamp, last_timestamp, saved_file = self.filter_lines(
            levels=levels,
            output_file=output_file
        )

        # Print summary
        print("\n--- SUMMARY ---")
        print(f"Total lines processed: {line_number}")
        print(f"Matches found: {match_count}")
        print(f"Matches saved to: {saved_file}")
        if first_timestamp and last_timestamp:
            print(f"First timestamp: {first_timestamp}")
            print(f"Last timestamp:  {last_timestamp}")
        else:
            print("⚠No valid timestamps found.")

if __name__ == "__main__":
    import argparse

    parser_cli = argparse.ArgumentParser(description="Log Inspector CLI Tool (Streaming Version)")

    # Required file argument
    parser_cli.add_argument("file", help="The log file to analyze")

    # Optional arguments
    parser_cli.add_argument("--levels", help="Comma-separated log levels to filter (e.g., ERROR,INFO)")
    parser_cli.add_argument("--output", default="filteredResults.txt", help="Custom output file name")

    args = parser_cli.parse_args()

    # Parse levels into a list if provided, else None
    levels = args.levels.split(",") if args.levels else None

    parser = LogParser(args.file)
    parser.run(levels=levels, output_file=args.output)
