import plac
import spacy
from spacy import English
from spacy.gold import GoldParse


def main(out_loc):
    nlp = English(parser=False) # Avoid loading the parser, for quick load times
    # Run the tokenizer and tagger (but not the entity recognizer)
    doc = nlp.tokenizer(u'Lions and tigers and grizzly bears!')
    nlp.tagger(doc) 

    nlp.entity.add_label('ANIMAL') # <-- New in v0.100

    # Create a GoldParse object. This should have a better API...
    indices = tuple(range(len(doc)))
    words = [w.text for w in doc]
    tags = [w.tag_ for w in doc]
    heads = [0 for _ in doc]
    deps = ['' for _ in doc]
    # This is the only part we care about. We want BILOU format
    ner = ['U-ANIMAL', 'O', 'U-ANIMAL', 'O', 'B-ANIMAL', 'L-ANIMAL', 'O']

    # Create the GoldParse
    annot = GoldParse(doc, (indices, words, tags, heads, deps, ner))

    # Update the weights with the example
    # Here we iterate until we get it entirely correct. In practice this is probably a bad idea.
    # Note that we've added a class to the existing model here! We "resume"
    # training the previous model. Whether this is good or not I can't say, you'll have to
    # experiment.
    loss = nlp.entity.train(doc, annot)
    i = 0
    while loss != 0 and i < 1000:
        loss = nlp.entity.train(doc, annot)
        i += 1
    print("Used %d iterations" % i)

    nlp.entity(doc)
    for ent in doc.ents:
        print(ent.text, ent.label_)
    nlp.entity.model.dump(out_loc)

if __name__ == '__main__':
    plac.call(main)