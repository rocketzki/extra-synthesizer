from enchant import DictWithPWL
import enchant
import re

pl_dict = enchant.Dict("pl_PL")
sentence_expr = re.compile(r'\s+[^.!?]*[.!?]')


def to_sentences(text: str):
    text = " " + text
    return sentence_expr.findall(text)


def tokenize(sentence: str):
    return (" ".join(sentence.split())).split(" ")


def dict_lookup(in_text, input_type='multi'):
    if input_type == 'single':
        return pl_dict.check(in_text)
    elif input_type == 'multi':
        result = []
        for v in tokenize(in_text):
            result.append({"word": v, "result": pl_dict.check(re.sub(r'[?.|;!]$', "", v))})
        return result
    else:
        raise AttributeError('No such option: ' + input_type)
