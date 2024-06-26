from transformers import BartForConditionalGeneration, BartTokenizer
from typing import Optional

# Paths to local directories containing the pre-trained models and tokenizers
model_path = "local_models/spider_model"  # Ensure this path matches your directory structure
model_path_ddl = "local_models/trained_bart_model"  # Ensure this path matches your directory structure

# Function to load a model and its tokenizer
def load_model_and_tokenizer(model_dir: str) -> Optional[tuple]:
    try:
        model = BartForConditionalGeneration.from_pretrained(model_dir)
        tokenizer = BartTokenizer.from_pretrained(model_dir)
        return model, tokenizer
    except Exception as e:
        print(f"Failed to load model and tokenizer from {model_dir}: {e}")
        return None

# Load the models and tokenizers
model, tokenizer = load_model_and_tokenizer(model_path)
model_ddl, tokenizer_ddl = load_model_and_tokenizer(model_path_ddl)

def generate_sql(prompt: str) -> str:
    inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
    output_sequences = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=512,
        num_beams=5,
        early_stopping=True
    )
    sql_command = tokenizer.decode(output_sequences[0], skip_special_tokens=True)
    return sql_command

def generate_sql_ddl(prompt: str) -> str:
    inputs = tokenizer_ddl(prompt, return_tensors="pt", max_length=512, truncation=True)
    output_sequences = model_ddl.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=512,
        num_beams=5,
        early_stopping=True
    )
    sql_command_ddl = tokenizer_ddl.decode(output_sequences[0], skip_special_tokens=True)
    return sql_command_ddl
