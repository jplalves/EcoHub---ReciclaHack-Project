from typing import Dict, List
from app.models.type_of_garbage import TypeOfGarbage
from database.repository import save, delete, commit


def create_type_garbage(data: Dict) -> TypeOfGarbage or None:
    try:
        return save(TypeOfGarbage(
            type=data.get('type'),
            description=data.get('description'),
            color=data.get('color'),
            active=data.get('active')
        ))
    except (AttributeError, KeyError, TypeError):
        return


def update_type_garbage(garbage_id: str, data: Dict) -> TypeOfGarbage:
    type_garbage: TypeOfGarbage = get_type_garbage_by_id(garbage_id)
    list_keys = list(data.keys())

    type_garbage.name = data.get('name') if data.get('name') else type_garbage.name
    type_garbage.active = data.get('active') if list_keys.count('active') else type_garbage.active
    type_garbage.description = data.get('description') if data.get('description') else type_garbage.description

    commit()
    return type_garbage


def delete_garbage(garbage_id: str) -> TypeOfGarbage:
    type_garbage: TypeOfGarbage = get_type_garbage_by_id(garbage_id)
    delete(type_garbage)
    commit()
    return type_garbage


def get_type_garbage() -> List[TypeOfGarbage]:
    list_type_garbage = TypeOfGarbage.query.all()
    return list_type_garbage


def get_type_garbage_by_id(garbage_id: str) -> TypeOfGarbage:
    return TypeOfGarbage.query.get(garbage_id)
