import streamlit as st
from password_utils import check_password_strength, generate_complex_password, generate_strong_passphrase

st.set_page_config(page_title="SecurePass", page_icon="🔐", layout="centered")

st.title("🔐 SecurePass: Smart Password Strength Auditor")
st.markdown("Check how secure your password is and get instant recommendations!")

# --- Password Input ---
password = st.text_input("Enter a password to check", type="password")

if password:
    result = check_password_strength(password)
    
    st.subheader("🔍 Analysis")
    st.write(f"**Strength Score:** {result['score']} / 4")
    st.write(f"**Estimated Crack Time:** {result['crack_time']}")

    if result['warning']:
        st.warning(f"⚠️ {result['warning']}")

    # Enhanced Suggestions Block
    st.info("💡 Suggestions:")
    if result['suggestions']:
        for s in result['suggestions']:
            st.markdown(f"- {s}")
    else:
        st.markdown("- Your password looks good! No suggestions needed.")

# --- Divider ---
st.markdown("---")

# --- Password Generators ---
st.subheader("🔁 Need a Stronger Password?")
col1, col2 = st.columns(2)

with col1:
    if st.button("🔑 Generate Complex Password"):
        strong_pass = generate_complex_password()
        st.code(strong_pass, language="text")

with col2:
    if st.button("🧠 Generate Smart Passphrase"):
        passphrase = generate_strong_passphrase()
        st.code(passphrase, language="text")

st.markdown("<br><sub>🔒 This tool runs fully locally and does not store any passwords.</sub>", unsafe_allow_html=True)
