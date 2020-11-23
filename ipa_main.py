from pprint import pprint

nat_classes = {
    'Major Natural Classes': ['Vowel', 'Consonant', 'Sonorant', 'Obstruent'],
    'Manner of Articulation Natural Classes': ['Glide', 'Liquid', 'Lateral', 'Rhotic', 'Nasal', 'Fricative', 'Stop', 'Affricate'],
    'Major Place of Articulation Natural Classes for Consonants': ['Labial', 'Coronal', 'Dorsal', 'Laryngeal'],
    'Place of Articulation Natural Classes for Vowels': ['High', 'Mid', 'Low', 'Front', 'Central', 'Back', 'Rounded', 'Unrounded']
}
features = [
    "consonant", "vowel", "sonorant", "obstruent", "glide", "liquid", 
    "lateral", "rhotic", "nasal", "affricate", "fricative", "stop",
    "labial", "coronal", "dorsal", "laryngeal", 
    "high", "mid", "low", "front", "central", "back", "rounded", "unrounded"
]


def ipaFeatures_dict() -> dict:
    """Returns a dict with ipa consonant/vowel as the key and a list of natural classes."""
    ipa_dict = {}
    with open("ipaFeatures_new.csv", "r") as f:
        f.readline()
        for row in f:
            row = row.rstrip().split(",")
            ipa_dict[row[0]] = []
            if row[1] == "+":
                for ind, ele in enumerate(row[1:-8]):
                    if ele == "+":
                        ipa_dict[row[0]].append(features[ind])
            else:
                for ind, ele in enumerate(row[1:]):
                    if not(12 <= ind <= 15) and ele == "+":
                        ipa_dict[row[0]].append(features[ind])
    return ipa_dict


def final_ipa_dict() -> dict:
    """Returns the ipaFeatures dict with added ipa_symbols and description."""
    ipa_dict = ipaFeatures_dict()
    with open("ipa_new.csv", "r") as f:
        f.readline()
        for row in f:
            row = row.split(",")
            if row[0] not in ipa_dict and len(row[0].split()) == 1:
                ipa_dict[row[0]] = [row[0], row[2].rstrip(), row[1]]
            elif len(row[0].split()) == 1: 
                ipa_dict[row[0]] = [row[0], row[2].rstrip(), ipa_dict[row[0]]]
            else:
                symbols = row[0].split()
                for symbol in symbols:
                    if symbol in ipa_dict:
                        symbol_in_dict = symbol
                        break
                for symbol in symbols:
                    ipa_dict[symbol] = [row[0], row[2].rstrip(), ipa_dict[symbol_in_dict]]
    return ipa_dict


ipa_dict = final_ipa_dict()
def final_output(ipa: str, gui=True) -> list:
    """Returns a list of: ipa symbol(s), description and natural classes."""
    if ipa not in ipa_dict:
        return False
    ipa, desc, cat_or_class = ipa_dict[ipa]
    if type(cat_or_class) == str:
        cat_or_class = [cat_or_class]
        last_line = f"Category: {cat_or_class}"
    else:
        last_line = f"Natural Classes: {cat_or_class}"
    if gui:
        return ipa.split(' '), desc.split(' '), cat_or_class
    output =  f"IPA Symbol(s): {ipa}\n" + f"Description: {desc}\n" + last_line
    return output

# final_output("w")