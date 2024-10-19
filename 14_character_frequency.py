for _ in range(int(input())):
    sentence = input().strip() 
    char_to_find = input().strip()

    occurrence_count = sentence.count(char_to_find)
    print(f"Occurrence of '{char_to_find}' in '{sentence}' = {occurrence_count}")
