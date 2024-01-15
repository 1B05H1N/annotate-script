# add-comments.py

`add-comments.py` is a Python script that uses OpenAI's GPT-3 API to automatically generate concise comments and annotations for a Python script. The script inserts comments only where there are no existing comments, and it adds a summary at the top of the script before the import statements.

## Prerequisites

Before using this script, make sure you have the following:

1. OpenAI API Key: You must have an OpenAI API key set as the `OPENAI_API_KEY` environment variable. You can obtain your API key from OpenAI's platform.

2. Python Environment: Ensure you have Python 3 installed on your system.

## Usage

To use the `add-comments.py` script, follow these steps:

1. Save the script with the name `add-comments.py` in your desired directory.

2. Open a terminal and navigate to the directory containing `add-comments.py`.

3. Run the script by providing the path to the Python script you want to annotate as an argument. For example:

   ```shell
   python add-comments.py your_script.py
   ```

4. The script will generate concise comments for your Python script and insert them where they make sense. It will also add a summary at the top of the script.

5. The annotated script will be saved in the same directory with the filename prefixed by "annotated_". For example, if your input script is `your_script.py`, the annotated script will be saved as `annotated_your_script.py`.

6. You can now review and run the annotated script with the added comments.

## Example

Here's an example of how to use the script:

```shell
python add-comments.py my_script.py
```

This will analyze `my_script.py`, add comments, and save the annotated script as `annotated_my_script.py`.

## License

This script is provided under the MIT License. You are free to use, modify, and distribute it as needed.

## Disclaimer

This script is for educational and convenience purposes. It generates comments based on AI predictions and may not always provide perfect results. It's recommended to review and adjust the generated comments as needed for accuracy and clarity.
