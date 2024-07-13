from fastapi import HTTPException, Request, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from tp_auth import JWTUtil, Token


class AuthHandler:
    def __init__(self, creds: OAuth2PasswordRequestForm) -> None:
        self.creds = creds


    def token_creator(self, request: Request, response: Response) -> Token:
        jwt_util = JWTUtil()
        payload = {
            "user_id": "user_099",
            "scopes": ["user:read", "user:write"],
            "username": "Admin",
            "issued_to": request.client.host,
        }
        access_token = jwt_util.encode(payload, 1)
        refresh_jwt_util = JWTUtil(token_type="refresh")
        refresh_token_payload = {
            "user_id": "user_099",
            "issued_to": request.client.host,
        }
        refresh_token = refresh_jwt_util.encode(refresh_token_payload, 5)
        response.set_cookie(
            key="refresh_token",
            value=refresh_token,
            max_age=5,
            httponly=True,
            secure=True,
            samesite="strict",
        )
        response.set_cookie(
            key="access_token",
            value=access_token,
            max_age=1,
            httponly=True,
            secure=True,
            samesite="strict",
        )
        return Token(access_token=access_token, refresh_token=refresh_token, token_type="bearer")

    def refresh_access_token(refresh_token: str, request: Request, response: Response) -> Token:
        jwt_util = JWTUtil()
        token_details = jwt_util.decode(refresh_token)
        if request.client.host != token_details["issued_to"] or token_details["token_type"] != "refresh":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")
        payload = {
            "user_id": "user_099",
            "scopes": ["user:read", "user:write"],
            "username": "Admin",
            "issued_to": request.client.host,
        }
        access_token = jwt_util.encode(payload, 1)
        response.set_cookie(
            key="access_token",
            value=access_token,
            max_age=1,
            httponly=True,
            secure=True,
            samesite="strict",
        )
        return Token(access_token=access_token, refresh_token=refresh_token, token_type="bearer")
