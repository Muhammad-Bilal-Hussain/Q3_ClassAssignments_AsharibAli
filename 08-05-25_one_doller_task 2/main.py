from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import json
import os

app = FastAPI()

DATA_FILE = "transactions.json"

# Ensure the file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

# Data model (id is optional on input)
class Transaction(BaseModel):
    id: str = None  # Will be auto-assigned
    type: str       # "Income" or "Expense"
    amount: float
    category: str
    description: str
    date: str

# Load data
def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Save data
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Generate sequential ID like "0001", "0002", etc.
def generate_id():
    data = load_data()
    if not data:
        return "0001"
    last_id = max(int(item["id"]) for item in data if item["id"].isdigit())
    return str(last_id + 1).zfill(4)

# GET all transactions
@app.get("/transactions", response_model=List[Transaction])
def get_transactions():
    return load_data()

# POST a new transaction
@app.post("/transactions", response_model=Transaction)
def add_transaction(transaction: Transaction):
    data = load_data()
    transaction.id = generate_id()
    data.append(transaction.dict())
    save_data(data)
    return transaction

# PUT update transaction
@app.put("/transactions/{transaction_id}", response_model=Transaction)
def update_transaction(transaction_id: str, updated: Transaction):
    data = load_data()
    for i, item in enumerate(data):
        if item["id"] == transaction_id:
            updated.id = transaction_id  # Ensure ID is unchanged
            data[i] = updated.dict()
            save_data(data)
            return updated
    raise HTTPException(status_code=404, detail="Transaction not found")

# DELETE a transaction
@app.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: str):
    data = load_data()
    updated_data = [item for item in data if item["id"] != transaction_id]
    if len(updated_data) == len(data):
        raise HTTPException(status_code=404, detail="Transaction not found")
    save_data(updated_data)
    return {"detail": "Transaction deleted"}
