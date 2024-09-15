# Smart-Assistant-Chatbot

This project leverages LangChain, Streamlit, and HuggingFace's state-of-the-art language models to create an intelligent assistant that helps users plan birthday parties. The assistant recommends venues, caterers, and entertainment options based on user inputs. It is powered by a custom prompt and retrieves data from a CSV file to provide relevant suggestions and confirm bookings.

# Technical Specifications

## Environment and Dependencies: 
The project utilizes several key technologies to create an interactive and efficient birthday party planning assistant. Streamlit is employed to develop the web interface, providing a user-friendly platform for interaction. LangChain is integrated to bridge conversational AI with data retrieval capabilities, enabling the assistant to fetch relevant information based on user queries. HuggingFace provides pre-trained language models and embeddings; specifically, HuggingFaceHub is used to load the language model, while HuggingFaceEmbeddings is utilized to encode the dataset. FAISS is used for managing and retrieving dense vector representations of the data, facilitating quick and accurate responses.

## Data Management: 
The dataset utilized in this project is a synthetically generated CSV file named Party.csv, which was created using GPT-4.0(Free version). This dataset contains 1,000 rows and five columns: venue, caterers, entertainment, date, and time. To integrate this data into the system, CSVLoader from LangChain is used to load the data, converting it into a format suitable for embedding and retrieval.

## Embedding: 
Textual data from the CSV file is converted into dense vector representations using HuggingFaceEmbeddings. The specific model used for this task is `sentence-transformers/all-MiniLM-L6-v2`. This model generates high-quality embeddings that capture semantic meanings of the text, which are crucial for performing efficient similarity searches. The embeddings are computed on the CPU, as indicated by the parameter model_kwargs={'device': 'cpu'}, ensuring compatibility and eliminating the need for a GPU.

## Model Loading:
The core language model is `Mistral Mixtral-8x7B-Instruct-v0.1`, loaded through the HuggingFaceHub API. This model is configured with parameters such as temperature set to 0.1, which controls the randomness of the generated responses, and top_k set to 50, limiting the number of candidate tokens considered for each step. An API token is required for authenticating with HuggingFace Hub, ensuring secure access to the model.

## Conversational Retrieval Chain:
The project employs a `ConversationalRetrievalChain` that combines the language model and the FAISS retriever. This setup integrates the language generation capabilities with the efficient data retrieval system provided by FAISS. The chain uses the language model (llm) to generate responses based on queries and the retriever to fetch relevant information from the embedded dataset.

## Custom Prompt Handling:
A custom prompt function is designed to format user queries in a way that guides the assistant's responses. The prompt ensures that the assistant only uses information available from the dataset, avoids generating unsupported information, and maintains a formal, helpful tone. It also includes instructions for booking confirmations and suggesting alternative dates if necessary.

## User Interaction and Chat Management:
The user interface is created using Streamlit, where users can input queries and receive responses. The chat interface includes a title and instructions to guide user interactions. The conversation history is maintained in `st.session_state`, which keeps track of both user inputs and assistant responses. The streamlit_chat library is used to display these interactions with distinct avatars for better user experience.

## Session State Management:
The project manages session state using Streamlit’s st.session_state to handle conversation history. This includes variables such as history for storing past interactions, generated for the assistant's responses, and past for tracking user queries. This state management ensures continuity and coherence in the dialogue.

## Deployment and Usage:
The project is designed to be run locally using Streamlit. Users can clone the repository, install the required dependencies, and launch the app to interact with the assistant. The deployment process involves setting up the environment, configuring the app, and running it to provide users with real-time party planning assistance.


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
WThe assistant follows up with relevant recommendations, provides booking confirmations, and offers alternative dates when necessary.


 # Technical Difficulties
 
The project presented several challenges primarily due to the use of a free model, which generally has limitations in handling contextual data effectively. One significant issue was the model's performance with the CSV dataset. Although the data was well-structured for retrieval, the free model struggled to deliver accurate and contextually relevant responses.

Another major challenge involved the development of the conversational bot. Unlike OpenAI models, which provide built-in history restoration features, the free model required manual management of conversational context. This led to difficulties in maintaining coherent interactions, with the model sometimes generating unusual or irrelevant data, and repeating context erroneously.

Handling custom prompts was also problematic. The free model occasionally included parts of the custom prompt in its responses, making it challenging to extract useful information. The lack of a clear method to isolate and strip out the relevant parts from the prompt text added to the complexity.

Frequent adjustments to the custom prompt were necessary to achieve acceptable results, which proved to be time-consuming. Additionally, the model exhibited occasional irrelevant behavior in responses, a problem that could potentially be addressed with more advanced paid models such as OpenAI's GPT-3.5 or higher.

Overall, while the free model provided a foundational capability, its limitations in context handling and response accuracy were significant hurdles. More advanced paid models would likely offer improved performance and more efficient handling of conversational nuances.

# Improvement Scope

However, there is substantial potential for improvement in this project. Utilizing advanced models such as GPT-3.5 or other paid alternatives could significantly enhance the model's ability to grasp context more effectively. Additionally, fine-tuning these models could further improve contextual accuracy, particularly when applied to a large dataset. Enhancing the dataset to be more comprehensive and well-structured would also contribute to better contextual understanding. Furthermore, considerable advancements can be made in the user interface and user experience (UI/UX) of the chatbot, which would improve overall user interaction and satisfaction.

