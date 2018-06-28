import asyncio
import functools
import logging
import socket

from asyncpg.exceptions import PostgresConnectionError, InterfaceError, UndefinedTableError


logger = logging.getLogger()


CONNECTION_EXCEPTIONS = (
    OSError,
    socket.gaierror,
    asyncio.TimeoutError,
    PostgresConnectionError,
    InterfaceError
)


QUERY_EXCEPTIONS = (
    UndefinedTableError,
)


def fragile_db():
    """
    Shuts down the whole app on any DB connection or table access error
    """
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args, **kwargs):
            try:
                result = await func(*args, **kwargs)
            except CONNECTION_EXCEPTIONS:
                logger.critical('Postgres connection is gone, exiting')
                raise SystemExit()
            except QUERY_EXCEPTIONS:
                logger.critical('Fatal Postgres query error, exiting')
                raise SystemExit()
            return result
        return wrapped
    return wrapper
