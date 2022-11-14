alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(input_text, input_shift):
  encrypted_list = []
  for letter in input_text:
    index = alphabet.index(letter)
    encrypted_list.append(alphabet[index + input_shift])

  encrypted_word = "".join(encrypted_list)
  print(encrypted_word)

encrypt(text, shift)
