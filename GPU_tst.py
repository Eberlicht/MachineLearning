"""
this loads a model into gpu-mem
"""


from transformers import pipeline

pipe = pipeline("text-generation", model="google/gemma-7b", device="cuda", token="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")

while True:
    text = input("give me some text bby: ")
    if text:
        model_output = pipe(text)
        print(model_output)
    elif text == "q":
        exit()







