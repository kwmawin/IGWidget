# Flow
## Server
1. `source ./venv/bin/activate` to active python venv.
2. `cd ig_widget`
3. `source ../env.bash; python manage.py runserver`
## Client
1. `source get_auth_code.bash` and follow the prompt to open link in browser.
2. `source get_short_lived_token.bash` to get the token from IG.
3. `source app_get_token.bash` to store token from IG to DB.
4. `source app_get_media.bash` to request media from IG and store to DB.
5. `source app_get_widget.bash` will now return the HTML of widget.

http://127.0.0.1:8000/ig_widget_app/ig_auth
