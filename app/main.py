# from fastapi import FastAPI
# from app.routes.student_routes import router as student_router
#
# app = FastAPI(title="Student Management System")
#
# app.include_router(student_router, tags=["Students"])

from fastapi import FastAPI
from app.routes import student_routes

app = FastAPI()

# Root endpoint for testing
@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Management System"}

# Include the student routes
app.include_router(student_routes.router)
