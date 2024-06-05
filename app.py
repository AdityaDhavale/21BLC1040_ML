import streamlit as st  
from langchain.prompts import PromptTemplate
from ctransformers import AutoModelForCausalLM

# Function to get response from Llama 2 model
def getLLamaresponse(input_text, no_words, blog_style):
    try:
        # Loading the Llama 2 model from local machine 
        model = AutoModelForCausalLM.from_pretrained(
           "D:\models\llama-2-7b-chat.ggmlv3.q8_0.bin",
            model_type='llama'
        )
        
        # Prompt Template
        template = """Write a blog for {blog_style} job profile for the topic {input_text} within {no_words} words."""
        
        prompt = PromptTemplate(input_variables=["blog_style", "input_text", "no_words"], template=template)
        formatted_prompt = prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words)

        # Generating the response from Llama 2 model
        raw_response = model(formatted_prompt)  # Generating text using the model
        generated_text = "".join(raw_response)  # Converting generator object to string
        response_words = generated_text.split()[:no_words]  # Truncating to the specified number of words
        response = ' '.join(response_words)
        return response
    except Exception as e:
        return str(e)

st.set_page_config(page_title="Generate Blogs", page_icon="", layout="centered", initial_sidebar_state="collapsed")
st.header("Generate Blogs!")

input_text = st.text_input("Enter your Blog topic")

# Creating columns for additional fields
col1, col2 = st.columns([5, 5])
with col1:
    no_words = st.text_input("Number of words")
with col2:
    blog_style = st.selectbox("Writing the blog for", ('Researchers', 'Data Scientists', 'Common People'), index=0)

submit = st.button("Generate Blog")

# Final Response
if submit:
    if input_text and no_words.isdigit():
        no_words = int(no_words)  # Ensuring no_words is an integer
        st.write(getLLamaresponse(input_text, no_words, blog_style))
    else:
        st.error("Please enter valid input for blog topic and number of words.")
