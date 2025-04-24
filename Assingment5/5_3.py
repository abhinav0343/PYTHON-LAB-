def next_lexicographic_permutation(w):
    from itertools import permutations
    
    all_permutations = sorted(''.join(p) for p in permutations(w))
    # it will generate all possible permutations and in smalller to bigger order (according to ASCII)

    current_index = all_permutations.index(w)
    #current_index stores index of the word W entered by user .

    if current_index == len(all_permutations) - 1:
        return "no answer"
    elif all_permutations[current_index] == all_permutations[current_index+1] :
        return "no answer"
    else:
        next_permutation = all_permutations[current_index + 1]
        return next_permutation

t = int(input("Enter number of test cases: "))
for _ in range(t):
    w = input("Enter a word: ")
    print(next_lexicographic_permutation(w))