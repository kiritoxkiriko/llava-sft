from datasets import load_dataset, Dataset
import os

# Load the dataset from local directory
dataset = load_dataset('./dataset/Trelis/chess_pieces', split='all')

print(f"Original dataset: {dataset}")

# Create output directory if it doesn't exist
os.makedirs("dataset/chess_pieces_sharegpt", exist_ok=True)
output_dir = 'dataset/chess_pieces_sharegpt/data/train.parquet'

# Convert to the requested format
converted_data = []

for item in dataset:
    # Each item has 'image' and 'caption'
    entry = {
        "image": item["image"],
        "conversations": [
            {
                "from": "human",
                "value": "<image>\nDescribe this image in detail."
            },
            {
                "from": "gpt",
                "value": item["caption"]
            }
        ],
        "system": "You are a chess expert. Describe chess pieces by their type, color, viewing angle, and arrangement. Be concise and accurate."
    }
    converted_data.append(entry)

# Create a new dataset
converted_dataset = Dataset.from_list(converted_data)

# Save as multi-part Parquet files
converted_dataset.to_parquet(
    output_dir,
    batch_size=1000,  # Controls number of examples per file
)

print(f"Dataset converted and saved to {output_dir}")
print(f"Total examples: {len(converted_dataset)}")