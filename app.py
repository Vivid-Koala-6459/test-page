import streamlit as st
import importlib
import sys
import os
#
sys.path.append(os.path.dirname(__file__))

# --- 1. PAGE CONFIG ---
st.set_page_config(
    page_title="Tester app",
    layout="wide"
)

import streamlit.components.v1 as components

components.html("""
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8411241596191088"
         crossorigin="anonymous"></script>
    <meta name="google-adsense-account" content="ca-pub-8411241596191088">
""", height=0)

# ====================== GOOGLE ADSENSE START ======================
#st.markdown(
#    """
#    <meta name="google-adsense-account" content="ca-pub-8411241596191088">
#    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8411241596191088"
#         crossorigin="anonymous"></script>
#    """,
#    unsafe_allow_html=True
#)
# ====================== GOOGLE ADSENSE END ======================



# --- 4. SIDEBAR HEADER ---
st.sidebar.markdown('**🚧 Maintenance underway. ⚠️ The app modules may not perform optimally, please try again later. 🙏</h3>**', unsafe_allow_html=True)
st.sidebar.markdown(
    '<h3 title="The most comprehensive app you will ever need.">'
    '🔥</h3>',
    unsafe_allow_html=True
)
st.sidebar.markdown("**AI-Powered Tool**")
                 
st.sidebar.caption(f"Session: {session_id[:8]}...")

# --- 5. NAVIGATION ---
tabs = ["Forecast", "Monte Carlo", "Risk Analysis", "Ask the AI", "Report"]
tab_choice = st.sidebar.radio("Navigate", tabs, index=0)


# Sidebar popover for disclaimer
with st.sidebar.popover("📜 View Disclaimer"):
    st.markdown("""
        <div style="font-size: 10px; line-height: 1.4;">
        <strong>🔒 Full Legal Disclaimer</strong><br><br>

        This tool is provided strictly for educational and informational purposes.  It does not constitute financial, 
        investment, retirement, legal, medical, or emergency advice.  No responsibility is taken for the accuracy of inputs, 
        assumptions, projections, or any outputs whatsoever from this application. 
    
        """,
        unsafe_allow_html=True
    )


# --- 6. SAFE MODULE LOADER ---
def load_module(name: str):
    """
    Import once; Python's sys.modules cache handles subsequent calls.
    Never reload — it breaks widget state and module identity.
    """
    try:
        return importlib.import_module(f"modules.{name}")
    except Exception as e:
        st.error(f"Failed to load module '{name}': {e}")
        return None

# --- 7. ROUTING ---
if tab_choice == "Forecast":
    mod = load_module("forecast")
    if mod and hasattr(mod, "forecast_tab"):
        mod.forecast_tab()

elif tab_choice == "Monte Carlo":
    mod = load_module("monte_carlo")
    if mod and hasattr(mod, "monte_carlo_tab"):
        mod.monte_carlo_tab()

elif tab_choice == "Risk Analysis":
    mod = load_module("risk_analysis")
    if mod and hasattr(mod, "risk_tab"):
        mod.risk_tab()

elif tab_choice == "Ask the AI":
    mod = load_module("ask_ai")
    if mod and hasattr(mod, "ask_ai_tab"):
        mod.ask_ai_tab()

elif tab_choice == "Report":
    mod = load_module("report")
    if mod and hasattr(mod, "report_tab"):
        mod.report_tab()

