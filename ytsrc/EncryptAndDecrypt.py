# https://www.youtube.com/shorts/c6wLod7Gvr8
# Ceasars cypher, not a very good method for serious security, but good for practice writing encryption algorithm

# message to be encrypted / decrypted
# inputText = 'secret message'
inputText = 'xjhwjy5rjxxflj'

# encryption / decryption key
key = 5

# encrypt / decrypt
#mode = 'encrypt'
mode = 'decrypt'

# ledger
ledger = 'abcdefghijklmnopqrstuvwxyz 1234567890'

# output message
outputText = ''

# for char in inputText:
#     # find the index of the character in ledger
#     inputIndex = ledger.find(char)
#     # perform encryption / decryption
#     if mode == 'encrypt':
#         outputIndex = inputIndex + key
#     elif mode == 'decrypt':
#         outputIndex = inputIndex - key
#     # handle wraparound
#     if outputIndex >= len(ledger):
#         outputIndex = outputIndex - len(ledger)
#     elif outputIndex < 0:
#         outputIndex = outputIndex + len(ledger)
#     # output
#     outputText = outputText + ledger[outputIndex]

for char in inputText:
    # find the index of the character in ledger
    inputIndex = ledger.find(char)
    # perform encryption / decryption and handle wraparound
    if mode == 'encrypt':
        outputIndex = (inputIndex + key) % len(ledger)
    elif mode == 'decrypt':
        outputIndex = (inputIndex - key) % len(ledger)
    # output
    outputText = outputText + ledger[outputIndex]

print(outputText)

