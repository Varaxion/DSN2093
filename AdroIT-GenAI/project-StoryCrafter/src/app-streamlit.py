import streamlit as st
from transformers import pipeline, set_seed
import torch

# Set Streamlit page config
st.set_page_config(page_title="StoryCrafter", page_icon="📝")

# Use CPU or GPU if available
device = 0 if torch.cuda.is_available() else -1

# Load base GPT-2 for faster performance
generator = pipeline(
    "text-generation",
    model="gpt2",
    device=device
)
set_seed(42)

# UI
st.title("🌌 StoryCrafter")
st.markdown("Craft short stories by entering a character and setting below.")

# Inputs
character = st.text_input("Character Name")
setting = st.text_input("Setting or Scenario")
length = st.slider("Story Length (tokens)", min_value=50, max_value=200, value=100)

# Generate story
if st.button("Generate Story"):
    if not character.strip() or not setting.strip():
        st.warning("Please enter both a character and a setting.")
    else:
        prompt = f"A short story about {character}, who is {setting}."
        st.markdown("### 🧠 Generated Story")
        
        result = generator(
            prompt,
            max_length=length,
            num_return_sequences=1,
            do_sample=True,
            temperature=0.8,
            top_p=0.95
        )
        story = result[0]["generated_text"]
        st.write(story)
