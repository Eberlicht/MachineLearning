import torch
from torchscale.architecture.config import RetNetConfig
from torchscale.architecture.retnet import RetNetDecoder
from transformers import BertTokenizer

config = RetNetConfig(vocab_size=64000, decoder_embed_dim=512)
retnet = RetNetDecoder(config)

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
token = tokenizer("test test test", return_tensors="pt", padding='max_length', truncation=True)

retnet(prev_output_tokens=token.input_ids, token_embeddings=token.input_ids)
