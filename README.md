# Python Token Server

## Requirements
Python 3.8+
fastapi, uvicorn, livekit, livekit-api

## .env_livekit_step_by_step

**create vitual environment and jupyter kernel**

cd C:\Users\Gebruiker\Documents\ai4m\laboratory
python -m venv .venv_livekit_step_by_step
.venv_livekit_step_by_step\scripts\activate
pip install ipykernel
python -m ipykernel install --user --name=.venv_livekit_step_by_step --display-name "Python (.venv_livekit_step_by_step)"

**requirements.txt**
fastapi
uvicorn
livekit
livekit-api
python-dotenv

**Install libraries**

cd livekit-step-by-step/backend-token-server
pip install -r requirements.txt
pip freeze > .req_venv_livekit_step_by_step

## Run locally:

cd livekit-step-by-step/backend-token-server
uvicorn livekit_token_server:app --reload --host 0.0.0.0 --port 8000

You can now access http://localhost:8000/token?identity=alice&room=test-room

## Documentation

[Python SDK for LiveKit](https://github.com/livekit/python-sdks)
[LiveKit API documentation](https://docs.livekit.io/reference/python/livekit/index.html#livekit)
[livekit.api.access_token](https://docs.livekit.io/reference/python/livekit/api/access_token.html)

## Git and github

git init
git remote add origin https://github.com/yourusername/livekit-step-by-step-backend-token-server.git
git add .
git commit -m "Initial commit: backend token server"
git push -u origin main


## Deployment

**CORS update**

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",                      # Vite local dev
        "https://your-frontend.netlify.app",          # If you deploy on Netlify
        "https://your-frontend.vercel.app",           # If you use Vercel
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

If you leave it as "*" during development, it's fine — but in production you should limit it to your actual domain.

