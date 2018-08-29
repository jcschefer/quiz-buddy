import re
import string
import json
from os.path import join
from django.conf import settings

# ignore punctuation and digits
tranlsation_table = str.maketrans(dict.fromkeys(string.punctuation + string.digits))
with open(join(settings.BASE_DIR, 'scripts', 'utils', 'commonWords.json'), 'r') as f:
    commonWords = set(json.loads(f.read()))

with open(join(settings.BASE_DIR, 'scripts', 'utils', 'trivialWords.json'), 'r') as f:
    trivialWords = set(json.loads(f.read()))


def get_tossup_keywords(tossup, limit=10):
    result = _regex_keywords(tossup.answer)
    if len(result) < limit:
        result += _regex_keywords(tossup.text_part_3)
    if len(result) < limit:
        result += _regex_keywords(tossup.text_part_2)
    if len(result) < limit:
        result += _regex_keywords(tossup.text_part_1)

    return result[:limit]


def _regex_keywords(text):
    formatted_text = re.sub("[\(\[].*?[\)\]]", " ", text).translate(
        tranlsation_table).replace("\n", " ")
    rareWords = set([word.lower() for word in formatted_text.translate(
        tranlsation_table).strip().split(" ") if (word not in commonWords and word.islower())])
    capWords = set(re.findall(r'(?<!\.\s)\b[A-Z][a-z]*\b',  formatted_text))
    return list(set(c for c in capWords if c not in trivialWords and c.lower() not in trivialWords and len(c) > 3).union(rareWords))
