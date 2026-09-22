import tiktoken


encoder = tiktoken.get_encoding('gpt2')

cipher = encoder.encode('Hello, my name is John Doe')

print(cipher)

print(encoder.decode(cipher))