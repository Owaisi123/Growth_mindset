import streamlit as st
import random
from PIL import Image

st.set_page_config(page_title="Growth Mindset Challenge", layout="centered")

st.title("🌱 Growth Mindset Challenge")
st.markdown("### Believe in Your Power to Grow!")

quotes = [
    "💬 Mistakes are proof that you are trying.",
    "💬 Challenges make you stronger.",
    "💬 Success comes from effort, not talent.",
    "💬 Believe in your ability to grow!",
    "💬 Every step forward counts, no matter how small."
]
random_quote = random.choice(quotes)
st.info(random_quote)

try:
    col1, col2, col3 = st.columns([1, 2, 1])  
    with col2: 
        img = Image.open("assests/growth.png")  
        st.image(img, caption="Keep Growing Every Day!", use_container_width=True)
except FileNotFoundError:
    st.error("⚠️ Image not found. Please make sure 'growth.png' is in the same folder.")

with st.expander("📘 What is a Growth Mindset?"):
    st.write("""
    A **growth mindset** means believing that you can improve with effort.
    You can learn anything if you keep trying and don’t give up!
    """)

with st.expander("💡 Why Adopt It?"):
    st.write("""
    - **Try New Things**: Don’t be afraid to take on challenges  
    - **Learn from Mistakes**: Mistakes help you grow  
    - **Keep Improving**: Practice makes progress  
    - **Celebrate Effort**: Trying matters more than talent  
    - **Stay Curious**: Explore, question, and learn more!
    """)

with st.expander("📈 How to Practice?"):
    st.write("""
    - Set learning goals  
    - Reflect on your progress regularly  
    - Be open to feedback  
    - Stay positive and help others grow too
    """)

st.subheader("📝 Pledge to Adopt a Growth Mindset")
name = st.text_input("Enter your name:")
if st.button("Pledge Now"):
    if name.strip():  
        st.success(f"🌟 Thank you, {name}! You're on the path of growth!")
    else:
        st.warning("⚠️ Please enter your name to continue.")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit by Owais")
