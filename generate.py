from transformers import pipeline

# Load the model
generator = pipeline("text-generation", model="distilgpt2")

# Generate text
prompt = "The future of artificial intelligence is"
outputs = generator(prompt, max_length=50, num_return_sequences=1)

# Show output
print("\nGenerated text:\n")
print(outputs[0]['generated_text'])
