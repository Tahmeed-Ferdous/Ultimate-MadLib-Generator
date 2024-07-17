#MadLib Generator

def is_vowel(char):
    return char.lower() in 'aeiou'
with open('sentence.txt', 'r') as file:
    story=file.read()

words, words_old, start, target1, target2= [], [], '-1', '(', ')'
for i in range(len(story)):
    if story[i]==target1:
        start=i
    if story[i]==target2 and start!=-1:
        word=story[start:i+1]
        if word not in words:
            words_old.append(word)
            words.append(word)

for i in range(len(words)):
    if words[i]=='(adjective)':
        answers=input('write an '+ str(words[i].strip('()')) + ': ')
        words[i]=answers
    if words[i]=='(adjective1)':
        answers=input('write an '+ str(words[i].strip('()')) + ': ')
        words[i]=answers
    if words[i]=='(adjective2)':
        answers=input('write an '+ str(words[i].strip('()')) + ': ')
        words[i]=answers
    if words[i]=='(noun)':
        answers=input('write a '+ str(words[i].strip('()')) + ': ')
        words[i]=answers
    if words[i]=='(name)':
        answers=input('write a '+ str(words[i].strip('()')) + ': ')
        words[i]=answers
    if words[i]=='(verb)':
        answers=input('write a '+ str(words[i].strip('()')) + ': ')
        words[i]=answers
    if words[i]=='(place)':
        answers=input('write a '+ str(words[i].strip('()')) + ': ')
        words[i]=answers
    if words[i]=='(animal)':
        answers=input('write an '+ str(words[i].strip('()')) + ': ')
        words[i]=answers
    if words[i]=='(plural noun)':
        answers=input('write a '+ str(words[i].strip('()')) + ': ')
        words[i]=answers

for i in range(len(words_old)):
    story=story.replace(words_old[i], words[i])

story_words = story.split()
for i in range(len(story_words) - 1):
    if story_words[i].lower() == 'a' and is_vowel(story_words[i + 1][0]):
        story_words[i] = 'an'
    elif story_words[i].lower() == 'an' and not is_vowel(story_words[i + 1][0]):
        story_words[i] = 'a'
story = ' '.join(story_words)
print('\n'+ story + '\n')
