# Web-App-for-Blog-Generation-using-LLAMA-2-Model
The project uses a pre-trained Llama 2 language model to create a web application for 'Dynamic Blog Generation', powered by Streamlit. It uses advanced natural language processing to generate relevant content for the blog, showcasing the potential of generative AI and NLP in content creation.

Short Introduction of the project

This project sets up a web application using Streamlit to facilitate dynamic blog generation utilizing a pre-trained Llama 2 language model. The application allows users to input a blog topic, specify the desired word count, and select the target audience from predefined options (Researchers, Data Scientists, Common People). The getLLamaresponse function is the core of the app, where it loads the Llama 2 model from a local path using AutoModelForCausalLM from the ctransformers library. It then constructs a prompt with the PromptTemplate class from langchain.prompts, generating the blog content based on user inputs. Upon submission, the app validates the inputs, formats the prompt, invokes the model to generate the text, truncates it to the specified word count, and displays the output. Error handling ensures any issues during the process are caught and communicated back to the user, providing a robust and interactive interface for generating contextually relevant blog content through advanced NLP techniques.

Detailed Understanding of the project

1) Imports and Setup

streamlit: A framework for creating web applications.
PromptTemplate: A utility from the langchain library for handling text prompts.
AutoModelForCausalLM: A utility from ctransformers for loading and working with causal language models.

2) Function Definition

Function getLLamaresponse: This function generates a blog using the Llama 2 model.
Loading the Model:
AutoModelForCausalLM.from_pretrained loads the model from the specified path of local machine with the type 'llama'.

3) Prompt Template:

A template string is defined for generating the prompt.
PromptTemplate is used to create a prompt object.
prompt.format formats the template with provided values (blog_style, input_text, and no_words).
Generating the Response:
model(formatted_prompt) generates the text from the model.
The response is processed to ensure it matches the word count (no_words).
The response is returned as a string.
Error Handling: If any error occurs, it returns the error message as a string.


4) Streamlit Interface
Page Configuration: Sets up the page title, icon, layout, and sidebar state for the Streamlit app.
Header: Adds a header to the page

5) Input Fields

Blog Topic: A text input field for entering the blog topic.
Columns: Two columns are created to organize the additional input fields.
Number of Words: A text input field for specifying the number of words.
Blog Style: A dropdown menu for selecting the target audience of the blog


6) Submit Button and Response Handling

Submit Button: A button to trigger the blog generation.
Response Handling:
Checks if the submit button is pressed.
Validates the input fields.
Calls getLLamaresponse with the inputs if they are valid and displays the generated blog.
Displays an error message if inputs are invalid.
This code sets up a Streamlit web application that allows users to input a blog topic, specify the number of words, select the target audience, and then generate a blog using the Llama 2 model.



