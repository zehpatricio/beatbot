from fastapi import APIRouter, Body, Request
from fastapi.responses import RedirectResponse
from secrets import token_hex

from app.core.services import (
   CreatePlaylistService, 
   FetchUserService,
   RequestAccessTokenService
)
from app.resources.dependencies import get_settings


router = APIRouter()
settings = get_settings()


@router.post("/print-body")
async def print_body(data: dict = Body(...)):
    """
    An API endpoint that prints the request body.
    """
    print(f"Request body: {data}")
    return {"message": "Request body received."}


@router.get("/login")
async def login():
  # Generate a random state string
  state = token_hex(8)

  url = f"https://accounts.spotify.com/authorize?" + \
        f"response_type=code&" + \
        f"client_id={settings.client_id}&" + \
        f"scope={','.join(settings.scopes)}&" + \
        f"redirect_uri={settings.redirect_uri}&" + \
        f"state={state}"

  return RedirectResponse(url=url)


@router.get("/callback")
async def callback(request: Request, code: str, state: str):
    request_access_token = RequestAccessTokenService(
       code,
       settings.redirect_uri, 
       settings.client_id, 
       settings.client_secret
    )
    access_token = request_access_token()

    fetch_user = FetchUserService(access_token)
    user = fetch_user()

    create_playlist = CreatePlaylistService(access_token, user)
    playlist_json = create_playlist('Name')
    return playlist_json['external_urls']['spotify']
