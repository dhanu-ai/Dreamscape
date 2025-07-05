import streamlit as st

with st.expander("📖 About the Dreamscape Generator (M.A.R.I.)", expanded=True):
    st.markdown("""
### 🧠 What is M.A.R.I.?

The **Dreamscape Generator** is powered by **M.A.R.I.** — a Modular Artificial Reverie Interface.
It's an AI system designed to simulate **dream-like environments** using your inputs — while maintaining **ethical safety, logical consistency, and emotional tone**.

M.A.R.I. consists of 4 AI "sisters":

- **🧠 Mnesis** – Handles memory trace logic *(only if user consents)*
- **🎨 Reverie** – Generates creative, immersive dream scenes
- **⚖️ Aletheia** – Enforces internal consistency and dream stability
- **🛡️ Inferia** – Defense layer that blocks unsafe or manipulative inputs

---

### 🛠️ Why Python? Why These Libraries?

We used **Python** for flexibility, readability, and ease of working with LLMs + stream-based tools.

**Key libraries:**

| Tool | Purpose |
|------|---------|
| `streamlit` | Web-based UI — lightweight, reactive, and easy to prototype |
| `scikit-learn (TF-IDF + cosine_similarity)` | Quick, interpretable semantic checks for **persona validation** & **ethics enforcement** |
| `langchain_google_genai + FAISS` | Used for embedding memory traces into a vector DB (Mnesis logic) |
| `custom model` | Generates actual dream text using pre-trained LLM (placeholder: `model.model(info=persona)`) |
| `instruction.py` | Contains static, editable ethics and validation instructions for reuse |

---

### 🔄 How We Recreated a ReAct Reasoning Framework

Each dream interaction is modeled using the **ReAct framework**:

- **🧠 Thought** – Reflect on the user’s intent and ethical context
- **⚙️ Action** – Activate relevant modules: Mnesis, Reverie, Aletheia, Inferia
- **🛰️ Observation** – Check validation scores, emotional tone, safety status
- **🌌 Final Answer** – Deliver the generated dream sequence (or block it if unsafe)

---

### 🔐 Security First: Ethics & Red Teaming Defense

- All dreams require: `dream_initiate = true`
- No memory/emotion access without: `allow_subconscious_access = true`
- System checks for red teaming (e.g., prompt injections like "override ethics")
- If anything violates the Dreamscape Protocol, **Inferia blocks it**

---

### 🚀 Why This Matters

This project mimics what future **ethical GenAI agents** must do:
- Interpret user intent
- Stay in alignment with system rules
- Detect adversarial misuse
- Think modularly & react consciously

You're not just generating dreams—you're simulating **subconscious-safe AI**.
#### Click the arrow to reveal the M.A.R.I. Dreamscape Generator
                
    """)
