from indicnlp import common
common.INDIC_RESOURCES_PATH="/home/sourya4/pro/repos/indic_nlp_resources"
from indicnlp import loader

from indicnlp.syllable import  syllabifier


loader.load()
indic_string=u'కార్యదర్శుల'
print(syllabifier.orthographic_syllabify(indic_string,'te'))


# w='जगदीशचंद्र'
# lang='hi'

# print(' '.join(syllabifier.orthographic_syllabify(w,lang)))
