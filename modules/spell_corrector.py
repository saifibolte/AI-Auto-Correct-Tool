from spellchecker import SpellChecker
import re

spell = SpellChecker()

def get_spell_suggestions(text: str):
    """
    Returns a dict of misspelled words and their suggestions.
    """
    words = re.findall(r"\w+", text)
    suggestions = {}
    for word in words:
        if word.lower() not in spell:
            corrected = spell.correction(word)
            if corrected and corrected.lower() != word.lower():
                suggestions[word] = corrected
    return suggestions

def correct_spelling(text: str) -> str:
    """
    Corrects spelling errors while preserving capitalization and punctuation.
    """
    tokens = re.findall(r"\w+|[^\w\s]", text, re.UNICODE)
    corrected_tokens = []

    for token in tokens:
        if token.isalpha():
            lower = token.lower()
            if lower in spell:
                corrected = token
            else:
                corrected = spell.correction(lower) or token
            if token[0].isupper():
                corrected = corrected.capitalize()
            corrected_tokens.append(corrected)
        else:
            corrected_tokens.append(token)

    return " ".join(corrected_tokens).replace(" n't", "n't")
