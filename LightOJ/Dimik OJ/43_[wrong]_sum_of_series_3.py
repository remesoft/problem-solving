for _ in range(int(input())):
    number = int(input()) 
    terms = []
    
    for i in range(number, 1, -1):
        terms.append(f"2^{i}")

    terms.append("2")
    terms.append("1")
    
    print(" + ".join(terms))