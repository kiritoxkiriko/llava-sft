
export HF_ENDPOINT=https://hf-mirror.com
export HF_HUB_ENABLE_HF_TRANSFER=1

# download datasets
#huggingface-cli download --repo-type dataset --resume-download  --local-dir dataset/HuggingFaceH4/llava-instruct-mix-vsft HuggingFaceH4/llava-instruct-mix-vsft
# use original sharegpt dataset
huggingface-cli download --repo-type dataset --resume-download  --local-dir dataset/theblackcat102/llava-instruct-mix theblackcat102/llava-instruct-mix

# download model
#huggingface-cli download --resume-download  --local-dir model/liuhaotian/llava-v1.6-vicuna-7b liuhaotian/llava-v1.6-vicuna-7b

# replace with hf model
huggingface-cli download --resume-download  --local-dir model/llava-hf/llava-1.5-7b-hf llava-hf/llava-1.5-7b-hf

