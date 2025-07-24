
# Blog Generator using LLaMA 2 & Streamlit

This project uses the LLaMA 2 language model with Streamlit to generate blog posts based on user-defined topics, audience type, and word count.

## 🔧 Features
- Choose any blog topic
- Select audience: Common People / Researchers / Data Scientists
- Customize word length
- Download the generated blog as a `.txt` file

## 🛠 Tech Stack
- LLaMA 2 (GGML version via CTransformers)
- Streamlit
- Python

## 📦 How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Download LLaMA 2 model from:
   [https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML)

   Place the `.bin` file (e.g. `llama-2-7b-chat.ggmlv3.q4_0.bin`) into the `/models` folder.

3. Run the app:
```bash
streamlit run app.py
```

## 📍 Live Demo

You can host this on [Streamlit Cloud](https://streamlit.io/cloud).
