from openai import OpenAI
import os
import sys

# Ensure the OpenAI API key is set in environment variables
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    print("Error: OPENAI_API_KEY environment variable not set.")
    sys.exit(1)

client = OpenAI(api_key=api_key)

# Function to read the script content from a file
def read_script(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading the script: {e}")
        sys.exit(1)

# Function to insert comments into the script content
def insert_comments(script_lines, comments):
    annotated_script = []
    comment_lines = comments.split('\n')
    comment_index = 0
    summary_inserted = False

    for script_line in script_lines:
        if comment_index == 0 and not summary_inserted:
            # Insert comment as a summary before the first import statement
            if script_line.startswith("import ") or script_line.startswith("from "):
                annotated_script.append(f"# Summary: {comment_lines[comment_index].strip()}\n")
                summary_inserted = True

        # Check if the line is not empty and there are comments left to insert
        if script_line.strip() and comment_index < len(comment_lines):
            # Insert comment on the same line as the code
            annotated_script.append(script_line.rstrip() + f"  # {comment_lines[comment_index].strip()}\n")
            comment_index += 1
        else:
            # Keep the script line as is
            annotated_script.append(script_line)

    # If there are remaining comments, add them at the end
    while comment_index < len(comment_lines):
        annotated_script.append(comment_lines[comment_index] + "\n")
        comment_index += 1

    return annotated_script

# Function to get the output file path in the same folder with "annotated_" prefix
def get_output_file_path(input_file_path):
    directory, filename = os.path.split(input_file_path)
    annotated_filename = "annotated_" + filename
    return os.path.join(directory, annotated_filename)

# Function to save the annotated script content to a file
def save_annotated_script(annotated_script, file_path):
    try:
        with open(file_path, 'w') as file:
            file.writelines(annotated_script)
    except Exception as e:
        print(f"Error saving the annotated script: {e}")
        sys.exit(1)

# Function to generate comments with OpenAI
def generate_comments_with_openai(code_content):
    """
    Generates code comments/annotations for a script using OpenAI's GPT-3 API.
    - code_content: String content of the script.
    """
    try:
        # Constructing the prompt for OpenAI's GPT-3 model
        prompt = (
            f"Generate concise comments for the script."
        )

        # Generating the comments using OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are going to help analyze my script to generate comments/annotations."},
                {"role": "user", "content": prompt + "\n\n" + code_content}
            ],
        )
        response_message = response.choices[0].message.content

        # Check if the response is empty
        if not response_message.strip():
            print("Received an empty response from OpenAI. Please try again.")
            return None

        return response_message.strip()
    except Exception as e:
        print(f"Error generating comments: {e}")
        return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python analyze_script.py <script_file_path>")
        sys.exit(1)

    input_script = sys.argv[1]

    # Read the script content
    script_content = read_script(input_script)

    # Generate comments with OpenAI
    comments = generate_comments_with_openai("\n".join(script_content))

    # Insert comments into the script content
    annotated_script = insert_comments(script_content, comments)

    # Get the output file path
    output_file = get_output_file_path(input_script)

    # Save the annotated script
    save_annotated_script(annotated_script, output_file)

    print(f"Annotated script saved to {output_file}")

if __name__ == "__main__":
    main()
