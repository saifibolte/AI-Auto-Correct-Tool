import streamlit as st
from modules.preprocessing import clean_text
from modules.spell_corrector import correct_spelling, get_spell_suggestions
from modules.grammar_corrector import correct_grammar_and_fluency

st.set_page_config(page_title="AI Grammarly Tool", layout="wide")
st.title("📝 AI Auto Correct Tool")
st.write("Check spellings and grammar.")

user_input = st.text_area("Enter your text:", height=200, placeholder="Type here...")

if user_input.strip():
    cleaned = clean_text(user_input)

    # Spell suggestions
    spell_suggestions = get_spell_suggestions(cleaned)
    corrected_spelling = correct_spelling(cleaned)

    # Grammar & fluency
    corrected_text = correct_grammar_and_fluency(corrected_spelling)

    col1, col2 = st.columns(2)

    # Original + Spell Suggestions
    with col1:
        st.subheader("Original Text")
        st.write(user_input)

        if spell_suggestions:
            st.markdown("**Spelling Suggestions:**")
            for wrong, suggestion in spell_suggestions.items():
                st.write(f"- {wrong} → {suggestion}")
        else:
            st.write("No spelling errors detected.")

    # Corrected Text
    with col2:
        st.subheader("Corrected Text")
        st.write(corrected_text)
