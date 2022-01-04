for token in doc:
    print({'text': token.text,
           'start': token.idx,
           'end': token.idx + len(token),
           'id': token.i
           })
