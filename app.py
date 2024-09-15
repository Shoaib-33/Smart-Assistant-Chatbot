import streamlit as st 
from streamlit_chat import message
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import HuggingFaceHub
from langchain.chains import ConversationalRetrievalChain

DB_FAISS_PATH = 'vectorstore/db_faiss'

# Loading the model
def load_llm():
    repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"
    llm = HuggingFaceHub(
        repo_id=repo_id,
        model_kwargs={"temperature": 0.1, "top_k": 50},
        huggingfacehub_api_token="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"
    )
    return llm

# Define a concise custom prompt function
def custom_prompt(question):
    return f"""
    You are an assistant helping the user book venues, caterers, and entertainment for a birthday party.
    The user may ask you of any available venues,caterers,entertainment.You will suggest the user as per the information you obtained.
    Dont write any information of your own and dont make up anything of yourself.If the requirement of the user is available then mention that is available else say not available.
    Be format and helpful.Ask the user if he needs any other help.Recommend services quickly and confirm bookings when the user requests. Suggest alternative dates if needed.Say Thank you at the end. 
    User Query: {question}
    """

st.title("Smart Assistant")

st.markdown("""
    <h3 style='text-align: center; color: white;'>Instructions:</h3>
    <p style='text-align: center; color: white;'>1. Enter your query about the data in the text input box below.</p>
    <p style='text-align: center; color: white;'>2. The chat will respond with answers based on the data in the CSV file.</p>
    <p style='text-align: center; color: white;'>3. Feel free to ask questions about the data or clarify any details.</p>
""", unsafe_allow_html=True)

# Hardcoded file path for the CSV
csv_file_path = 'Party.csv'

if csv_file_path:
    loader = CSVLoader(file_path=csv_file_path, encoding="utf-8", csv_args={'delimiter': ','})
    data = loader.load()
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', model_kwargs={'device': 'cpu'})
    db = FAISS.from_documents(data, embeddings)
    db.save_local(DB_FAISS_PATH)
    llm = load_llm()

    # Create the chain with LLM and retriever
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=db.as_retriever()
    )

    # Function to handle the conversational chat with custom prompt handling
    def conversational_chat(query):
        # Check if the query is a casual greeting
        if query.lower() in ["hello", "hi", "hey"]:
            return "Hello! How can I assist you today? Are you planning a party and need help with venues, caterers, or entertainment?"

        # Check if the user confirmed a booking
        if "yes" in query.lower() and any(keyword in query.lower() for keyword in ["book", "confirm", "proceed"]):
            return "Booking successful. Is there anything else I can help with?"

        # Check if the user is thanking the assistant
        if any(thanks in query.lower() for thanks in ["thank you", "thanks", "cheers", "appreciate"]):
            return "You're welcome! Let me know if you need any further assistance."

        # Generate the custom prompt with instructions
        prompt = custom_prompt(query)
        result = chain({"question": prompt, "chat_history": st.session_state['history']})
        
        # Clean the response to only show the helpful answer (excluding "Question:")
        clean_response = result["answer"].strip()  # Strip any leading/trailing whitespace
        if "Helpful Answer:" in clean_response:
            clean_response = clean_response.split("Helpful Answer:")[-1].strip()  # Keep only the helpful answer
        if clean_response.startswith("User Query:"):
            clean_response = clean_response.split("User Query:")[-1].strip()
        
        st.session_state['history'].append((query, clean_response))
        return clean_response

    # Initialize session state for conversation history
    if 'history' not in st.session_state:
        st.session_state['history'] = []

    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["Hello! Ask me anything about Party Plan"]

    if 'past' not in st.session_state:
        st.session_state['past'] = ["Hey! 👋"]
        
    response_container = st.container()
    container = st.container()

    # User input form and chat logic
    with container:
        with st.form(key='my_form', clear_on_submit=True):
            user_input = st.text_input("Query:", placeholder="Talk to your csv data here (:", key='input')
            submit_button = st.form_submit_button(label='Send')
            
        if submit_button and user_input:
            output = conversational_chat(user_input)
            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)

    # Display conversation history with formal avatars
    if st.session_state['generated']:
        with response_container:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="adventurer-neutral")
                message(st.session_state["generated"][i], key=str(i), avatar_style="micah")
