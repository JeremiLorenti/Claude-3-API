# Anthropic API Python Starter Template

This is a starter template for using the Anthropic API with Python. It demonstrates how to use the `anthropic` Python package to interact with the API and generate text using the powerful `claude-3-opus-20240229` model.

## Prerequisites

Before running this script, ensure you have the following:

1. Python 3.6 or later installed on your system.
2. An API key from Anthropic. You can obtain one by signing up on the Anthropic website.

## Setup

1. Install the `anthropic` Python package by running the following command:

```bash
pip install anthropic
```

2. Set your Anthropic API key as an environment variable. This is important for security reasons, as it prevents your API key from being exposed in your code. You can set the environment variable using the following command:

- For Unix-like systems (Linux, macOS):
  ```bash
  export ANTHROPIC_API_KEY=your_api_key
  ```

- For Windows:
  ```bash
  set ANTHROPIC_API_KEY=your_api_key
  ```

  Replace `your_api_key` with your actual Anthropic API key.

## Usage

1. Clone or download this starter template to your local machine.

2. Open the `run.py` file in a text editor.

3. Customize the user message if desired. You can modify the `messages` list to include your own user message for testing or experimentation. For example:

```python
messages=[
    {"role": "user", "content": "Hello Claude, how are you doing today?"}
]
```

4. Save the changes to the `run.py` file.

5. Open a terminal or command prompt and navigate to the directory where the `run.py` file is located.

6. Run the script using the following command:

```bash
python run.py
```

7. The script will send the user message to the Anthropic API and stream the generated response from the `claude-3-opus-20240229` model. The response will be printed in the console.

## Customization

You can customize various aspects of the script to suit your needs:

- **Model**: If you want to use a different Claude model, update the `model` parameter in the `client.messages.stream()` function call. Make sure to use a compatible model version.

- **Max Tokens**: Adjust the `max_tokens` parameter to control the maximum number of tokens (words or word pieces) in the generated response. Keep in mind that increasing this value may result in longer response times and higher API usage costs.

- **User Message**: Modify the `messages` list to include your own user messages for testing or experimentation. You can add multiple user messages to simulate a conversation flow.

## Compatibility

This starter template is compatible with all Claude models up to version 3. It has been tested with the `claude-3-opus-20240229` model, but you can use other compatible models as well.

## Troubleshooting

If you encounter any issues while running the script, consider the following:

- Make sure you have a valid Anthropic API key set as an environment variable.
- Ensure that you have installed the `anthropic` Python package correctly.
- Verify that you are using a compatible Python version (3.6 or later).
- Check the Anthropic API documentation for any updates or changes to the API usage.