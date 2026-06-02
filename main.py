from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Supaya dompet kripto (Phantom, dll) bisa baca API ini dari browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# Struktur data dasar untuk Solana Blink
class ActionResponse(BaseModel):
    icon: str
    title: str
    description: str
    label: str

@app.get("/api/actions/buy-coffee")
def get_action_metadata():
    return ActionResponse(
        icon="https://img.freepik.com/free-vector/coffee-cup-pixel-art-style_24877-83216.jpg",
        title="Beli Kopi Digital",
        description="Dukung proyek GitHub pertamaku dengan mengirimkan 0.1 SOL.",
        label="Kirim 0.1 SOL"
    )

@app.get("/")
def home():
    return {"status": "API Blink Solana Jalan!"}