from transformers import ViltProcessor, ViltForQuestionAnswering
from PIL import Image

pre_trained_model = "dandelin/vilt-b32-finetuned-vqa"

processor = ViltProcessor.from_pretrained(pre_trained_model)
model = ViltForQuestionAnswering.from_pretrained(pre_trained_model)


def model_pipeline(text: str, image: Image):
    encoding = processor(image, text, return_tensors="pt")
    outputs = model(**encoding)
    logits = outputs.logits
    index = logits.argmax(-1).item()

    return model.config.id2label[index]
