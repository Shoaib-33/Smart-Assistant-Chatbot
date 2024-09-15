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
