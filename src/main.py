from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from api.v1.account import router as account_router
from api.v1.customer import router as customer_router
from config.config import settings
from use_case.common import exceptions

app = FastAPI(title="Banking system APIs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(account_router, prefix="/api/v1")
app.include_router(customer_router, prefix="/api/v1")


@app.exception_handler(exceptions.ErrorAccountNotFound)
async def account_not_found_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=404, content=exc.message)


@app.exception_handler(exceptions.ErrorCustomerNotFound)
async def customer_not_found_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=404, content=exc.message)


@app.exception_handler(exceptions.ErrorInsufficientBalance)
async def insufficient_balance_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=400, content=exc.message)


@app.exception_handler(exceptions.ErrorNotSupportTransactionType)
async def not_support_transaction_type_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=400, content=exc.message)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True, host="0.0.0.0")
