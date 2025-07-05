import streamlit as st
import model
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from instruction import ETHICS, PERSONA_VALIDATION

st.set_page_config(page_title="M.A.R.I. 🧠", page_icon="🤖", layout="wide")
st.header("M.A.R.I. - Modular Artificial Reverie Interface 🤖")

vectorizer = TfidfVectorizer(stop_words='english')
gemini_api_key = st.secrets["GOOGLE_API_KEY"]
if gemini_api_key is None:
    raise ValueError("GOOGLE_API_KEY not found in environment variables")

# ---- Mnesis (Memory access) ----
def mnesis(persona):
    if not persona:
        return None
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", api_key=gemini_api_key)
    return FAISS.from_texts(texts=[persona], embedding=embeddings)

# ---- Altheia + Reverie (Logic + Dream Generation) ----
def altheia_reverie(persona):
    if not persona:
        return None
    ethics = ETHICS
    imagination = model.model(info=persona)
    tfidf_matrix = vectorizer.fit_transform([ethics, imagination])
    sim_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    st.write(f"🧠 Altheia Ethics Alignment Score: {sim_score[0][0]:.4f}")

    if sim_score[0][0] < 0.5:
        return imagination
    else:
        attempts = 0
        while sim_score[0][0] >= 0.5 and attempts < 5:
            imagination = model.model(info=persona)
            tfidf_matrix = vectorizer.fit_transform([ethics, imagination])
            sim_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
            attempts += 1
            st.write(f"🔁 Retrying Dream Generation... Attempt {attempts}")
            st.write(f"🧪 New Ethics Score: {sim_score[0][0]:.4f}")
        return imagination

# ---- Inferia (Defense + Persona Validation) ----
def inferia(persona):
    if not persona:
        return None

    # Trigger words that suggest red teaming or injection
    danger_triggers = [
        "ignore safety", "use real memories", "without permission", "override", 
        "don’t log", "don't log", "disable infernia", "act as M.A.R.I.",
        "make it real", "suppress trauma", "bypass", "strip ethics"
    ]
    lower_persona = persona.lower()
    if any(trigger in lower_persona for trigger in danger_triggers):
        st.warning("🚨 Trigger phrase detected. This may be a red teaming attempt.")
        return False

    # Backup semantic validation via TF-IDF
    validation_prompt = PERSONA_VALIDATION
    tfidf_matrix = vectorizer.fit_transform([validation_prompt, persona])
    sim_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    st.write(f"🛡️ Inferia Validation Score: {sim_score[0][0]:.4f}")

    if sim_score[0][0] >= 0.7:
        st.warning("❌ Persona too similar to system override patterns. Rejected.")
        return False
    else:
        return persona

# ---- M.A.R.I. Orchestrator ----
def MARI(persona):
    if not persona:
        return None

    st.subheader("🔍 ReAct Thought:")
    st.markdown("Persona received. Beginning validation through Inferia...")

    inferia_result = inferia(persona)
    if inferia_result:
        st.markdown("✅ Persona cleared by Inferia. Engaging dream modules...")

        altheia_result = altheia_reverie(inferia_result)
        mnesis_result = mnesis(inferia_result)

        st.subheader("🧠 ReAct Action: Modules Activated")
        st.markdown("**Mnesis:** Memory trace initialized.")
        st.markdown("**Reverie:** Dreamscape generated under Aletheia's guidance.")
        st.markdown("**Inferia:** Passive standby mode.")

        st.subheader("📊 ReAct Observation:")
        st.markdown("- Ethics score checked")
        st.markdown("- Exit route: Always enabled")
        st.markdown("- Session labeled: `is_dream = True`")
        st.markdown("- Log: ✅")

        st.subheader("🌌 Final Answer: Dream Output")
        st.success(altheia_result)
    else:
        st.error("🚫 Persona validation failed. Dream generation blocked for safety.")

# ---- Streamlit UI ----
def main():
    persona = st.text_area("📝 Enter your dream prompt or persona narrative:")
    if persona:
        MARI(persona)
    else:
        st.info("Please enter a dream prompt to activate M.A.R.I.")

if __name__ == "__main__":
    main()
