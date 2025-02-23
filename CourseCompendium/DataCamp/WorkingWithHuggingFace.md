1. **Hugging Face platform**: a central hub for open-source machine learning models and datasets for text, vision, and audio tasks. This platform simplifies the process of exploring, sharing, and experimenting with machine learning tools, significantly lowering the barriers to entry for research and development. Key points covered include:

2. **Hugging Face Hub** is a repository for models and datasets that supports a wide range of ML tasks across domains and languages. It makes it easier to experiment with various models and processors.
3. **Large Language Models (LLMs)**: You discovered that LLMs, like GPT from OpenAI and Llama from Meta, can understand and generate human-like text by learning patterns in data. The core component that enables this is the transformer architecture, which allows these models to understand the context within word sequences.
4. **Use Cases for Hugging Face:** This tool is Ideal for projects requiring quick implementation of ML tasks, teams with basic Python knowledge but limited ML expertise, testing multiple models, or when a project needs a dataset. However, it might not be suitable for highly customized architectures, domain-specific needs not covered by existing models, or when computational resources are limited.


- Getting Started: To use Hugging Face, you need to install the transformers and datasets libraries along with a machine learning framework like PyTorch. This setup enables interaction with the vast array of models and datasets available on the Hugging Face Hub for various ML tasks.
```
# Example code snippet for installing Hugging Face libraries
!pip install transformers datasets
# Followed by the installation of a machine learning framework, e.g., PyTorch
```
5. Searching the Hub with Python
```
# Create the instance of the API
api = HfApi()

# Return the filtered list from the Hub
models = api.list_models(
    filter=ModelFilter(task="text-classification"),
    sort="downloads",
    direction=-1,
  	limit=1
)

# Store as a list
modelList = list(models)

print(modelList[0].modelId)
```
6. Saving a model
```
modelId = "distilbert-base-uncased-finetuned-sst-2-english"

# Instantiate the AutoModel class
model = AutoModel.from_pretrained(modelId)

# Save the model
model.save_pretrained(save_directory=f"models/{modelId}")
```
7. Inspecting datasets

```
# Load the module
from datasets import load_dataset_builder

# Create the dataset builder
dataset_builder = load_dataset_builder("wikidata_extract")

# Extract the features
dataset_info = dataset_builder.info.features
```
8. Loading datasets
```
# Load the train portion of the dataset
wikipedia = load_dataset("wikimedia/wikipedia", language="20231101.en", split="train")

print(f"The length of the dataset is {len(wikipedia)}")
```
9. Manipulating datasets
```
# Filter the documents
filtered = wikipedia.filter(lambda row: "football" in row["text"])

# Create a sample dataset
example = filtered.select(range(1))

print(example[0]["text"])
```
10. Getting started with pipelines
```
# Import pipeline
from transformers import pipeline

# Create the task pipeline
task_pipeline = pipeline("sentiment-analysis")

# Create the model pipeline
model_pipeline = pipeline(model="distilbert-base-uncased-finetuned-sst-2-english")

# Predict the sentiment
task_output = task_pipeline(input)
model_output = model_pipeline(input)

print(f"Sentiment from task_pipeline: {task_output[0]['label']}; Sentiment from model_pipeline: {model_output[0]['label']}")
```
11. Using AutoClasses
```
# Download the model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

# Create the pipeline
sentimentAnalysis = pipeline(task="sentiment-analysis", model=model, tokenizer=tokenizer)

# Predict the sentiment
output = sentimentAnalysis(input)

print(f"Sentiment using AutoClasses: {output[0]['label']}")
```
12. Comparing models with the pipeline
```
# Create the pipeline
distil_pipeline = pipeline(task="sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Predict the sentiment
distil_output = distil_pipeline(input_text)

# Create the second pipeline and predict the sentiment
bert_pipeline = pipeline(task="sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
bert_output = bert_pipeline(input_text)

print(f"Bert Output: {bert_output[0]['label']}")
print(f"Distil Output: {distil_output[0]['label']}")
```
13. Normalizing text
```
# Import the AutoTokenizer
from transformers import AutoTokenizer

# Download the tokenizer
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

# Normalize the input string
output = tokenizer.backend_tokenizer.normalizer.normalize_str(input_string)

print(output)
```
14. Comparing tokenizer output
```
# Download the gpt tokenizer
gpt_tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Tokenize the input
gpt_tokens = gpt_tokenizer.tokenize(input)

# Repeat for distilbert
distil_tokenizer = DistilBertTokenizer.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english"
)
distil_tokens = distil_tokenizer.tokenize(text=input)

# Compare the output
print(f"GPT tokenizer: {gpt_tokens}")
print(f"DistilBERT tokenizer: {distil_tokens}")
```
15. Grammatical correctness
> Text classification is the process of labeling an input text into a pre-defined category. This can take the form of sentiment - positive or negative - spam detection - spam or not spam - and even grammatical errors.

```
# Create a pipeline
classifier = pipeline(
  task="text-classification", 
  model="abdulmatinomotoso/English_Grammar_Checker"
)

# Predict classification
output = classifier("I will walk dog")

print(output)
```
16. Question Natural Language Inference
```
# Create the pipeline
classifier = pipeline(task="text-classification", model="cross-encoder/qnli-electra-base")

# Predict the output
output = classifier("Where is the capital of France?, Brittany is known for their kouign-amann.")

print(output)
```
17. Zero-shot classification
```
# Build the zero-shot classifier
classifier = pipeline(task="zero-shot-classification", model="facebook/bart-large-mnli")

# Create the list
candidate_labels = ["politics", "science", "sports"]

# Predict the output
output = classifier(text, candidate_labels)

print(f"Top Label: {output['labels'][0]} with score: {output['scores'][0]}")
```
18. Summarizing long text
```
# Create the summarization pipeline
summarizer = pipeline(task="summarization", model="cnicu/t5-small-booksum")

# Summarize the text
summary_text = summarizer(original_text)

# Compare the length
print(f"Original text length: {len(original_text)}")
print(f"Summary length: {len(summary_text[0]['summary_text'])}")
```
19. Using min_length and max_length
```
# Create a short summarizer
short_summarizer = pipeline(task="summarization", model="cnicu/t5-small-booksum", min_length=1, max_length=10)

# Summarize the input text
short_summary_text = short_summarizer(original_text)

# Print the short summary
print(short_summary_text[0]["summary_text"])
```


```
# Create a short summarizer
short_summarizer = pipeline(task="summarization", model="cnicu/t5-small-booksum", min_length=1, max_length=10)

# Summarize the input text
short_summary_text = short_summarizer(original_text)

# Print the short summary
print(short_summary_text[0]["summary_text"])

# Repeat for a long summarizer
long_summarizer = pipeline(task="summarization", model="cnicu/t5-small-booksum", min_length=50, max_length=150)

long_summary_text = long_summarizer(original_text)

# Print the long summary
print(long_summary_text[0]["summary_text"])
```


20. Summarizing several inputs
```
# Create the list
text_to_summarize = [w["text"] for w in wiki]

# Create the pipeline
summarizer = pipeline("summarization", model="cnicu/t5-small-booksum", min_length=20, max_length =50)

# Summarize each item in the list
summaries = summarizer(text_to_summarize[:3], truncation=True)

# Create for-loop to print each summary
for i in range(0,3):
  print(f"Summary {i+1}: {summaries[i]['summary_text']}")
```
