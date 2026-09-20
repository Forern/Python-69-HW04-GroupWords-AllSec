def group_by_signature(words: list) -> list:
    group = {}
    
    for word in words:
        if word == "":
            continue
        
        signature = ''.join(sorted(word))
        
        if signature not in group:
            group[signature] = []
            
        group[signature].append(word)
        
    return list(group.values())

if __name__ == "__main__":
    # Example 1
    words = ["abc", "bca", "cab", "bac", "xyz", "yxz", "zxy", "dog"]
    print(group_by_signature(words))
    # Output: [["abc", "bca", "cab", "bac"], ["xyz", "yxz", "zxy"], ["dog"]]

    # Example 2
    words = ["apple", "pale", "leap", "plea", "papel", "hello"]
    print(group_by_signature(words))
    # Output: [["apple", "papel"], ["pale", "leap", "plea"], ["hello"]]
