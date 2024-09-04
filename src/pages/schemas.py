import contextlib

from src.auth.utils import get_user_db
from src.auth.manager import get_user_manager

from src.db import get_async_session

get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)
