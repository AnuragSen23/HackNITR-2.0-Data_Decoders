import warnings
warnings.filterwarnings('ignore')
import twint
import pandas as pd
pd.set_option('display.max_colwidth', -1)
import streamlit as st
from PIL import Image
import os

image = Image.open(os.path.join('image_dem.jpg'))
st.image(image)
st.title('COVID19 - LeadsFinder')
st.write("LIVE! Twitter data based on location, requirement and availability of leads is scraped to provide instant assistance. Contact details (Phone Number) and location can be retrieved. Do redirect to the tweets using the links generated for more details.")
'-------------------------------------------------------------'
try:
    location = st.text_input("Enter your location (India): ")
    commodity, cause = st.beta_columns(2)
    commodity = commodity.selectbox("Your Requirement: ",("Oxygen","Plasma","Remdesivir","ICU","Tocilizumab","Ventilator","Hospital Beds"))
    cause = cause.selectbox("Available / in Need? ",("Available","Need"))
    st.write("If no record is retrieved from your exact location, try the nearest city from your location.")
    st.markdown("**➡ Searching Leads: **" + location + " " + commodity + " " + cause)
    verified = st.checkbox("Verified resource search")
    if st.button('Search'):
        c = twint.Config()
        if (commodity == "Oxygen" or commodity == "Remdesivir" or commodity == "Ventilator" or commodity == "ICU" or commodity == "Hospital Beds" or commodity == "Plasma"):
            c.Search = location + " " + commodity + " " + cause
        if commodity == "Tocilizumab":
            c.Search = "Tocilizumab"
        c.Phone = True
        if verified:
            c.Verified = True
        c.Pandas = True
        c.Limit = 25
        c.Hide_output = True
        twint.run.Search(c)
        def twint_to_table(columns):
            return twint.output.panda.Tweets_df[columns]
        Tweets = twint_to_table(["date","username","tweet","link"])
        Tweets.set_index("username",inplace=True)
        st.table(Tweets.head(25))
        res = Tweets.drop(['date','tweet'],axis=1)
        res = res.reset_index()
        try:
            st.markdown("**Tweet Source:**")
            st.table(st.markdown(res['link'].head(25)))
        except TypeError:
            pass
    else:
        pass
    st.warning("This app scraps live twitter data by keyword search, thus I am not responsible for it's authenticity.✌️")
    st.info("For Feedbacks and suggestion, drop a message on my LinkedIn😃:  [Anurag Sen](https://www.linkedin.com/in/anurag-sen-aa36961b2/)")
    st.success("Stay Connected. Stay safe. [WHO-Covid19](https://www.who.int/emergencies/diseases/novel-coronavirus-2019/question-and-answers-hub/q-a-detail/coronavirus-disease-covid-19) • [Ministry of health and family welfare](https://www.mohfw.gov.in/) • [GAVI](https://www.gavi.org/covid19?gclid=Cj0KCQjwppSEBhCGARIsANIs4p7U9Uf4QdGlKsTn1nPZjjYbwnMmFSshyqd64qbkHm0gQnoKeIR7GjEaApIhEALw_wcB)")
except KeyError:
     st.markdown("**Relevant records not found 👎**")
