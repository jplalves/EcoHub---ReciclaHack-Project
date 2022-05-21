from typing import Dict, List
from app.models.post import Post
from database.repository import save, delete, commit


def create_post(data: Dict) -> Post or None:
    try:
        return save(Post(
            title=data.get('title'),
            type_id=data.get('type_id'),
            garbage_id=data.get('garbage_id'),
            description=data.get('description'),
            comments=data.get('comments'),
            active=data.get('active')
        ))
    except (AttributeError, KeyError, TypeError):
        return


def update_post(post_id: str, data: Dict) -> Post:
    post: Post = get_post_by_id(post_id)
    list_keys = list(data.keys())

    post.name = data.get('name') if data.get('name') else post.name
    post.active = data.get('active') if list_keys.count('active') else post.active
    post.description = data.get('description') if data.get('description') else post.description

    commit()
    return post


def delete_post(post_id: str) -> Post:
    post: Post = get_post_by_id(post_id)
    delete(post)
    commit()
    return post


def get_post() -> List[Post]:
    list_post = Post.query.all()
    return list_post


def get_post_by_id(post_id: str) -> Post:
    return Post.query.get(post_id)
