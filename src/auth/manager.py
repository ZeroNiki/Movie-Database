from typing import Optional
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin
from sqlalchemy import select

from src.auth.models import User
from src.auth.utils import get_user_db
from src.db import get_async_session
from src.config import AUTH_TOKEN


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = AUTH_TOKEN
    verification_token_secret = AUTH_TOKEN

    async def on_after_register(
        self,
        user: User,
        request: Optional[Request] = None
    ):
        print(f"User {user.id} {user.username} has been registered.")

    async def on_after_forgot_password(
        self,
        user: User,
        token: str,
        request: Optional[Request] = None
    ):
        print(f"User {user.id} {user.username} \
                has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self,
        user: User,
        token: str,
        request: Optional[Request] = None
    ):
        print(f"Verification requested for user \
                {user.id}. Verification token: {token}")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
