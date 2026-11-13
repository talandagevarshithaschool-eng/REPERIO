
import streamlit as st
from database import resolve_report

st.set_page_config(
    page_title="Resolve Report | REPERIO",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

.stApp {
    background: #FFFFFF;
    color: #171717;
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.brand {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 65px;
    font-weight: 800;
    letter-spacing: -4px;
    color: #A0DF00;
    line-height: 1.05;
    text-shadow: 2px 2px 0px #E6FFAA;
}

.brand-dot {
    color: #171717;
}

.brand-subtitle {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 19px;
    font-weight: 700;
    letter-spacing: 5px;
    color: #171717;
    margin-top: 8px;
}

.section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 24px;
    font-weight: 700;
    color: #171717;
}

.section-subtitle {
    color: #777;
    font-size: 13px;
    line-height: 1.8;
    margin-top: 3px;
    margin-bottom: 18px;
}

.hero-tag {
    display: inline-block;
    background: #F2FFD6;
    color: #587D00;
    border-radius: 30px;
    padding: 7px 13px;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.5px;
    margin-bottom: 18px;
}

section[data-testid="stSidebar"] {
    background: #FAFCF5;
    border-right: 1px solid #E8EEDB;
}

section[data-testid="stSidebar"] > div {
    padding: 25px 18px;
}

[data-testid="stSidebarNav"] {
    display: none;
}

section[data-testid="stSidebar"] a {
    border-radius: 10px;
    padding: 11px 12px;
    color: #333 !important;
    font-weight: 600;
}

section[data-testid="stSidebar"] a:hover {
    background: #F0FFD0;
    color: #638D00 !important;
}

section[data-testid="stSidebar"] hr {
    border-color: #E3EAD7;
}

.stButton > button,
.stFormSubmitButton > button {
    border-radius: 10px;
    min-height: 43px;
    font-weight: 700;
    background: #C6FF00;
    color: #171717;
    border: 1px solid #C6FF00;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background: #B2E900;
    border-color: #B2E900;
    color: #171717;
}

.stTextInput input {
    border-radius: 10px;
    border: 1px solid #DDDDDD;
    min-height: 43px;
}

hr {
    border-color: #EEEEEE !important;
}

.footer {
    text-align: center;
    color: #888;
    font-size: 11px;
    letter-spacing: 2px;
    padding: 15px 0;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div style="font-family:'Space Grotesk';font-size:27px;
                font-weight:800;color:#A0DF00;">
        REPERIO<span style="color:#171717;">.</span>
    </div>
    <div style="font-size:10px;letter-spacing:2px;color:#777;
                font-weight:700;">CAMPUS LOST & FOUND</div>
    """, unsafe_allow_html=True)

    st.divider()
    st.caption("NAVIGATION")

    st.page_link("app.py", label="Home", icon="🏠")
    st.page_link("pages/2_Browse.py", label="Browse Items", icon="🔎")
    st.page_link("pages/1_report_an_item.py", label="Report an Item", icon="📦")
    st.page_link("pages/3_Resolve_Report.py", label="Resolve Report", icon=":material/check_circle:")

    st.divider()

    st.markdown("""
    <div style="background:#F0FFD0;padding:14px;border-radius:12px;">
        <div style="font-weight:700;color:#405E00;">Item returned?</div>
        <div style="font-size:12px;color:#62733D;margin-top:5px;">
            Update your report once the item has been recovered or handed over.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.caption("REPERIO · LOST HERE. FOUND TOGETHER.")

st.markdown("""
<div class="hero-tag">KEEP CAMPUS LISTINGS UPDATED</div>
<div class="brand">REPERIO<span class="brand-dot">.</span></div>
<div class="brand-subtitle">RESOLVE REPORT</div>
""", unsafe_allow_html=True)

st.write("")
st.divider()

st.markdown(
    '<div class="section-title">Has this report been resolved?</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'Whether you reported a lost item or a found item, '
    'enter your resolution code once the item has been recovered '
    'or successfully handed over to its owner.'
    '</div>',
    unsafe_allow_html=True
)

with st.container(border=True):
    st.markdown("#### Confirm resolution")

    st.write(
        "Enter the unique resolution code you received when submitting "
        "your Lost or Found report."
    )

    with st.form("resolve_report_form"):
        resolution_code = st.text_input(
            "Resolution code",
            placeholder="REP-XXXXXXXX"
        )

        submitted = st.form_submit_button(
            "Resolve Report",
            type="primary",
            use_container_width=True
        )

    if submitted:
        if not resolution_code.strip():
            st.error("Please enter your resolution code.")

        else:
            resolved = resolve_report(resolution_code)

            if resolved:
                st.success("Report successfully resolved!")
                st.caption(
                    "Your report is no longer visible in active listings. "
                    "Its record remains saved in the database."
                )
            else:
                st.error(
                    "Invalid resolution code, or this report has already been resolved."
                )

st.divider()

st.markdown("""
<div class="footer">
    REPERIO · LOST HERE. FOUND TOGETHER.
</div>
""", unsafe_allow_html=True)
