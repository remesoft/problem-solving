for _ in range(int(input())):
    text = input()
    words = text.split()
    
    reversed_words = ' '.join(word[::-1] for word in words)
    print(reversed_words)