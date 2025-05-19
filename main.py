from fastapi import FastAPI

from routers import product_router, inventory_router, sales_router, category_router

app = FastAPI()

app.include_router(product_router)
app.include_router(inventory_router)
app.include_router(sales_router)
app.include_router(category_router)