# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, FAISS
#from langchain.vectorstores.faiss import FAISS
from langchain.chains.question_answering import load_qa_chain
#from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.llms import OpenAI
#import tiktoken
import os
import gradio as gr

#openai API key
os.environ["OPENAI_API_KEY"] = "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"

# location of the pdf file/files.
reader = PdfReader('Data/Automation A360-1 to 100 pages.pdf')

# read data from the file and put them into a variable called raw_text
raw_text = ''
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        raw_text += text

#print(raw_text[:100])

# We need to split the text that we read into smaller chunks so that during information retreival we don't hit the token size limits.
text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 1000,
    chunk_overlap  = 200,
    length_function = len,
)
texts = text_splitter.split_text(raw_text)

# Download embeddings from OpenAI
embeddings = OpenAIEmbeddings()
docsearch = FAISS.from_texts(texts, embeddings)

chain = load_qa_chain(OpenAI(), chain_type="stuff")

#Testing, working code modified by Rahul on 30-04-2023.
query = "How do I upgrade to the latest version of Automation Anywhere?"
docs = docsearch.similarity_search(query)
chain.run(input_documents=docs, question=query)


# modified by Rahul on 30-04-2023 chatbot interface for user interaction.
def chatbot(input):
    if input:
        # messages.append({"role": "user", "content": input})
        # chat = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo", messages=messages
        # )

        # reply = chat.choices[0].message.content
        # messages.append({"role": "assistant", "content": reply})
        # return reply
        query = input
        docs = docsearch.similarity_search(query)
        return chain.run(input_documents=docs, question=query)


inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
print(inputs)
outputs = gr.outputs.Textbox(label="Reply")
print(outputs)
gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
             description="Ask anything you want",
             theme="compact").launch(share=True)


