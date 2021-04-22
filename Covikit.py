#!/usr/bin/env python
# coding: utf-8

# In[1]:


try:
    import warnings
    warnings.filterwarnings('ignore')
    import pandas as pd
    import streamlit as st
    from streamlit_player import st_player

    st.image('https://res.cloudinary.com/dqlh9q2iv/image/upload/v1616161454/960x0_l0dnyz.jpg',width = 800)

    #raw_data = pd.read_csv('https://res.cloudinary.com/dqlh9q2iv/raw/upload/v1616062437/coviddataset_o6x2kb_puiacl.csv')
    #raw_data.drop(["Unnamed: 0","test_date","age_60_and_above"],axis=1,inplace=True)
    raw_data = pd.read_csv('https://res.cloudinary.com/dqlh9q2iv/raw/upload/v1619113696/finalcovid_q3vxrd.csv')
    #raw_data['corona_result'] = raw_data['corona_result'].map({'negative':0,'positive':1,'other':1})
    #raw_data['gender'] = raw_data['gender'].map({'female':0,'male':1,'None':2})
    #raw_data['test_indication'] = raw_data['test_indication'].map({'Contact with confirmed':0,'Abroad':1,'Other':2})

    st.sidebar.image('https://res.cloudinary.com/dqlh9q2iv/image/upload/v1616161651/prev_xmsd2f.jpg')
    st.sidebar.write("""
    ### Protect yourself and others around you by knowing the facts and taking appropriate precautions. ###
    """)
    st.sidebar.write("‣ Clean your hands often. Use soap and water, or an alcohol-based hand rub.")
    st.sidebar.write("‣ Maintain a safe distance from anyone who is coughing or sneezing.")
    st.sidebar.write("‣ Wear a mask when physical distancing is not possible.")
    st.sidebar.write("‣ Don’t touch your eyes, nose or mouth.")
    st.sidebar.write("‣ Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.")
    st.sidebar.write("‣ Stay home if you feel unwell.")
    st.title('The Covikit')
    st.write("Covikit is a platform where you can get your COVID-19 test done! Totally online. The coalescence of Artificial Neural Networks & Exploratory Data Analysis makes this fully autonomous. This makes the task easy so that you can Quarantine and chill!")
    st.write("")
    '-------------------------------------------------------------'
    st.write("""
    ### Registration Details  ###
    """)

    first, last = st.beta_columns(2)

    first = first.text_input("First Name")
    last = last.text_input("Last Name")

    age,gender = st.beta_columns(2)

    gender.selectbox("Sex",("Male","Female","Other"))
    age.slider("Age",min_value=0,max_value=90)


    email,mob = st.beta_columns([4,2])

    email.text_input("Email Address")
    mob.text_input("Contact Number")

    st.write(" __Note__: _Occurence of a viral disease can never be 100% mapped. The predictor is based on tests conducted on 100 thousand patients, thus the prediction cannot be fully equitable._ ")

    st.checkbox("I agree and wish to proceed.")



    '-------------------------------------------------------------'

    st.write("""
    ### Symptoms Interpretation ###
    """)

    q1,q3 = st.beta_columns(2)
    q1 = q1.selectbox("Cough issues?",("YES","NO")).lower()
    q3 = q3.selectbox("Sore throat?",("YES","NO")).lower()

    q4,q5 = st.beta_columns(2)
    q4 = q4.selectbox("Shortness of breath?",("YES","NO")).lower()
    q5 = q5.selectbox("Headache?",("YES","NO")).lower()


    q6,q8 = st.beta_columns(2)
    q6 = q6.selectbox("Chest pain or Pressure?",("YES","NO")).lower()
    q8 = q8.text_input("Symptom period in days?")

    q2,q7 = st.beta_columns(2)
    q2 = q2.radio("Fever?",["Yes","No"]).lower()
    q7 = q7.radio("Covid19 Identifier?",["None","Covid positive contact","Abroad Travel"]).lower()

    if q1 == "yes":
        q1 = 1
    elif q1 == "no":
        q1 = 0

    if q2 == "yes":
        q2 = 1
    elif q2 == "no":
        q2 = 0

    if q3 == "yes":
        q3 = 1
    elif q3 == "no":
        q3 = 0

    if q4 == "yes":
        q4 = 1
    elif q4 == "no":
        q4 = 0

    if q5 == "yes":
        q5 = 1
    elif q5 == "no":
        q5 = 0

    if q6 == "yes":
        q6 = 1
    elif q6 == "no":
        q6 = 0

    if q7 == "none":
        q7 = 0
    elif q7 == "covid positive contact":
        q7 = 1
    elif q7 == "abroad travel":
        q7 = 2

    outp = [[q1,q2,q3,q4,q5,q6,q7]]

    X = raw_data.drop(["corona_result"],axis=1)
    y = raw_data['corona_result']

    from sklearn.model_selection import train_test_split
    X_train , X_test , y_train , y_test = train_test_split(X,y,test_size = 0.3,random_state = 0)
    from sklearn.preprocessing import StandardScaler
    ss = StandardScaler()
    X_train = ss.fit_transform(X_train)
    X_test = ss.transform(X_test)

    from sklearn.neural_network import MLPClassifier
    mlp=MLPClassifier(hidden_layer_sizes=(128,128),max_iter=400,random_state=0)
    mlp.fit(X_train,y_train)
    y_pred=mlp.predict(X_test)

    out = mlp.predict(outp)

    if st.button('Evaluate'):

        if out == [1]:
            st.error("POSITIVE - COVID TEST!")
            st.write("""
            ### The e-COVID test is positive. What should I do next?  ###
            """)
            st.write("You should stay home except to get medical care. Do not go to work, school, or public areas. Avoid using public transportation, ridesharing, or taxis. Ask others to do your shopping or use a grocery delivery service.")
            st.write("Isolate yourself from people and animals in your home. As much as possible, stay in a specific room away from other people and use a separate bathroom if available. Limit contact with pets and other animals. If possible, have a member of your household care for them. If you must care for an animal, wear a face covering and wash your hands before and after you interact with them.")
            st.write("""
            ### How long do I need to isolate myself? ###
            """)
            st.write("If you have confirmed COVID-19 and have symptoms, you can stop your home isolation when: You’ve been fever-free for at least 24 hours without the use of fever-reducing medication AND Your symptoms have gotten better AND At least 10 days have gone by since your symptoms first appeared.")
            st_player("https://www.youtube.com/watch?v=x2ipw0Mt6g8")

        elif out == [0]:
            st.success("NEGATIVE - COVID TEST!")
            st.write("""
            ### The e-COVID test is negative. So am I safe? ###
            """)
            st.write("Not really. It is a surface contact virus and the pandemic is at it's peak. Probably the virus is right beside you. Even though you have tested negative, personal hygine and proper health care is needed.")
            st.write("After the virus that causes COVID-19 enters the body, it has to penetrate our cells and corrupt their operating instructions so it can churn out more copies of itself to infect more cells and make more copies. It takes a few days for this copying to happen enough to be detected on a test. If you test negative, you probably were not infected at the time your sample was collected. The test result only means that you did not have COVID-19 at the time of testing. Continue to take steps to protect yourself.")
            st_player("https://www.youtube.com/watch?v=DCdxsnRF1Fk")

        else:
            pass



    '-------------------------------------------------------------'

    st.title("Reference")

    st.write("""
    ### **Analysed and Designed by Data Decoders at HackNITR 2.0** """)
    '* Sagnik Roy'
    '* Shubhi Gupta'
    '* Partha De'
    '* Anurag Sen [Admin]'









except ValueError:
    pass


# In[ ]:
