import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image


st.title('Industrial copper modeling')

image = Image.open('copper.jpg')
st.image(image, 'Copper modeling')

tab1, tab2 = st.tabs(["PREDICT SELLING PRICE", "PREDICT STATUS"])
with tab1:
    model = pickle.load(open('model.pkl', 'rb'))




    def user_report():
        id = st.text_input('id')
        item_date = st.text_input('item_date')
        quantity_tons = st.text_input('quantity_tons')
        customer = st.text_input('customer')
        country = st.text_input('country')
        status = st.text_input('status')
        item_type = st.text_input('item_type')
        application = st.text_input('application')
        thickness = st.text_input('thickness')
        width = st.text_input('width')
        material_ref = st.text_input('material_ref')
        product_ref = st.text_input('product_ref')
        delivery_date = st.text_input('delivery_date')
        
    


        user_report_data = {
           'id':id,
           'item_date':item_date,
           'quantity_tons':quantity_tons,
           'customer':customer,
           'country':country,
           'status':status,
           'item_type':item_type,
           'application':application,
           'thickness':thickness,
           'width':width,
           'material_ref':material_ref,
           'product_ref':product_ref,
           'delivery_date':delivery_date
            }   
        report_data = pd.DataFrame(user_report_data, index=[0])
        return report_data


    user_data = user_report()


    if st.button("predict"):
        model.predict(user_data)
        st.write(model.predict(user_data))             


with tab2:


    modelRF = pickle.load(open('RFmodel.pkl', 'rb'))
    
    
    def user_reports():
        id = st.text_input('ids')
        item_date = st.text_input('item_dates')
        quantity_tons = st.text_input('quantity_tonss')
        customer = st.text_input('customers')
        country = st.text_input('countrys')
        item_type = st.text_input('item_types')
        application = st.text_input('applications')
        thickness = st.text_input('thicknesss')
        width = st.text_input('widths')
        material_ref = st.text_input('material_refs')
        product_ref = st.text_input('product_refs')
        delivery_date = st.text_input('delivery_dates')
        selling_price = st.text_input('selling_prices')
    


        user_report_datas = {
           'id':id,
           'item_date':item_date,
           'quantity_tons':quantity_tons,
           'customer':customer,
           'country':country,
           'item_type':item_type,
           'application':application,
           'thickness':thickness,
           'width':width,
           'material_ref':material_ref,
           'product_ref':product_ref,
           'delivery_date':delivery_date,
           'selling_price':selling_price
            }   
        report_datas = pd.DataFrame(user_report_datas, index=[0])
        return report_datas


    user_datas = user_reports()


    if st.button("predicts"):
        modelRF.predict(user_datas)
        st.write(modelRF.predict(user_datas)) 


  