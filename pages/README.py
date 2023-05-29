import streamlit as st
import os

# 定義 page name
st.set_page_config(
        page_title="說明文件",
)

# 獲取目前的工作目錄位置
current_dir = os.getcwd()

# 組合完整的檔案路徑
markdown_file_path = os.path.join(current_dir, "README.md")

st.write(markdown_file_path)

# 讀取 Markdown 檔案的內容
with open(markdown_file_path, "r", encoding='utf-8') as file:
    markdown_content = file.read()

# 在 Streamlit 中呈現 Markdown 內容
st.markdown(markdown_content)
