
export HF_ENDPOINT=https://huggingface.co
export HF_HUB_ENABLE_HF_TRANSFER=1

# download datasets
huggingface-cli download --repo-type dataset --resume-download  --local-dir dataset/HuggingFaceH4/llava-instruct-mix-vsft HuggingFaceH4/llava-instruct-mix-vsft


# download model
huggingface-cli download --repo-type dataset --resume-download  --local-dir model/HuggingFaceH4/llava-instruct-mix-vsft HuggingFaceH4/llava-instruct-mix-vsft

