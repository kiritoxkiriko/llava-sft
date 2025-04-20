export NCCL_P2P_DISABLE=1
export NCCL_IB_DISABLE=1
#export HF_HOME="./dataset"
export HF_ENDPOINT=https://hf-mirror.com
export HF_HUB_ENABLE_HF_TRANSFER=1


llamafactory-cli train config/config.yaml