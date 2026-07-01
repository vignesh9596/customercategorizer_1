from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import uvicorn

app = FastAPI()

# Static files (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def read_form(request: Request):
    print("👉 GET / called")
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "context": None}
    )


@app.post("/", response_class=HTMLResponse)
def predict(
    request: Request,

    Age: int = Form(...),
    Education: int = Form(...),
    Marital_Status: int = Form(...),
    Parental_Status: int = Form(...),
    Children: int = Form(...),
    Income: float = Form(...),
    Total_Spending: float = Form(...),
    Days_as_Customer: int = Form(...),
    Recency: int = Form(...),

    Wines: float = Form(...),
    Fruits: float = Form(...),
    Meat: float = Form(...),
    Fish: float = Form(...),
    Sweets: float = Form(...),
    Gold: float = Form(...),

    Web: int = Form(...),
    Catalog: int = Form(...),
    Store: int = Form(...),
    Discount_Purchases: int = Form(...),
    Total_Promo: int = Form(...),
    NumWebVisitsMonth: int = Form(...)
):
    print("✅ POST / called")
    print("Age:", Age, "Income:", Income)

    # Dummy prediction
    cluster = 2

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "context": cluster}
    )


# 🔥 MAIN ENTRY POINT
if __name__ == "__main__":
    print("Starting FastAPI server...")
    print(" Open browser at: http://127.0.0.1:8000")
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
