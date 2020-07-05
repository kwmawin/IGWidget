source env.bash
curl -X POST \
  $APP_URL:$APP_PORT/get_token/ \
  -F access_token=$ACCESS_TOKEN \
  -F user_id=$USER_ID
