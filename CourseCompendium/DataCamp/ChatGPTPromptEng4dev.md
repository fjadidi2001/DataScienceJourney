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
