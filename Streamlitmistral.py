import streamlit as st
import requests

st.header("Bienvenue dans l'application Mistral-7B-Instruct-v0.3 en Français")
st.write("Cette application utilise le modèle Mistral-7B-Instruct-v0.3 pour générer des réponses en français basées sur les instructions fournies par l'utilisateur.")


# Champ de texte pour l'entrée utilisateur
user_input = st.text_area("Entrez votre texte ici :")


# Bouton pour générer la réponse
if st.button("Générer une réponse"):
    if user_input:
        # URL de l'API d'inférence de Hugging Face
        api_url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
        
        # Votre clé API Hugging Face
        headers = {
            "Authorization": f"Bearer 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"
        }
        
        # Données de la requête avec instruction en français
        prompt = f"Réponds à la question suivante en français : {user_input}"
        
        data = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 256,
                "temperature": 0.7,
                "top_p": 0.95,
                "do_sample": True,
                "seed": 42
            }
        }
        
        # Appel à l'API
        response = requests.post(api_url, headers=headers, json=data)
        
        if response.status_code == 200:
            result = response.json()
            generated_text = result[0]['generated_text'].strip()
            # Suppression de la prompt initiale de la réponse générée
            prompt_in_response = "Réponds à la question suivante en français : " + user_input + "\n\nRéponse"
            clean_response = generated_text.replace(prompt_in_response, "").strip()
            # Affichage de la réponse nettoyée
            st.write("Réponse générée :")
            st.write(clean_response)
        else:
            st.error("Erreur lors de l'appel à l'API : " + response.text)
    else:
        st.error("Veuillez entrer un texte pour générer une réponse.")
