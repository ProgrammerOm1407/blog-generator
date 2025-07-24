
import streamlit as st
from ctransformers import AutoModelForCausalLM

# Load LLaMA 2 model (make sure model file is in /models folder)
@st.cache_resource
def load_model():
    model = AutoModelForCausalLM.from_pretrained(
        "./models",
        model_type="llama",
        model_file="llama-2-7b-chat.ggmlv3.q4_0.bin",  # Replace if you use another version
        max_new_tokens=500,
        temperature=0.7
    )
    return model

model = load_model()

# Streamlit UI
st.set_page_config(page_title="Blog Generator", layout="centered")
st.title("📝 AI Blog Generator")
st.markdown("Generate customized blog posts using LLaMA 2. Enter a topic, audience, and length to get started.")

topic = st.text_input("Enter blog topic:", "Artificial Intelligence in Healthcare")
audience = st.selectbox("Choose target audience:", ["Common People", "Researchers", "Data Scientists"])
length = st.slider("Approximate word count:", 100, 800, 300)

if st.button("Generate Blog"):
    prompt = f'''Write a detailed blog post of around {length} words on the topic "{topic}" for {audience}. Make it informative, structured, and engaging.'''
    with st.spinner("Generating your blog..."):
        output = model(prompt)
        st.subheader("📝 Generated Blog")
        st.write(output)
        st.download_button("📥 Download Blog as TXT", output, file_name="blog.txt")
