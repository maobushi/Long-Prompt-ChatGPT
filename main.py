import streamlit as st
import pyperclip

def split_text(input_text, length):
    return [input_text[i:i+length] for i in range(0, len(input_text), length)]

st.title('Long Prompt Splitter')

# 入力欄の作成
text_A = st.text_area('Long prompt input field', '')
text_B = st.text_area('instruction input field', '上記の文章は全体のテキストの一部です。まだまとめないでください。')
macro_length = st.number_input('Number of delimiters', min_value=1, value=10000, step=1)

# テキストを指定された長さで分割
splitted_texts = split_text(text_A, macro_length)

# クリップボードにコピーするテキストのインデックス
index = st.session_state.get('index', 0)

# 進捗バーの表示
progress = st.progress(0)
if len(splitted_texts) > 0:
    progress.progress(index / len(splitted_texts))

if st.button('クリップボードコピー'):
    if index < len(splitted_texts):
        combined_text = splitted_texts[index] + '\n' + text_B
        pyperclip.copy(combined_text)
        st.write(f'コピーされたテキスト:\n{combined_text}')
        st.session_state.index = index + 1
    else:
        st.write('全てのテキストがコピーされました。')

if 'index' in st.session_state and st.session_state.index >= len(splitted_texts):
    st.session_state.index = 0
