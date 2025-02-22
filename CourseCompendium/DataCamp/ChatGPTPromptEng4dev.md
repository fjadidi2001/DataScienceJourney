# Create the OpenAI client
```
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the conversation messages
conversation_messages = [
    {"role": "system", "content": "You are a helpful event management assistant."},
    {"role": "user", "content": "What are some good conversation starters at networking events?"},
    {"role": "assistant", "content": ""}
]

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=conversation_messages
)
print(response.choices[0].message.content)

```
# create a get_response() function that receives a prompt as input and returns the response as an output
```
def get_response(prompt):
  # Create a request to the chat completions endpoint
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}], 
    temperature = 0)
  return response.choices[0].message.content

# Test the function with your prompt
response = get_response("poem about ChatGPT.")
print(response)
```
# modify the prompt you used in the previous exercise
```
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt that follows the instructions
prompt = "write a poem in basic English that a child can understand."

# Get the response
response = get_response(prompt)

print(response)
```
> Clear and concise prompts enhance the model's output and ensure successful task completion. 


## summary from ch1

- Action Verbs: You discovered the importance of using specific action verbs like "write," "explain," and "describe" to direct the model's tasks clearly. Avoiding vague verbs ensures the model understands the expected action.

- Precise Instructions: Crafting prompts with detailed instructions about the context, output length, format, style, and audience leads to more accurate responses. For instance, specifying "describe the behavior and characteristics of Golden Retrievers" yields more focused results than a general prompt about dogs.

- Output Length: You learned to control the output length by specifying expectations directly in the prompt, such as requesting "two sentences" on a topic. This approach helps manage the model's output more effectively than using parameters like max_tokens, which might cut responses off.

- Prompts: The lesson introduced the use of delimiters (e.g., triple backticks) to structure prompts clearly, especially when including input data for tasks like text summarization. This technique helps the model identify and process the input correctly.

- Using f-strings: You practiced embedding variables into prompts using Python's f-strings, allowing for dynamic prompt creation. For example:

# Generating a table
```
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a prompt that generates the table
prompt = "generate a table of 10 books with science fiction subject contains column for Title, Author, Year"
# Get the response
response = get_response(prompt)
print(response)
```
# Customizing output format
```
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the instructions
instructions = "you will be provided with a text delimited by triple backticks. generate a sutable title for it. and also detrmine the language of it"

# Create the output format
output_format = """
                - Text: <text we want to title>
                - Language:<the determined language>
                - Title:<the generated title>
                """ 

# Create the final prompt
prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)
```
# Conditional prompts
```
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the instructions
instructions = " the language and the number of sentences of the given delimited text; then if the text contains more than one sentence, generate a suitable title for it, otherwise, write 'N/A' for the title"

# Create the output format
output_format = """
                - Text: <text we want to title>
                - Language:<the determined language>
                - Number of Sentences:<number of sentences>
                - Title:<the generated title>
                """ 

prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)
```
# Create a one-shot prompt
```
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a one-shot prompt
prompt = """A: set number one is {1, 3, 7, 12, 19} B: the odd numbers from this set is:  {1, 3, 7, 19}
A: set number two is {3, 5, 11, 12, 16} B:
"""

response = get_response(prompt)
print(response)
```
# Sentiment analysis with few-shot prompting
```
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
  model = "gpt-4o-mini",
  # Provide the examples as previous conversations
  messages = [{"role": "user", "content": "The product quality exceeded my expectations"},
              {"role": "assistant", "content": "1"},
              {"role": "user", "content": "I had a terrible experience with this product's customer service"},
              {"role": "assistant", "content": "-1"},
              # Provide the text for the model to classify
              {"role": "user", "content": "The price of the product is really fair given its features"}
             ],
  temperature = 0
)
print(response.choices[0].message.content)
```
# Single-step prompt to plan a trip
```
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a single-step prompt to get help planning the vacation
prompt = "plan a beach vacation."

response = get_response(prompt)
print(response)
```
# Multi-step prompt to plan a trip
```
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a prompt detailing steps to plan the trip
prompt = """Plan a trip for beach vacation:
            Step 0: four potential locations
            Step 1: accommodation options
            Step 2: activities
            Step 3: evaluation of the pros and cons.
"""

response = get_response(prompt)
print(response)

```

