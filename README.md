# Chat with any PDF using the new ChatGPT API
### The fast and easy way to chat with any PDF, Talk to books, research papers, manuals, essays, legal contracts, whatever you have!

## Table of Content
  * [openai](#openai)
  * [LangChain](#langchain)
  * [PyPDF2](#PyPDF2)
  * [tiktoken](#tiktoken)
  * [Installation](#Installation)

## openai
The OpenAI API can be applied to virtually any task that involves understanding or generating natural language, code, or images. We offer a spectrum of models with different levels of power suitable for different tasks, as well as the ability to fine-tune your own custom models. These models can be used for everything from content generation to semantic search and classification.

## LangChain
LangChain is a framework for developing applications powered by language models. We believe that the most powerful and differentiated applications will not only call out to a language model via an API, but will also:

Be data-aware: connect a language model to other sources of data
Be agentic: allow a language model to interact with its environment

The LangChain framework is designed with the above principles in mind.

## PyPDF2
PyPDF2 is a free and open source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. PyPDF2 can retrieve text and metadata from PDFs as well.

## tiktoken
When you want to deal with long pieces of text, it is necessary to split up that text into chunks. As simple as this sounds, there is a lot of potential complexity here. Ideally, you want to keep the semantically related pieces of text together. What “semantically related” means could depend on the type of text. This notebook showcases several ways to do that.

At a high level, text splitters work as following:

Split the text up into small, semantically meaningful chunks (often sentences).

Start combining these small chunks into a larger chunk until you reach a certain size (as measured by some function).

Once you reach that size, make that chunk its own piece of text and then start creating a new chunk of text with some overlap (to keep context between chunks).

That means there two different axes along which you can customize your text splitter:

How the text is split

How the chunk size is measured

## Installation
First we need to create python environment with version higher than 3.8. and install the below libraries. 
<img src="Installation.png" alt="">
