import streamlit as st
import requests
print("✅ Inició la app correctamente")

# Token personal de Hugging Face
import os
from dotenv import load_dotenv
load_dotenv()

HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")


API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    print("Respuesta cruda:", response.text)  # 👈 Log de la respuesta
    return response.json()

# Interfaz de la app
st.title("Resumen Automático de Textos")

st.write("""
Esta aplicación utiliza Inteligencia Artificial para resumir automáticamente textos largos en unas pocas frases. Pegá el texto que quieras resumir abajo y hacé clic en el botón.
""")

texto_usuario = st.text_area("Pegá tu texto aquí:", height=250)

if st.button("Generar resumen"):
    if texto_usuario:
        with st.spinner("Generando resumen..."):
            resultado = query({"inputs": texto_usuario})
            resumen = resultado[0]['summary_text'] if isinstance(resultado, list) else "Error al generar el resumen."
        st.subheader("Resumen generado:")
        st.success(resumen)
    else:
        st.warning("Por favor, ingresá un texto para resumir.")

st.markdown("---")
st.header("¿Cómo funciona?")
st.write("""
Esta app utiliza el modelo de IA `facebook/bart-large-cnn` alojado en Hugging Face para generar resúmenes automáticos. Es un modelo entrenado con grandes cantidades de datos y puede entender el contenido de un texto largo para extraer sus ideas principales.

Pasos:
1. Pegás un texto largo.
2. La app lo envía al modelo de IA.
3. El modelo responde con un resumen conciso.
""")
