# ChatGPT Overview

## 1. What is ChatGPT?
ChatGPT, by OpenAI, is a chatbot application capable of answering questions and performing tasks based on user input. Unlike traditional chatbots that provide predetermined responses, ChatGPT leverages its understanding of language to interpret questions and generate appropriate responses, making it more versatile and applicable to a variety of tasks.

## 2. Generative AI
ChatGPT utilizes generative AI, a subset of artificial intelligence and machine learning, which allows it to create new content based on patterns in information it has processed.

## 3. From Prompt to Response
1. Users submit a question or instruction (prompt).
2. The application interprets this prompt using its language understanding.
3. A relevant response is generated and returned to the user.

## 4. Summarizing Text
ChatGPT excels at summarizing text and explaining concepts for specific audiences. This is particularly useful when communicating complex information. Users can instruct ChatGPT to provide concise summaries, and it can recall previous information from the conversation, allowing for follow-up corrections or refinements.

## 5. Creating Marketing Content
Beyond summarization, ChatGPT can generate creative content, such as marketing materials. For example, it can craft tweets that promote skills like data literacy, ensuring the output is engaging and adheres to platform constraints.

## 6. Generating and Debugging Code
Software engineers and data practitioners find value in ChatGPT’s ability to generate template code, troubleshoot issues, and offer suggestions for code improvement.

## 7. Why Utilize ChatGPT?
Implementing ChatGPT in workflows can enhance efficiency by automating time-consuming tasks, allowing human experts to finalize and verify AI-generated outputs. This synergy saves time and costs, enabling professionals to focus on complex decision-making and enhancing customer personalization in products.



# Limitations of ChatGPT

Although ChatGPT is a valuable tool that can perform a huge variety of tasks, there are some limitations to be aware of to use it effectively.

## ChatGPT Under the Hood

- ChatGPT's text-generation capabilities come from a large language model (LLM) that interprets prompts and generates relevant text based on its understanding of language.
- To understand some of the limitations of ChatGPT, we first need to delve deeper into how the LLM works.

## Demystifying the LLM

- Imagine we've been shown a large, complex building block wall and given an incomplete wall to finish in the same style. This analogy illustrates how ChatGPT functions.
- During development, the LLM was exposed to vast amounts of text data (the large building block wall), allowing it to understand the structure of language by analyzing the relationships between characters, words, and sentences (the differently colored building blocks).
- This learned data is referred to as *training data*, and its sheer volume and diversity contribute significantly to ChatGPT's success.
- The model utilized complex algorithms to detect language patterns in the training data and underwent fine-tuning through iterative processes, including rating the quality of the responses.
- When a prompt is provided to ChatGPT, it is effectively completing a building block wall by generating words based on the most likely continuation from its training data.

## Limitations of ChatGPT

1. **Knowledge Cutoff**  
   ChatGPT was trained on data up to a certain date, which varies depending on the model used. Without being directly provided with additional context, these models lack knowledge of events past these dates. As OpenAI updates the LLMs, these dates will continue to shift forward.
  
2. **Training Data Bias**  
   There is potential for bias in the training data. ChatGPT was trained on a large text dataset from various sources, including books, articles, and websites, which could contain biases. The model may learn these biases and produce biased responses.

3. **Context Tracking**  
   ChatGPT can build on information and context from earlier in the conversation, allowing for follow-up corrections. However, if the conversation topic shifts multiple times, ChatGPT may struggle to track context, leading to inaccurate or irrelevant responses. It's advisable to keep conversations focused on one topic and create new discussions for different topics.

4. **Hallucination**  
   Hallucination occurs when the model confidently provides inaccurate information, often when it goes beyond its knowledge cutoff or abilities. These inaccuracies can be challenging to identify without external validation. One of the active areas of LLM development is the identification and reduction of hallucinations.

5. **Legal and Ethical Considerations**  
   Consider a scenario where we ask ChatGPT to write a new song in the style of our favorite artist. The resulting song may resemble the artist's style based on the lyrics available in the training data. However, ownership of this new song becomes complicated. Is it owned by the user who wrote the prompt, the original artist, or OpenAI, the creators of ChatGPT? It's easy to navigate legal gray areas if the use cases for ChatGPT are not properly defined, which raises concerns about ownership and legal implications that will need to be addressed later in the course.



**ChatGPT has a knowledge cutoff**
