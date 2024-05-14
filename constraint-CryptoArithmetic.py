from itertools import permutations

def solveCryptographic(s1, s2, s3):
    letters = set(s1 + s2 + s3)
    if len(letters) > 10:
        print("Invalid strings")
        return False

    for perm in permutations(range(10), len(letters)):
        mapping = {c: v for c, v in zip(letters, perm)}
        if mapping[s1[0]] == 0 or mapping[s2[0]] == 0 or mapping[s3[0]] == 0:
            continue
        val1 = int(''.join(str(mapping[c]) for c in s1))
        val2 = int(''.join(str(mapping[c]) for c in s2))
        val3 = int(''.join(str(mapping[c]) for c in s3))
        if val1 + val2 == val3:
            print("\nSolution found:")
            for c, v in mapping.items():
                print(c, "=", v)
            return True

    print("No solution")
    return False


s1 = input("String 1: ")
s2 = input("String 2: ")
s3 = input("Result String: ")
solveCryptographic(s1, s2, s3)