import streamlit as st
from services.blobs_service import upload_blob
from services.intelligence_service import analise_card

def show_validation(credit_card):
    if credit_card and credit_card["card_name"]:
        st.markdown(f"<h1 style='color: green;'> Cartão Validado</h1>", unsafe_allow_html=True)
        st.write(f"Titular: {credit_card['card_name']}")
        st.write(f"Emissor: {credit_card['bank_name']}")
        st.write(f"Validade: {credit_card['expiry_date']}")
    else:
        st.markdown(f"<h1 style='color: red;'> Cartão Inválido</h1>", unsafe_allow_html=True)
        st.write('Não foi possível validar este cartão.')



def conf_interface():
    st.title("Upload de Arquivo")
    uploaded_file = st.file_uploader("Selecione um arquivo de imagem", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        file_name = uploaded_file.name
        blob_url = upload_blob(uploaded_file, file_name)
        if blob_url:
            st.write("Enviado com sucesso.")
            try:
                creditcard_data = analise_card(blob_url)
                show_validation(creditcard_data)
            except Exception as e:
                st.write(f"Falha ao analisar cartão: {e}")
        else:
            st.write("Falha ao enviar arquivo.")



if __name__ == "__main__":
    conf_interface()