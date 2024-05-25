# TalkWithDoc-Backend
# TalkWithDoc: Retrieval-Augmented Generation (RAG) Implementation with Large Language Models (LLMs)

## Overview
TalkWithDoc is a project aimed at enabling users to interact with web content through a conversational interface powered by Retrieval-Augmented Generation (RAG) and Large Language Models (LLMs). The project utilizes cutting-edge technologies to crawl data from web pages, convert it into vectorized format, and then employ a Mixtral 8x7b LLM model via Groq API to generate responses to user queries.

## Features
- Web scraping: Extracts relevant text data from user-provided web links.
- Data preprocessing: Stores crawled data in a text file for vectorization.
- Vectorization: Converts text data into vectorized format suitable for LLM input.
- LLM Integration: Utilizes the MixtR8 8x7b model via Groq API for response generation.
- Conversational interface: Allows users to interact with web content through a chatbot interface.

## Requirements
- Python 3.x
- Libraries: BeautifulSoup, requests, transformers, Groq API (credentials required)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/TalkWithDoc.git

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv env

