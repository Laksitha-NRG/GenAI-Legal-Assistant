import streamlit as st
from nlp.text_extractor import extract_text
from nlp.clause_extractor import extract_clauses
from nlp.ner import extract_entities
from nlp.risk_analyzer import analyze_clause_risk
from llm.legal_reasoner import explain_clause
from utils.pdf_generator import generate_pdf
from utils.text_normalizer import normalize_contract_text
import json
from datetime import datetime
import os

# ================== PAGE CONFIG ==================
st.set_page_config(
    page_title="GenAI Legal Assistant",
    page_icon="⚖️",
    layout="wide"
)

# Hide Streamlit UI clutter
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ================== HERO SECTION ==================
st.markdown("""
<div style="
    background: linear-gradient(90deg, #f8fafc, #eef2ff);
    padding: 40px;
    border-radius: 16px;
    text-align: center;
    margin-bottom: 30px;
">
    <h1 style="font-size: 42px;">⚖️ GenAI Legal Assistant</h1>
    <h3 style="color: #4b5563;">
        Smart Contract Risk Analysis for Indian SMEs
    </h3>
    <p style="font-size: 18px; color: #374151; max-width: 900px; margin: auto;">
        Upload business contracts and instantly get
        <b>risk scores, clause explanations, Hindi & English insights</b>,
        and downloadable legal reports — powered by Generative AI.
    </p>
</div>
""", unsafe_allow_html=True)

# ================== FEATURES ==================
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="padding:20px; border-radius:14px; background:#f0fdf4;">
    <h4>🔍 Risk Detection</h4>
    <p>
    Automatically detects penalty clauses, indemnities,
    unilateral termination, lock-in periods and more.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="padding:20px; border-radius:14px; background:#eff6ff;">
    <h4>🌐 Multilingual Support</h4>
    <p>
    Supports English & Hindi contracts with
    simple explanations for business owners.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="padding:20px; border-radius:14px; background:#fff7ed;">
    <h4>📄 Audit-Ready Reports</h4>
    <p>
    Generates downloadable PDF reports
    for legal review & compliance tracking.
    </p>
    </div>
    """, unsafe_allow_html=True)

# ================== UPLOAD SECTION ==================
st.markdown("---")
st.markdown("### 📤 Upload Your Contract")

uploaded_file = st.file_uploader(
    "Upload Contract (PDF / DOCX / TXT)",
    type=["pdf", "docx", "txt"]
)

# ================== PROCESSING ==================
if uploaded_file:
    text = extract_text(uploaded_file)

    # Auto language detection + normalization
    text, language = normalize_contract_text(text)
    st.info(f"🗣️ Detected Language: {language}")

    # Show extracted text
    st.subheader("📄 Extracted Contract Text")
    st.text_area("Contract Content", text, height=220)

    # NLP tasks
    clauses = extract_clauses(text)
    entities = extract_entities(text)

    st.subheader("🔍 Identified Legal Entities")
    st.json(entities)

    st.subheader("📌 Clause-by-Clause Risk Analysis")

    risks = []
    clause_details = []

    for i, clause in enumerate(clauses[:5]):
        risk = analyze_clause_risk(clause)
        risks.append(risk)

        explanation = explain_clause(clause, language)

        clause_details.append({
            "text": clause,
            "risk": risk,
            "explanation": explanation
        })

        with st.expander(f"Clause {i+1} | Risk Level: {risk}"):
            st.write(clause)
            st.info(explanation)

    # ================== OVERALL RISK ==================
    st.subheader("📊 Overall Contract Risk")

    overall_risk = (
        "HIGH" if "HIGH" in risks else
        "MEDIUM" if "MEDIUM" in risks else
        "LOW"
    )

    if overall_risk == "HIGH":
        st.error("🔴 HIGH RISK CONTRACT – Legal review strongly recommended")
    elif overall_risk == "MEDIUM":
        st.warning("🟡 MEDIUM RISK CONTRACT – Renegotiation advisable")
    else:
        st.success("🟢 LOW RISK CONTRACT – No major legal red flags detected")

    # ================== PDF DOWNLOAD ==================
    if st.button("📄 Download Risk Report (PDF)"):
        os.makedirs("reports", exist_ok=True)
        pdf_path = f"reports/{uploaded_file.name}_risk_report.pdf"

        generate_pdf(
            pdf_path,
            uploaded_file.name,
            overall_risk,
            clause_details,
            language
        )

        with open(pdf_path, "rb") as f:
            st.download_button(
                "⬇️ Click to Download PDF",
                f,
                file_name=os.path.basename(pdf_path),
                mime="application/pdf"
            )

    # ================== AUDIT LOG ==================
    os.makedirs("data", exist_ok=True)
    audit = {
        "file": uploaded_file.name,
        "language": language,
        "overall_risk": overall_risk,
        "timestamp": str(datetime.now())
    }

    with open("data/audit_log.json", "a", encoding="utf-8") as f:
        json.dump(audit, f)
        f.write("\n")

    st.success("✅ Audit log updated successfully")

# ================== DISCLAIMER ==================

