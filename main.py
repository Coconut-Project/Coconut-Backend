from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.handlers import ENDPOINTS, fetch_data, new_instance_table
from database import get_db
from routers import auth, user
from contextlib import asynccontextmanager
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import uvicorn


# Actualiser la base de donnée avec les data d'écobalyse
def edit_db():
    db = next(get_db())
    for endpoint in ENDPOINTS:
        data = fetch_data(endpoint)
        for schema in data:
            new_instance_table(schema, db)
    db.close()


# Set up the scheduler
scheduler = BackgroundScheduler()
trigger = CronTrigger(hour=19, minute=17)  # trigger l'actualisation à une certaine heure
scheduler.add_job(edit_db, trigger)
scheduler.start()

app = FastAPI()


# Ensure the scheduler shuts down properly on application exit.
@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    scheduler.shutdown()


origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(user.router)
app.include_router(auth.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

#run server with : uvicorn main:app --host 0.0.0.0 --port 8000 --reload
