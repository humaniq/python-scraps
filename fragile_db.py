import asyncio
import functools
import logging
import socket

from asyncpg.exceptions import PostgresConnectionError, InterfaceError


logger = logging.getLogger()


def fragile_db():
    """
    Shuts down the whole app on any DB connection error
    """
    handled_exceptions = (
        OSError,
        socket.gaierror,
        asyncio.TimeoutError,
        PostgresConnectionError,
        InterfaceError
    )
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args, **kwargs):
            try:
                result = await func(*args, **kwargs)
            except handled_exceptions:
                logger.critical('Postgres connection is gone, exiting')
                raise SystemExit()
            return result
        return wrapped
    return wrapper
