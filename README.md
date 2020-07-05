# Server
1. `source ./venv/bin/activate` to active python venv.
2. `cd ig_widget; python manage.py runserver`
# Client
3. `source get_auth_code.bash` and follow the prompt to open link in browser.
4. `source get_short_lived_token.bash` to get the token from IG.
5. `source app_get_token.bash` to store token from IG to DB.
6. `source app_get_media.bash` to request media from IG and store to DB.
7. `source app_get_widget.bash` will now return the HTML of widget.
