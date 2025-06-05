from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Set model name
model_name = "facebook/blenderbot-400M-distill"

# Load model (download on first run and reference local installation for consequent runs)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Initialize conversation history
conversation_history = []

while True:
    # Create conversation history string
    history_string = "\n".join(conversation_history)

    # Prompt
    input_text =input("> ")

    # Tokenize the input text and history
    inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")

    #tokenizer.pretrained_vocab_files_map

    # Get response from the model
    outputs = model.generate(**inputs)

    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    print(response)

    # Update conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)