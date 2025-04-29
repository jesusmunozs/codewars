def generate_hashtag(s):
    result = "#"
    words = s.split()
    for i in range(len(words)):
        words[i] = words[i].capitalize()
        result += words[i]

    if s == "" or len(result) > 140:
        return False
    
    return result

print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'))