# Analyze solution correctness
```
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

code = """
def calculate_rectangle_area(length, width):
    area = length * width
    return area
"""

# Create a prompt that analyzes correctness of the code
prompt = f"""The code delimited by triple backticks, check these steps:
            Step 1: nalyze a function for correct syntax,
            Step 2: receiving two inputs,
            Step 3: returning one output
        ```{code}```"""
response = get_response(prompt)
print(response)
```
# Reasoning with chain-of-thought prompts
```
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the chain-of-thought prompt
prompt = """Q:determine my friend's father's age in 10 years, given that he is currently twice my friend's age, and my friend is 20.
A: Let's thinkin step-by-step
"""

response = get_response(prompt)
print(response)
```
# One-shot chain-of-thought prompts
```
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the example 
example = """Q: Sum the even numbers in the following set: {9, 10, 13, 4, 2}.
             A: Even numbers: {10,4,2}. Adding them: 10+4+2=16"""

# Define the question
question = """Q: Sum the even numbers in the following set: {15, 13, 82, 7, 14} 
              A:Even numbers:
              Adding them:
            """

# Create the final prompt
prompt = example + question
response = get_response(prompt)
print(response)
```
# Self-consistency prompts
> Imagine you own a store that sells laptops and mobile phones. You start your day with 50 devices in the store, out of which 60% are mobile phones. Throughout the day, three clients visited the store, each of them bought one mobile phone, and one of them bought additionally a laptop. Also, you added to your collection 10 laptops and 5 mobile phones. How many laptops and mobile phones do you have by the end of the day? This problem is defined in the problem_to_solve string, and you will use a self-consistency prompt to solve it.
```
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the self_consistency instruction
self_consistency_instruction = " solve the problem with three experts and combine the results with a majority vote."

# Create the problem to solve
problem_to_solve = "If you own a store that sells laptops and mobile phones. You start your day with 50 devices in the store, out of which 60% are mobile phones. Throughout the day, three clients visited the store, each of them bought one mobile phone, and one of them bought additionally a laptop. Also, you added to your collection 10 laptops and 5 mobile phones. How many laptops and mobile phones do you have by the end of the day?"

# Create the final prompt
prompt = self_consistency_instruction + problem_to_solve

response = get_response(prompt)
print(response)
```

# Iterative prompt engineering

![image](https://github.com/user-attachments/assets/9212641f-d702-4a0e-97ac-1d7c7722391c)


### Basic Iterative prompt engineering
```
client = OpenAI(api_key="<OPENAI_API_TOKEN>")
# Refine the following prompt
prompt = """Give me a table with three columns for the top 10 pre-trained language models
the columns name should be model name, release year, and owning company.
"""
response = get_response(prompt)
print(response)
```

### Iterative prompt engineering for few-shot prompts
```
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Refine the following prompt
prompt = """
Receiving a promotion at work made me feel on top of the world -> Happiness
The movie's ending left me with a heavy feeling in my chest -> Sadness
Walking alone in the dark alley sent shivers down my spine -> Fear
Time flies like an arrow -> No explicit emotion
They sat and ate their meal ->
"""

response = get_response(prompt)
print(response)
```

# Market research report summarization


```
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to summarize the report
prompt = f"""Summarizes the report in maximum five sentences while related to AI and data privacy
```{report}```
"""

response = get_response(prompt)

print("Summarized report: \n", response)
```


# Product features summarization
```
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to summarize the product description
prompt = f""" summarizes the product_description in no more than five bullet points  ```{product_description}```"""

response = get_response(prompt)

print("Original description: \n", product_description)
print("Summarized description: \n", response)
```


## transform concise product descriptions into engaging and detailed narratives for the e-commerce platform
```
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to expand the product's description
prompt = f"""expands the product_description pre-loaded string, and writes a one paragraph comprehensive overview capturing the key information of the product: unique features, benefits, and potential applications.

```{product_description}
"""

response = get_response(prompt)

print("Original description: \n", product_description)
print("Expanded description: \n", response)
```
## Translation for multilingual communication
```
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt that translates
prompt = f""" translates the marketing_message from English to French, Spanish, and Japanese```{marketing_message}"""
 
response = get_response(prompt)

print("English:", marketing_message)
print(response)
```
## Tone adjustment for email marketing
```
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to change the email's tone
prompt = f"""transforms the sample_email by changing its tone to be professional, positive, and user-centric ```{sample_email}```

"""

response = get_response(prompt)

print("Before transformation: \n", sample_email)
print("After transformation: \n", response)
```


## Writing improvement


```
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to transform the text
prompt = f"""step 1: proofreads the text without changing its structure
 step2: adjusts the text tone to be formal and friendly
 ```{text}```
"""

response = get_response(prompt)

print("Before transformation:\n", text)
print("After transformation:\n", response)
```

## Customer support ticket routing
```
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to classify the ticket
prompt = f"""classifies the ticket as technical issue, billing inquiry, or product feedback, without providing anything else in the response```{ticket}"""

response = get_response(prompt)

print("Ticket: ", ticket)
print("Class: ", response)
```

## Customer support ticket analysis

```
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a few-shot prompt to get the ticket's entities
prompt = f"""
ticket_1 = entities_1
ticket_2 = entities_2
ticket_3 = entities_3
ticket_4 = 
"""

response = get_response(prompt)

print("Ticket: \n", ticket_4)
print("Entities: \n", response)
```


## Code generation with problem description

```
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt that asks the model for the function
prompt = """
write a Python function that receives a list of 12 floats representing monthly sales data as input and, returns the month with the highest sales value as output.

"""

response = get_response(prompt)
print(response)
```


## Input-output examples for code generation

```
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

examples="""input = [10, 5, 8] -> output = 23
input = [5, 2, 4] -> output = 11
input = [2, 1, 3] -> output = 6
input = [8, 4, 6] -> output = 18
"""

# Craft a prompt that asks the model for the function
prompt = f""" infer the Python function that maps the inputs to the outputs in the provided examples ```{examples}```"""

response = get_response(prompt)
print(response)
```
