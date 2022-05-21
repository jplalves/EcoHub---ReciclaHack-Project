from typing import Dict, List
from app.models.entities.garbage import Garbage
from database.repository import save, delete, commit


def create_garbage(data: Dict) -> Garbage or None:
    try:
        return save(Garbage(
            name=data.get('name'),
            description=data.get('description'),
            active=data.get('active'),
            type_id=data.get('type_id')
        ))
    except (AttributeError, KeyError, TypeError):
        return


def update_garbage(garbage_id: str, data: Dict) -> Garbage:
    garbage: Garbage = get_garbage_by_id(garbage_id)
    list_keys = list(data.keys())

    garbage.name = data.get('name') if data.get('name') else garbage.name
    garbage.active = data.get('active') if list_keys.count('active') else garbage.active
    garbage.description = data.get('description') if data.get('description') else garbage.description

    commit()
    return garbage


def delete_garbage(garbage_id: str) -> Garbage:
    garbage: Garbage = get_garbage_by_id(garbage_id)
    delete(garbage)
    commit()
    return garbage


def get_garbage() -> List[Garbage]:
    list_garbage = Garbage.query.all()
    return list_garbage


def get_garbage_by_id(garbage_id: str) -> Garbage:
    return Garbage.query.get(garbage_id)
