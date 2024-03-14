import json

def split_json_file(input_file_path, lines_per_file=100):
    """
    Splits a large JSON file into smaller files, each containing up to a specified
    number of lines, and prints progress updates on the number of chunks created.

    Parameters:
    - input_file_path: Path to the input JSON file.
    - lines_per_file: Number of lines each output file should contain.
    """
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        file_number = 1
        lines_in_current_file = 0
        current_file_content = []

        for line in input_file:
            current_file_content.append(json.loads(line))  # Convert string to JSON object
            lines_in_current_file += 1

            if lines_in_current_file == lines_per_file:
                output_file_path = f"{input_file_path[:-5]}_chunk{file_number}.json"
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    json.dump(current_file_content, output_file, ensure_ascii=False, indent=4)

                print(f"Chunk {file_number} created.")  # Progress update
                file_number += 1
                lines_in_current_file = 0
                current_file_content = []

        # Save any remaining content to a new file
        if current_file_content:
            output_file_path = f"{input_file_path[:-5]}_chunk{file_number}.json"
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                json.dump(current_file_content, output_file, ensure_ascii=False, indent=4)
            print(f"Chunk {file_number} created.")  # Final chunk progress update

# Example usage
input_file_path = r'C:\Users\leonw\Desktop\JsonFiles\corpus-webis-shortened.json'
split_json_file(input_file_path)
