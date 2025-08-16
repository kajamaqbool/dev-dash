def is_anagram(s1: str,s2: str):
    s1 = str(s1).replace(" ", "").lower()
    s2 = str(s2).replace(" ", "").lower()
    return sorted(s1) == sorted(s2)

if __name__ == "__main__":
    s1 = input()
    s2 = input()

    if is_anagram(s1, s2):
        print("YES")
    else:
        print("NO")