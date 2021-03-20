mkdir -p ~/.streamlit/

echo "
[server]\n
headless = true\n
enableCORS=false\n
port = $PORT\n
[theme]\n
primaryColor="#5548fd"\n
backgroundColor="#fafafd"\n
secondaryBackgroundColor="#dbf7f3"\n
textColor="#0a0909"\n
font=“sans serif”\n
" > ~/.streamlit/config.tom
