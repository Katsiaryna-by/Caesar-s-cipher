uppercase_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
text = input().split()
encrypted = ''

for i in text:
    count = 0
    for j in i:
        if j.isalpha():
            count += 1
    for j in i:
        index_in_upp = uppercase_alphabet.find(j)
        index_in_low = lowercase_alphabet.find(j)
        new_index_upp = index_in_upp + count
        new_index_low = index_in_low + count
        if j.isalpha():
            if j == j.upper():
                encrypted += uppercase_alphabet[new_index_upp % 26]
            elif j == j.lower():
                encrypted += lowercase_alphabet[new_index_low % 26]
        else:
            encrypted += j
    encrypted += ' '
    
print(encrypted.rstrip())