import streamlit as st
import pandas as pd
from pandas.io.formats import excel
import io

st.markdown('BOM breaker')
excel.ExcelFormatter.header_style = None

def create_xlsx(data_pd):
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer) as writer:
        data_pd.to_excel(writer, index = False)
    return buffer

uploaded_file = st.file_uploader("Choose a Excel file", accept_multiple_files=False, type='xlsx')
if uploaded_file is not None:

    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_excel(uploaded_file)
    df.drop(['STFIRM', 'STWKNR', 'B7PONR', 'DESCR1', 'DESCR2', 'TEMATC', 'TETART'], axis=1, inplace = True)
    df.rename(columns={"B7STU0": "Part-no.", "B7OSTU": "Level", "B7OTNR": "Intermediar", "B7OMNG": "Quantity"}, inplace=True)

    st.dataframe(df, use_container_width=True,hide_index=True)
    
    st.download_button(
        label="Download",
        data=create_xlsx(df) ,
        file_name='customer.xlsx'
)