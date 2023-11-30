# CloudWhiz: [AWS Assistant Chatbot](https://cloudwhiz.streamlit.app/)

 CloudWhiz is a chatbot built with Streamlit, Langchain, Hugging Face's LLM, and Faiss. It serves as a helpful Amazon Web Service assistant, capable of answering questions regarding AWS solutions based on an AWS Solutions Architect PDF.

![preview](image/preview.png)

## Getting Started

### Prerequisites

Before you begin, make sure you have the following installed:

- Python (>=3.10)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)
- [Git](https://git-scm.com/)

### Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:aibunny/cloudwhiz.git
   ```
2. Navigate to the project directory:

   ```bash
   cd cloudwhiz
   ```
3. Create a virtual environment:

   ```bash
   virtualenv venv
   ```
4. Activate the virtual environment:

   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```
   - On Unix or MacOS:

     ```bash
     source venv/bin/activate
     ```
5. Create a `.env` file in the project root and add your Hugging Face API token:

   ```env
   HUGGINGFACEHUB_API_TOKEN=hf_your_token_here
   ```
6. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

After setting up the environment, you can run the CloudWhiz  using Streamlit. Execute the following command:

```bash
streamlit run helper.py
```
