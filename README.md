# Smart-Assistant-Chatbot

This project leverages LangChain, Streamlit, and HuggingFace's state-of-the-art language models to create an intelligent assistant that helps users plan birthday parties. The assistant recommends venues, caterers, and entertainment options based on user inputs. It is powered by a custom prompt and retrieves data from a CSV file to provide relevant suggestions and confirm bookings.

# Project Structure

## Dataset:
The dataset used for this project was synthetically generated using GPT-4 (free version). It contains 1,000 rows and 5 columns:
venue.caterers,entertainment,date,time.The dataset is stored in CSV format and is used to provide real-time recommendations for birthday party planning. The assistant retrieves information from this dataset to help users book services based on their queries.The dataset is available as `Party.csv`.

## Model:
The core model is the pre-trained Mistral Mixtral-8x7B-Instruct-v0.1 available on HuggingFace Hub. The assistant operates with a custom prompt, ensuring that it only provides information available from the CSV and avoids hallucinating data. The prompt also guides the assistant to help with service recommendations, booking confirmations, and offering alternative dates when necessary.

## User Interaction with Streamlit:
The front-end interface is built using Streamlit, providing a clean, user-friendly chat interface. Users can enter their queries, such as asking for available venues, caterers, or entertainment options, and receive real-time responses. The chat history is maintained throughout the session to ensure a smooth conversation flow.

## Model Deployment: 
The conversational model is built using LangChain's `ConversationalRetrievalChain`,combining language model generation with FAISS-based data retrieval. This ensures that the user receives relevant and accurate responses to their queries, enhancing the overall experience.


# Working Principal of Chatbot

The project operates as an intelligent assistant that interacts with users through a chat interface built using Streamlit. Its core functionality is to help users plan birthday parties by recommending and booking venues, caterers, and entertainment options. The system uses a ConversationalRetrievalChain from LangChain, combining language generation with data retrieval from a pre-embedded CSV file containing relevant service details.The steps by step approach is given below: 
 ### 1.Data Handling:
      The dataset (Party.csv) containing information on venues, caterers, and entertainment options is loaded and embedded using HuggingFaceEmbeddings for efficient retrieval.
      The embedded data is stored in FAISS, allowing fast searches based on user queries.

 ### 2.Language Model Integration:
        The project uses a pre-trained Mistral Mixtral-8x7B-Instruct-v0.1 model from HuggingFace, loaded through the HuggingFaceHub API.
        The assistant is guided by a custom prompt, ensuring that responses are directly based on the available data and that it avoids generating unsupported or fictional information.

 ### 3.Conversational Chain:
        A ConversationalRetrievalChain is set up to integrate the language model with the vectorized data. When a user submits a query, the assistant retrieves relevant information from the CSV and responds accordingly.
        The conversation flow is managed in Streamlit, with session history maintained to ensure a coherent dialogue.

 ### 4.User Interaction:
        Users can enter queries into a chat interface, such as asking for available venues or confirming bookings.
        The assistant follows up with relevant recommendations, provides booking confirmations, and offers alternative dates when necessary.
