source env.bash

curl -X POST \
  https://api.instagram.com/oauth/access_token \
  -F client_id=$INSTAGRAM_APP_ID \
  -F client_secret=$INSTAGRAM_APP_SECRET \
  -F grant_type=authorization_code \
  -F redirect_uri=$SITE \
  -F code=$CODE
