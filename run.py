import anthropic
import os

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")  
)

with client.messages.stream(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, is this script working? If you see this, it is."}
    ]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
