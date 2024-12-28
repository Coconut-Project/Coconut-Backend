from typing import Type, Union
from pydantic import BaseModel
import requests
from api.schemas import EcoCountries, EcoMaterials, EcoProducts
from api.models import *
from sqlalchemy.orm import Session


class Endpoint(BaseModel):
    name: str
    response: Type[BaseModel]


ENDPOINTS: list[Endpoint] = [
    Endpoint(name="countries", response=EcoCountries),
    Endpoint(name="materials", response=EcoMaterials),
    Endpoint(name="products", response=EcoProducts),
]


def fetch_data(
    endpoint: Endpoint,
) -> Union[list[EcoProducts], list[EcoMaterials], list[EcoCountries]]:
    url = f"https://ecobalyse.beta.gouv.fr/api/textile/{endpoint.name}"
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = [endpoint.response(**element) for element in r.json()]
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None


def new_instance_table(
    schema: Union[EcoCountries, EcoMaterials, EcoProducts],
    db: Session,
):

    if isinstance(schema, EcoCountries):
        type_table = EcoCountriesTable
    elif isinstance(schema, EcoMaterials):
        type_table = EcoMaterialsTable
    elif isinstance(schema, EcoProducts):
        type_table = EcoProductsTable
    else:
        raise ValueError("Unsupported schema type")
    new_instance = type_table(
        code=schema.code,
        name=schema.name,
    )

    db.add(new_instance)
    db.commit()
    db.refresh(new_instance)

    return new_instance
