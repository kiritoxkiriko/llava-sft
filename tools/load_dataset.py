from datasets import load_dataset, Dataset
import os

# Load the dataset from local directory
dataset = load_dataset('./dataset/chess_pieces_sharegpt', split='all')

print(f"Original dataset: {dataset}")
