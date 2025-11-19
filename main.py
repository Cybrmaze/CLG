from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Static + templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# -------------------------------------------------------
# ROOT DASHBOARD (Control Panel)
# -------------------------------------------------------
@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

# -------------------------------------------------------
# LICENSING
# -------------------------------------------------------
@app.get("/licensing", response_class=HTMLResponse)
async def licensing(request: Request):
    return templates.TemplateResponse("licensing.html", {"request": request})

# -------------------------------------------------------
# POLICIES & PROCEDURES
# -------------------------------------------------------
@app.get("/policies", response_class=HTMLResponse)
async def policies(request: Request):
    return templates.TemplateResponse("policies.html", {"request": request})

# -------------------------------------------------------
# TRAINING
# -------------------------------------------------------
@app.get("/training", response_class=HTMLResponse)
async def training(request: Request):
    return templates.TemplateResponse("training.html", {"request": request})

# -------------------------------------------------------
# ACCREDITATION
# -------------------------------------------------------
@app.get("/accreditation", response_class=HTMLResponse)
async def accreditation(request: Request):
    return templates.TemplateResponse("accreditation.html", {"request": request})

# -------------------------------------------------------
# AGENT EDITOR
# -------------------------------------------------------
@app.get("/edit/{slot}", response_class=HTMLResponse)
async def edit_agent(request: Request, slot: str):
    return templates.TemplateResponse("edit_agent.html", {"request": request, "slot": slot})

# -------------------------------------------------------
# AVATAR UPDATE
# -------------------------------------------------------
@app.post("/update-avatar")
async def update_avatar(slot: str = Form(...), file: UploadFile = File(...)):
    avatar_path = f"static/avatars/{slot}.png"
    contents = await file.read()
    with open(avatar_path, "wb") as f:
        f.write(contents)
    return {"status": "ok", "saved": avatar_path}

