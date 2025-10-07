import streamlit as st
import pickle
import base64
def add_bg_image(image_file):
    with open(image_file, "rb") as img_file:
        encoded_img = base64.b64encode(img_file.read()).decode()
    page_bg = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_img}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)



def main():
    add_bg_image("global-connections.jpg")
    scaler = pickle.load(open('scaler.sav', 'rb'))
    encoder = pickle.load(open('label_encoder.sav', 'rb'))
    model = pickle.load(open('model.sav', 'rb'))
    if "page" not in st.session_state:
        st.session_state.page = "input"
    if st.session_state.page == "input":
        st.title(':blue[Telco Customer Churn]')
        SenCit = {"Yes": 1, "No": 0}[st.selectbox(
            label='Whether senior citizen or not?',
            options=['Yes', 'No']
        )]
        Partner=encoder[1].transform([st.selectbox(label='Whether has a partner or not ?',options=['Yes', 'No'])])[0]
        Depen=encoder[2].transform([st.selectbox(label='Whether has dependents or not?',options=['Yes', 'No'])])[0]
        tentu=st.slider(
        label="Number of months has stayed with the company",
        min_value=1,
        max_value=80,
    )
        OnliSecu=encoder[6].transform([st.selectbox(label='Whether has online security or not?',options=['Yes', 'No'])])[0]
        OnliBack=encoder[7].transform([st.selectbox(label='Whether has online backup or not?',options=['Yes', 'No'])])[0]
        DevProt=encoder[8].transform([st.selectbox(label='Whether has device protection or not?',options=['Yes', 'No'])])[0]
        TechSupp=encoder[9].transform([st.selectbox(label='Whether has tech support or not?',options=['Yes', 'No'])])[0]
        StreTv=encoder[10].transform([st.selectbox(label='Whether has streaming TV or not?',options=['Yes', 'No'])])[0]
        contra=encoder[12].transform([st.selectbox(label='Select contract term',options=['Month-to-month', 'One year', 'Two year'])])[0]
        PapleBill=encoder[13].transform([st.selectbox(label='Whether has paperless billing or not ?',options=['Yes', 'No'])])[0]
        PaymMeth=encoder[14].transform([st.selectbox(label='Select the customer’s payment method ',options=['Electronic check', 'Mailed check', 'Bank transfer (automatic)',
           'Credit card (automatic)'])])[0]
        MontChar=st.text_input("Enter the total amount to Monthly charge")
        TotChar=st.text_input("Enter the total amount to Total charge")
        features=[SenCit,Partner,Depen,tentu,OnliSecu,
           OnliBack,DevProt,TechSupp,StreTv,
           contra,PapleBill,PaymMeth,MontChar,
           TotChar]
        pred = st.button("PREDICT")
        if pred:
            result = model.predict(scaler.transform([features]))[0]
            st.session_state.result=result
            st.session_state.page="result"
            st.rerun()
    elif st.session_state.page == "result":

        if st.session_state.result:
            st.title(":red[Prediction Result]")
            st.error("This customer is **Churned**")
        else:
            st.title(":green[Prediction Result]")
            st.success("This customer is **Not Churned**")
        back=st.button("Go Back")
        if back:
            st.session_state.page="input"
            st.rerun()

main()