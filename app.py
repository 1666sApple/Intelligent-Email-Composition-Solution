import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

# Get Response from LLM
def llmresponse(form_input, sender, recipient, style):
    """
    Generate an email response using the provided input.

    Args:
        form_input (str): The topic of the email.
        sender (str): The name of the email sender.
        recipient (str): The name of the email recipient.
        style (str): The writing style of the email ("formal", "informal", "Satisfied", "Unsatisfied").

    Returns:
        str: The generated email response.
    """
    llm = CTransformers("llm/llama-2-7b-chat.ggmlv3.q8_0.bin", 
                        model_type="llama",
                        config={
                            "max_new_tokens": 256,
                            "temperature": 0.0
                        })
    
    template = """
    Write an email with {style} style to {recipient} from {sender} and 
    remember to include topic: {topic}.

    Senders name is {sender} and 
    Recipients name is {recipient}.

    Email text:
    """

    prompt = PromptTemplate(
        template=template, 
        input_variables=["style", "recipient", "sender", "topic"]
    )

    full_prompt = prompt.format(style=style, recipient=recipient, sender=sender, topic=form_input)
    response = llm(full_prompt)

    return response

# Set the page configuration
st.set_page_config(
    page_title="Email Generator",
    page_icon="📧",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Display the header
st.header("Email Generator")

# Get the email topic from the user
form_input = st.text_area("Enter the topic of the E-mail:", height=150)

# Create three columns for input fields
col1, col2, col3, col4, col5 = st.columns(5, gap="medium")

# Get the sender's name
with col1:
    sender = st.text_input("Name of the sender:")
    
# Get the sender's Email
with col2:
    sender_email = st.text_input("Email of the sender:")

# Get the recipient's name    
with col3:
    recipient = st.text_input("Name of the recipient:")
    
# Get the recipient's Email
with col4:
    recipients_email = st.text_input("Email of the recipient:")

# Get the writing style
with col5:
    style = st.selectbox("writing in", 
                               ("formal", "informal", "Satisfied", "Unsatisfied"),
                               index=0)
    
    # Create the "Generate Email" button
    submit = st.button("Generate Email")
    
    # Handle the button click
    if submit:
        # Check if sender and recipient names are provided
        if sender == "" or recipient == "":
            st.error("Please enter the sender and recipient's name")
        else:
            # Display a message while generating the email
            st.write("Generating Email...")
            
            # Generate the email response
            generated_email = llmresponse(form_input, sender, recipient, style)
            
            # Display the generated email
            st.write(generated_email)
