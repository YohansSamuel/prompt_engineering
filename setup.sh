mkdir -p ~/.flaskapp/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.flaskapp/config.toml