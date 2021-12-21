import spacy
from scipy.spatial.distance import cosine
nlp = spacy.load('en_core_web_lg')


def vector_similarity(x, y):
    return 1 - cosine(x, y)


def make_guess_word(words):
    [first, second, third] = words
    return nlp.vocab[first].vector - nlp.vocab[second].vector + nlp.vocab[third].vector


def get_similar_word(words, scope=nlp.vocab):

    guess_word = make_guess_word(words)

    similarities = []

    for word in scope:
        if not word.has_vector:
            continue

        similarity = vector_similarity(guess_word, word.vector)
        similarities.append((word, similarity))

    similarities = sorted(similarities, key=lambda item: -item[1])
    print([word[0].text for word in similarities[:10]])


words = ["king", "queen", "woman"]
get_similar_word(words)
