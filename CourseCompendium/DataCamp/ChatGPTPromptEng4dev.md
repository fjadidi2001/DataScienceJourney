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

The OpenAI package and the get_response() function have been pre-loaded for you.

The get_response() function in this exercise employs the max_tokens parameter to help this exercise run faster.
