import argparse
import gpt


def generate_python_code(task):
    prompt = f"""Write a Python program that {task} and only returns the code.
    
    The code should be well documented, including logging using the logging library and docstrings for all functions.
    The code should be organized into functions, including a main function and separate functions for each task.
    The code should adhere to PEP8 standards and be well-formatted and readable.
    Finally, the code should be runnable via the command line using the argparse library.
    """
    response = gpt.generate_completion("text-davinci-003", prompt, 0, 1000)
    return response


def main():
    # Define command-line arguments using argparse
    parser = argparse.ArgumentParser(
        description="Generate Python code for a specified task."
    )
    parser.add_argument("task", type=str, help="the task to generate code for")
    parser.add_argument(
        "--output-file",
        type=str,
        default="output.py",
        help="the file to save the generated code to",
    )

    # Parse command-line arguments
    args = parser.parse_args()

    # Generate the Python code for the specified task using GPT
    generated_code = generate_python_code(args.task)

    # Write the generated code to the specified output file
    with open(args.output_file, "w") as f:
        f.write(generated_code)

    # Print a message to the console indicating where the generated code was saved
    print(f"Generated code saved to {args.output_file}.")


if __name__ == "__main__":
    main()
