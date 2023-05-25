from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional  # doar pt. put

app = FastAPI()

# CRUD = Create, Read ,Update, Delete
# GET, POST, PUT, DELETE

class Item(BaseModel):
    nume: str
    pret: int
 
class UpdateItem(BaseModel):
    nume: Optional[str] = None
    pret: Optional[int] = None
cars = {
    1:{
        "nume":"Volvo",
        "pret":3600
    },
    2:{ "nume":"Audi",
        "pret":2500,
            
    }
}

@app.get('/')
def acasa():
    return {"Mesaj":"Sautare lume."}

@app.get('/contat')
def contact():
    return {"Contact":"Aceasta este pagina de contact"}


@app.get('/get_car/{item_id}')
def get_car(item_id: int):
    return cars[item_id]

@app.post('/create_car/{item_id}')
def create_car(item_id: int, item: Item):
    if item_id in cars:
        return {"Eroare":"Acest ID deja exista!"}
    cars[item_id] = {"nume":item.nume, "pret":item.pret}
    return cars[item_id]

@app.delete('/delete-car/')
def delete_car(item_id: int):
    if item_id not in cars:
        return {'Eroare':'ID-ul nu exista!'}
    del cars[item_id]
    return {'Succes':'Acest ID a fost sters cu succes!'}

@app.put('/update_cars/{item_id}')
def update_cars(item_id: int, item: UpdateItem):
    if item_id not in cars:
        return {'Eroare':'Acest ID nu exista'}
    if item.nume != None:
        cars[item_id]["nume"] = item.nume
    if item.pret != None:
        cars[item_id]["pret"] = item.pret
    return cars[item_id]