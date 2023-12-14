
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import LLMChain
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

from dotenv import load_dotenv

load_dotenv()

DATA_PATH = 'data/'
DB_FAISS_PATH = 'vectorstore/db_faiss'

embeddings = HuggingFaceEmbeddings(
    model_name='sentence-transformers/all-MiniLM-L6-v2',
    model_kwargs={'device': 'cpu'} 
    )

# Create vector database
def create_vector_db()->FAISS:
    """
    This function uses FAISS to create a vector store 
    which is saved locally for easy access
    """
    loader = DirectoryLoader(
        DATA_PATH,
        glob='*.pdf',
        loader_cls=PyPDFLoader
        )
    documents = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=300
        )
    texts = text_splitter.split_documents(documents)
    
    embeddings = HuggingFaceEmbeddings(
        model_name='sentence-transformers/all-MiniLM-L6-v2',
        model_kwargs={'device': 'cpu'}
        )
    db = FAISS.from_documents(texts, embeddings)
    
    db.save_local(DB_FAISS_PATH)
    
    return db


def get_reponse_from_query(query):
    """
    uses Faiss to do a similarity search 
    of the query in the vector store(db)
    then uses the llm to generate the 
    appropriate response
    """
    
    db = create_vector_db()
    
    
    docs = db.similarity_search(query)
    llm = HuggingFaceHub(
        repo_id="HuggingFaceH4/zephyr-7b-beta",
        model_kwargs={"max_length": 512}
        )
    prompt = PromptTemplate(
        input_variables=['question', 'docs'],
        template="""
        You're a helpful Amazon Web Service assistant that can answer any 
        question regarding AWS solutions based on an AWS solutions Architect pdf
        
        Answer this question: {question}
        By searching the following pdf: {docs}
        
        Only use factual information from the pdf and aws to answer the question.
        
        If you don't feel like you have enough information to answer the question
        say "Oops🤭! I don't know"
        
        All answers should be detailed and should respond to the questions
        do not suggest question just generate the answer.
        """          
    )    

    chain = LLMChain(llm=llm, prompt=prompt)
    
    response= chain.run(question=query, docs=docs)
    
    return response
