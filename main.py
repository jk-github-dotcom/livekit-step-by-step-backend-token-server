#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Choose kernel "Python (.venv_livekit_step_by_step)"

# python -m venv .venv_livekit_step_by_step
# .venv_livekit_step_by_step\scripts\activate


# In[2]:


#!pip install -r requirements.txt
#!pip install fastapi
#!pip install uvicorn
#!pip install livekit
#!pip install livekit-api
#!pip install python-dotenv

# pip install ipykernel
# python -m ipykernel install --user --name=.venv_livekit_step_by_step --display-name "Python (.venv_livekit_step_by_step)"
# pip freeze > .req_venv_livekit_step_by_step


# In[ ]:


# Documentation in README.md


# In[ ]:


# Run locally

# cd backend
# uvicorn livekit_token_server:app --reload --host 0.0.0.0 --port 8000

# You can now access http://localhost:8000/token?identity=alice&room=test-room


# In[ ]:


# CORS update

#app.add_middleware(
#    CORSMiddleware,
#    allow_origins=[
#        "http://localhost:5173",                      # Vite local dev
#        "https://your-frontend.netlify.app",          # If you deploy on Netlify
#        "https://your-frontend.vercel.app",           # If you use Vercel
#    ],
#    allow_credentials=True,
#    allow_methods=["*"],
#    allow_headers=["*"],
#)

# If you leave it as "*" during development, it's fine — but in production you should limit it to your actual domain.

# Best practice: Define a .env variable ALLOWED_ORIGINS and set for development and production.


# In[13]:


import os
from dotenv import load_dotenv

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from livekit import api

load_dotenv()
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",")

app = FastAPI()

# Allow requests from Vite dev server or Netlify
app.add_middleware(
    CORSMiddleware,
#    allow_origins=["*"],  # In production, restrict this to your frontend URL
    allow_origins=ALLOWED_ORIGINS, # In production, restrict this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/token")
async def get_token(identity: str, room: str):
    token = api.AccessToken(os.getenv("LIVEKIT_API_KEY"), os.getenv("LIVEKIT_SECRET")) \
        .with_identity(identity) \
        .with_grants(api.VideoGrants(
        room_join=True,
        room=room
        ))
    return {"token": token.to_jwt()}


# In[ ]:




