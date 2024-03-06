import json
import random

def filter_json_file(input_file_path, output_file_path, total_lines, keep_prob=0.1):
    """
    Filters a large JSON file by keeping only a specified percentage of its lines.
    Additionally, prints the number of lines processed and the progress.

    Parameters:
    - input_file_path: Path to the input JSON file.
    - output_file_path: Path where the filtered JSON file will be saved.
    - total_lines: Total number of lines in the input file.
    - keep_prob: Probability of keeping any given line. Defaults to 0.1 (10%).
    """
    lines_read = 0
    lines_written = 0
    
    with open(input_file_path, 'r', encoding='utf-8') as input_file, \
         open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line in input_file:
            lines_read += 1
            if random.random() < keep_prob:
                # Keep this line with a probability of keep_prob
                output_file.write(line)
                lines_written += 1
            
            if lines_read % 1000 == 0:  # Update progress for every 1000 lines read
                progress = (lines_read / total_lines) * 100
                print(f"Lines read: {lines_read}/{total_lines} ({progress:.2f}%), Lines written: {lines_written}")

# Example usage
input_file_path = r'C:\Users\leonw\Desktop\corpus-webis-tldr-17.json'
output_file_path = r'C:\Users\leonw\Desktop\corpus-webis-shortened.json'
total_lines = 3848331  # Total number of lines in the input file

filter_json_file(input_file_path, output_file_path, total_lines)
