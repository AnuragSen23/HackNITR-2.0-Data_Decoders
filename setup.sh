mkdir -p ~/.streamlit/
echo "
[server]\n
headless = true\n
enableCORS=false\n
port = $PORT\n
[theme]\n
primaryColor="#08424f"\n
backgroundColor="#08424f"\n
secondaryBackgroundColor="#0d5a6a"\n
textColor="#ffffff"\n
font=“sans serif”\n
" > ~/.streamlit/config.toml
