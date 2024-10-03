from typing import List
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io

from func import extract_text_from_image, get_prix_exact


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Remplacez par votre domaine ou utilisez ["*"] pour autoriser tous
    allow_credentials=True,
    allow_methods=["*"],  # Autoriser toutes les méthodes (GET, POST, etc.)
    allow_headers=["*"],  # Autoriser tous les headers
)

@app.get("/")
def hello():
    return {"message": "Hello, World"}

# Modèle de données
@app.post("/upload-images/")
async def upload_images(files: List[UploadFile] = File(...)):
    results = []

    for index, file in enumerate(files):
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        mots = extract_text_from_image(image)
        prix = get_prix_exact(mots)
        
        results.append({
            "id": index + 1,
            "filename": file.filename,
            "prix": prix
        })

    return JSONResponse(content=results)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='10.0.105.140', port=5000)
