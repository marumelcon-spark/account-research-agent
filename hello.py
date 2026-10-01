import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from your environment

response = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "In one sentence, what does an account-research agent do for a sales rep?"}],
)

for block in response.content:
    if block.type == "text":
        print(block.text)