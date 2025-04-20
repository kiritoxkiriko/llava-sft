from datasets import load_dataset

# Load the dataset from Hugging Face Hub or local directory
dataset = load_dataset('./dataset/theblackcat102/llava-instruct-mix', split='train')

# Define the output JSON file path
output_file = 'dataset/llava-instruct-mix.json'

# Save the dataset to a JSON file
dataset.to_json(output_file, orient='records', force_ascii=False)

print(f"Dataset saved to {output_file}")