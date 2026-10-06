import tiktoken


encoder = tiktoken.get_encoding('gpt2')

#text to token-id
cipher = encoder.encode('Hello, my name is John Doe')

print(cipher)

print(encoder.decode(cipher))


print(tiktoken.list_encoding_names())
 # ['gpt2', 'r50k_base', 'p50k_base', 'p50k_edit', 'cl100k_base', 'o200k_base', 'o200k_harmony']


print(type(tiktoken.encoding_for_model('gpt-4')))

