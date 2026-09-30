import streamlit as st
import requests
import json

st.title("🤖 Llama Live Chat")

# Enter press panna send aagara trick - form
with st.form("my_form", clear_on_submit=False):
    prompt = st.text_input("Prompt:", placeholder="Type here and press Enter...")
    submitted = st.form_submit_button("Ask ")

if submitted:
    if prompt.strip() == "":
        st.warning("Prompt type pannu bro")
    else:
        url = "http://localhost:11434/api/generate"
        data = {"model": "llama3.2:1b", "prompt": prompt, "stream": True}

        response = requests.post(url, json=data, stream=True)
        
        full_text = ""
        placeholder = st.empty()

        for line in response.iter_lines():
            if line:
                j = json.loads(line.decode('utf-8'))
                full_text += j.get("response", "")
                placeholder.markdown(full_text)
                if j.get("done"):
                    break