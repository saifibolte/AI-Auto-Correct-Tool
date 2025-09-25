from transformers import pipeline
import re

grammar_model = pipeline(
    "text2text-generation",
    model="pszemraj/flan-t5-large-grammar-synthesis"
)

def correct_grammar_and_fluency(text: str) -> str:
    """
    Corrects grammar and fluency while preserving proper nouns.
    """
    # Detect capitalized words / names
    names = re.findall(r'\b[A-Z][a-z]*\b', text)
    placeholders = {}
    for i, name in enumerate(names):
        placeholder = f"__NAME{i}__"
        placeholders[placeholder] = name
        text = text.replace(name, placeholder)

    # Grammar + fluency correction
    result = grammar_model(text, max_length=256, do_sample=False)
    corrected = result[0]['generated_text']

    # Restore names
    for placeholder, name in placeholders.items():
        corrected = corrected.replace(placeholder, name)

    return corrected
