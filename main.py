# Text Analyzer
# 1. Obtains paragraph from user, while validating that it is a string and is not empty
import streamlit as st
import re

st.set_page_config(page_title="Text Analyzer", page_icon="📝", layout="wide")
st.title("📝 Text Analyzer")
st.write("Write your paragraph, and we'll analyze it for you!")

# Defaults
if "para_entered" not in st.session_state:
    st.session_state.para_entered = False

# Mark entry of paragraph. Really, to avoid warning of empty paragraph
# right when the page has just loaded.
def mark_para_entry():
    if not st.session_state.para_entered:
        st.session_state.para_entered = True

# Count words in the paragraph.
# For ease, splitting paragraph by spaces and getting the length of the list
# should do the trick.
def count_word(paragraph: str) -> int:
    words = paragraph.split()
    return len(words)

# Count characters in the paragraph, including spaces
def count_char(paragraph: str) -> int:
    return len(paragraph)

# Count vowels in paragraph
def count_vowel(paragraph: str) -> int:
    count = 0
    vowels = ['a','e','i','o','u']
    for char in paragraph.lower():
        if char in vowels:
            count += 1
    return count

# Search and Replace
# Replace all occurrences of the 'search' substring with 'replace' substring
# in the given paragraph
def search_and_replace(paragraph: str):
    if st.session_state.search and st.session_state.replace:
        return paragraph.replace(st.session_state.search,st.session_state.replace)

# Uppercase and lowercase representations
def uppercase_and_lowercase(paragraph: str):
    return paragraph.upper(),paragraph.lower()


# Main Execution
paragraph : str = st.text_area("Enter your paragraph here:",on_change=mark_para_entry)
if paragraph != "":
    st.write("Let's analyze!")

    # 1. Counts
    # Using type castings to convert counts into strings
    st.subheader("Word and Character Count")
    n_words : int = count_word(paragraph)
    n_chars : int = count_char(paragraph)

    # Type castings
    n_words = str(n_words)
    n_chars = str(n_chars)
    st.write(f'''
Words: {n_words}\n\n\
Characters: {n_chars}
''')

    st.subheader("Vowel Count")
    n_vowels : int = count_vowel(paragraph)
    n_vowels = str(n_vowels) 
    st.write(f"Vowels: {n_vowels}")

    # 2. Search and Replace
    st.subheader("Search and Replace")
    [col1,col2] = st.columns(2)
    with col1:
        st.text_input("Search:",key="search")
    with col2:
        st.text_input("Replace:",key="replace")

    if st.session_state.search and st.session_state.replace:
        st.write(f"Converted paragraph: {search_and_replace(paragraph)}")

    # 3. Uppercase and lowercase
    uppercase,lowercase = uppercase_and_lowercase(paragraph)
    st.subheader("Uppercase")
    st.write(uppercase)
    st.subheader("Lowercase")
    st.write(lowercase)

    # 4. Python check and Average word length
    words = paragraph.split()
    n_words = len(words)
    n_chars = 0
    check_once : bool = True
    st.subheader("Python in Paragraph? (have at least one 'Python' in entire paragraph)")
    for word in words:
        # Python check
        if check_once and "Python" in word:
            st.write("At least one instance of word 'Python' exists in the paragraph")
            check_once = False
    
        # Average word length
        word_chars = re.findall("[a-zA-Z0-9]",word)
        if word_chars:
            n_chars += len(word_chars)

    st.subheader("Average word length (total characters **in words** divided by total words")
    if n_words:
        st.write(f"Average word length: {round(n_chars/n_words,2)}")
    
else:
    if st.session_state.para_entered:
        st.warning("Cannot analyze an empty paragraph. Please enter a paragraph.")