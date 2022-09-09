from fastapi import APIRouter, Query, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import groups
from db.database import get_db

from .schemes import GroupResponseScheme, CreateGroupScheme


router = APIRouter(
    prefix='/groups',
    tags=['groups']
)


@router.post('/', response_model=GroupResponseScheme)
def create_group(
    db: Session = Depends(get_db),
    *,
    data: CreateGroupScheme
):
    group = groups.create_group(
        db,
        name=data.name
    )
    return group

@router.get('/', response_model=GroupResponseScheme)
def get_group(
    db: Session = Depends(get_db),
    *,
    id: int = Query(None)
):
    group = groups.get_group(
        db,
        id=id
    )
    return group