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
st.subheader("Original Paragraph")
paragraph : str = st.text_area("Enter your paragraph here:",on_change=mark_para_entry,label_visibility="hidden")
if paragraph != "":

    # 1. Counts
    # Using type castings to convert counts into strings
    n_words : int = count_word(paragraph)
    n_chars : int = count_char(paragraph)
    n_vowels : int = count_vowel(paragraph)

    # Type castings
    n_words = str(n_words)
    n_chars = str(n_chars)
    n_vowels = str(n_vowels) 
    st.write(f'''
Total Words: {n_words}\n\n\
Total Characters: {n_chars}\n\n\
Number of vowels: {n_vowels}
''')

    # 2. Python check and Average word length
    words = paragraph.split()
    n_words = len(words)
    n_chars = 0
    check_once : bool = True
    for word in words:
        # Python check
        if check_once and "Python" in word:
            check_once = False
    
        # Average word length parameters
        word_chars = re.findall("[a-zA-Z0-9]",word)
        if word_chars:
            n_chars += len(word_chars)

    st.subheader("Does the paragraph contain the word 'Python'?")
    st.write("Yes" if not check_once else "No")
 
    # 2. Search and Replace
    [col1,col2] = st.columns(2)
    with col1:
        st.subheader("Enter a word to search for:")
        st.text_input("Search:",key="search",label_visibility="hidden")
    with col2:
        st.subheader("Enter a word to replace with:")
        st.text_input("Replace:",key="replace",label_visibility="hidden")

    if st.session_state.search and st.session_state.replace:
        paragraph = search_and_replace(paragraph)
        st.subheader("Modified Paragraph:")
        st.write(paragraph)

    # 3. Uppercase and lowercase
    uppercase,lowercase = uppercase_and_lowercase(paragraph)
    st.subheader("Paragraph in Uppercase")
    st.write(uppercase)
    st.subheader("Paragraph in Lowercase")
    st.write(lowercase)


    st.subheader("Average word length")
    if n_words:
        st.write(f"{round(n_chars/n_words,2)}")
    
else:
    if st.session_state.para_entered:
        st.warning("Cannot analyze an empty paragraph. Please enter a paragraph.")