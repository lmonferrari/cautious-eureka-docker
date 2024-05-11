import io
import uvicorn
from modelo import model_pipeline
from PIL import Image
from fastapi import FastAPI, UploadFile, File, Form

app = FastAPI()


@app.get("/")
def index():
    return {"API": "Reconhecimento de texto em imagem."}


@app.post("/api/v1/")
async def api_v1(text: str = Form(...), image: UploadFile = File(...)):
    image_contents = await image.read()
    image = Image.open(io.BytesIO(image_contents))
    predict = model_pipeline(text, image)
    return {"predict": predict}


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
