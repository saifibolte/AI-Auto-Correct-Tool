# AI Auto-Correct Tool

An AI-driven text correction tool that automatically corrects spelling, grammar, and fluency, designed to function similarly to Grammarly. This tool is built using PySpellChecker for spelling correction and Flan-T5 transformer for grammar and fluency improvement. Proper nouns are preserved to avoid unwanted changes.

## Features 
- Context-aware spelling correction using pyspellchecker
- Grammar & fluency improvement using Hugging Face Flan-T5
- Proper noun preservation to avoid name modifications
- Side-by-side display of original and corrected text
- Real-time suggestions for spelling errors

## Demo
- Input:
  
  ```text
  he dont no how too cook, becuse it taste bad.
  ```
- After Spelling Correction:
  
  ```text
  He don't no how too cook, because it taste bad.
  ```
- After Grammar + Fluency Correction:

  ```text
  He doesn't know how to cook, because it tastes bad.
  ```
## Installation

### 1. Clone the repository:

```text
git clone link
cd directory_name
```

### 2. Create a virtual environment:

```text
python3 -m venv corr-env
source corr-env/bin/activate  # Linux/macOS
# OR on Windows: .\corr-env\Scripts\activate
```

## Usage

Run the streamlit application: 

```text
streamlit run app.py
```
- Enter your text in the text area
- View spelling suggestions and corrected text side by side

## Project Structure

```text
AI-Auto-Correct-Tool/
│── app.py                     # Main Streamlit app
│── modules/
│   ├── preprocessing.py       # Text cleaning utilities
│   ├── spell_corrector.py     # Spelling correction using pyspellchecker
│   └── grammar_corrector.py   # Grammar & fluency correction using Flan-T5
│── requirements.txt
```
## Dependencies

- Python 3.10+
- Streamlit
- PySpellChecker
- Transformers
- PyTorch

## How it works: 

- **Text Cleaning:** Remove extra spaces and normalize input text
- **Spelling Correction:** Word-level correction with pyspellchecker
- **Grammar & Fluency:** Context-aware corrections using Flan-T5
- **Proper Noun Preservation:** Detect and preserve names before grammar correction
- **Display Results:** Side-by-side comparison of original and corrected text
