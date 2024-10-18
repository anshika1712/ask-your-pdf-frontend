# RAG System with Agent and Voice Response

## Overview

This project is a **Retrieval-Augmented Generation (RAG)** system designed as part of an assignment. It processes PDF files and uses a vector database to answer user queries based on the content of the PDFs. The system includes an intelligent agent that can perform specific actions based on user queries, including:

- **Wikipedia Search**
- **Arithmetic Calculation**
- **Summarization Tool**

The system provides responses in both text and speech formats. The backend is built using **FastAPI** and hosted on **Render**, while the frontend is created with **Streamlit** for easy user interaction.

## Features

- **RAG System**: Accepts PDF files, retrieves relevant information using a vector database, and returns a response to user queries.
- **Agent with Smart Decision-Making**: The agent decides when to access the vector database or trigger one of its built-in tools (Wikipedia search, arithmetic calculation, summarization).
- **Voice Response**: Using Sarvam's API, the system converts text responses into speech.
- **Multi-Tool Capabilities**: 
  - Wikipedia search for factual information.
  - Arithmetic calculation for numerical inputs.
  - Summarization tool for concise text generation.

## Agent Decision-Making Logic

The agent makes decisions based on the presence of specific keywords in the user's query:

- **Wikipedia Search**: If the query contains the keyword `"wiki"`, the agent routes the request to the Wikipedia search functionality.
- **Summarization Tool**: If the query contains the keyword `"summarize"`, the agent routes the request to the summarization tool.
- **Arithmetic Calculation**: If the query contains the keyword `"calculate"`, the agent routes the request to the arithmetic calculation tool.
- **Greeting and Generic Inputs**: For generic queries like "hello", "hi", or "how are you", the agent does not interact with the vector database or any tools and simply returns a greeting response.

For all other queries that do not fall into these categories, the agent invokes the **RAG system**, accessing the vector database to retrieve relevant information from the uploaded PDF files.

## Try it out
The backend code is in a private repository and this repository contains the frontend code. You can try out the hosted application here:
<https://ask-your-pdf-anshika.streamlit.app/>
