from fastapi import APIRouter, Depends, HTTPException
from auth.handlers import get_current_active_user
from database import get_db
from app.schemas import User, Product
from sqlalchemy.orm import Session
from app.models import ProductTable, UserTable

router = APIRouter()


# Retourne l'utilisateur si son token est valide
@router.get("/users/me/")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


# Crée une relation produit-utilisateur dans la base de données
@router.post("/users/me/add_product")
def create_user_product_relation(
    product: Product,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    user = (
        db.query(UserTable).filter(UserTable.username == current_user.username).first()
    )
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")

    # Créer un nouvel objet ProductTable et l'ajouter à la base de données
    new_product = ProductTable(
        user_id=user.id,
        name=product.name,
        ecoscore=product.ecoscore,
        natural_resources_score=product.natural_resources_score,
        health_score=product.health_score,
        pollution_score=product.pollution_score,
        ecosystem_score=product.ecosystem_score,
        analyzed_at=product.analyzed_at,
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


# Retourne la liste des produits d'un utilisateur
@router.get("/users/me/products")
async def get_user_products(
    current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)
):
    user = (
        db.query(UserTable).filter(UserTable.username == current_user.username).first()
    )
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")
    return user.products
