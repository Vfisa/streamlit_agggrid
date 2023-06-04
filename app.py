import streamlit as st
import pandas as pd
import numpy as np

from st_aggrid import AgGrid, GridOptionsBuilder, JsCode


DATATYPES = ["NUMBER","DECIMAL","NUMERIC","INT","INTEGER","BIGINT","SMALLINT","TINYINT","BYTEINT","FLOAT","FLOAT4","FLOAT8","DOUBLE","DOUBLE","PRECISION","REAL","VARCHAR","CHAR","CHARACTER","STRING","TEXT","BINARY","VARBINARY","BOOLEAN","DATE","DATETIME","TIME","TIMESTAMP","TIMESTAMP_LTZ","TIMESTAMP","TIMESTAMP_NTZ","TIMESTAMP","TIMESTAMP_TZ","TIMESTAMP","VARIANT","OBJECT","ARRAY","GEOGRAPHY","GEOMETRY"]


#@st.cache()
df = pd.DataFrame(
    "",
    index=range(10),
    columns=["name","data_type","length","primary_key","nullable"],
)

gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_default_column(editable=True)

gb.configure_column('data_type',
    cellEditor='agRichSelectCellEditor',
    cellEditorParams={'values':DATATYPES},
    cellEditorPopup=True
)

gb.configure_column('nullable',
    cellEditor='agRichSelectCellEditor',
    cellEditorParams={'values':["True", "False"]},
    cellEditorPopup=True
)

gb.configure_column('primary_key',
    cellEditor='agRichSelectCellEditor',
    cellEditorParams={'values':["True", "False"]},
    cellEditorPopup=True
)

gb.configure_grid_options(enableRangeSelection=True)

cellsytle_jscode = JsCode("""
function(params) {
    if (params.value == 'True') {
        return {
            'color': 'black',
            'backgroundColor': 'DodgerBlue'
        }
    } else {
        return {
            'color': 'black',
            'backgroundColor': 'white'
        }
    }
};
""")
gb.configure_column("primary_key", cellStyle=cellsytle_jscode)
gb.configure_selection('multiple', use_checkbox=True)


response = AgGrid(
    df,
    gridOptions=gb.build(),
    fit_columns_on_grid_load=True,
    allow_unsafe_jscode=True,
    enable_enterprise_modules=True
)

st.subheader("Returned Data")
st.dataframe(response["data"])