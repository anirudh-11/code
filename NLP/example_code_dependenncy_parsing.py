from __future__ import print_function, unicode_literals, division

from bz2 import BZ2File
import time
import plac
import json

from spacy.matcher import PhraseMatcher
import spacy


@plac.annotations(
    patterns_loc=("Path to gazetteer", "positional", None, str),
    text_loc=("Path to Reddit corpus file", "positional", None, str),
    n=("Number of texts to read", "option", "n", int),
    lang=("Language class to initialise", "option", "l", str),
)
def main(patterns_loc, text_loc, n=10000, lang="en"):
    nlp = spacy.blank(lang)
    nlp.vocab.lex_attr_getters = {}
    phrases = read_gazetteer(nlp.tokenizer, patterns_loc)
    count = 0
    t1 = time.time()
    for ent_id, text in get_matches(nlp.tokenizer, phrases, read_text(text_loc, n=n)):
        count += 1
    t2 = time.time()
    print("%d docs in %.3f s. %d matches" % (n, (t2 - t1), count))


def read_gazetteer(tokenizer, loc, n=-1):
    for i, line in enumerate(open(loc)):
        data = json.loads(line.strip())
        phrase = tokenizer(data["text"])
        for w in phrase:
            _ = tokenizer.vocab[w.text]
        if len(phrase) >= 2:
            yield phrase


def read_text(bz2_loc, n=10000):
    with BZ2File(bz2_loc) as file_:
        for i, line in enumerate(file_):
            data = json.loads(line)
            yield data["body"]
            if i >= n:
                break


def get_matches(tokenizer, phrases, texts, max_length=6):
    matcher = PhraseMatcher(tokenizer.vocab, max_length=max_length)
    matcher.add("Phrase", None, *phrases)
    for text in texts:
        doc = tokenizer(text)
        for w in doc:
            _ = doc.vocab[w.text]
        matches = matcher(doc)
        for ent_id, start, end in matches:
            yield (ent_id, doc[start:end].text)


if __name__ == "__main__":
    if False:
        import cProfile
        import pstats

        cProfile.runctx("plac.call(main)", globals(), locals(), "Profile.prof")
        s = pstats.Stats("Profile.prof")
        s.strip_dirs().sort_stats("time").print_stats()
    else:
        plac.call(main)