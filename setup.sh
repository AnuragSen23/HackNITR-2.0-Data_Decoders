mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
[theme]\n
primaryColor="#5548fd"\n
backgroundColor="#fafafd"\n
secondaryBackgroundColor="#dbf7f3"\n
textColor="#0a0909"\n
font=“sans serif”\n
" > ~/.streamlit/config.toml
