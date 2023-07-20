from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from smit_test.settings import settings

http_bearer = HTTPBearer()


def only_admin(
    authorization: Annotated[
        HTTPAuthorizationCredentials | None, Depends(http_bearer)
    ] = None
) -> None:
    if authorization and authorization.credentials == settings.ADMIN_TOKEN:
        return
    raise HTTPException(status.HTTP_403_FORBIDDEN, "Only admin.")
