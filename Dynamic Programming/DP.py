# collections.defaultdict 사용하기 => 피보나치 수열
def countLetters(word):
    counter = defaultdict(int)
    for letter in word:
        counter[letter] += 1
    return counter
