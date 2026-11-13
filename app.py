

import streamlit as st
from database import get_reports

st.set_page_config(
    page_title="REPERIO | Campus Lost & Found",
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

.brand-dot { color: #171717; }

.brand-subtitle {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 19px;
    font-weight: 700;
    letter-spacing: 5px;
    color: #171717;
    margin-top: 8px;
}

.hero-description {
    color: #777;
    font-size: 15px;
    line-height: 1.8;
    max-width: 600px;
    margin-top: 15px;
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

.section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 24px;
    font-weight: 700;
    color: #171717;
}

.section-subtitle {
    color: #777;
    font-size: 13px;
    margin-top: 3px;
    margin-bottom: 18px;
}

.item-card {
    border: 1px solid #EAEAEA;
    border-radius: 17px;
    padding: 19px;
    min-height: 205px;
    margin-bottom: 12px;
    background: white;
}

.item-icon {
    background: #F4F9E9;
    border-radius: 13px;
    width: 48px;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    margin-bottom: 15px;
}

.item-name {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 19px;
    font-weight: 700;
    color: #171717;
    overflow-wrap: anywhere;
    margin-bottom: 7px;
}

.item-category {
    color: #777;
    font-size: 12px;
    margin-bottom: 13px;
}

.status {
    display: inline-block;
    border-radius: 20px;
    padding: 5px 10px;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 0.7px;
    text-transform: uppercase;
}

.status-lost {
    background: #FFF0D9;
    color: #A65A00;
}

.status-found {
    background: #EFFFCA;
    color: #527900;
}

.status-other {
    background: #EEEEEE;
    color: #555;
}

.item-location {
    color: #555;
    font-size: 12px;
    margin-top: 12px;
}

/* Sidebar */
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

.stButton > button {
    border-radius: 10px;
    min-height: 43px;
    font-weight: 700;
}

.stButton > button[kind="primary"] {
    background: #C6FF00;
    color: #171717;
    border: 1px solid #C6FF00;
}

.stButton > button[kind="primary"]:hover {
    background: #B2E900;
    border-color: #B2E900;
    color: #171717;
}

.stButton > button:not([kind="primary"]) {
    background: white;
    border: 1px solid #DDDDDD;
    color: #171717;
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
        <div style="font-weight:700;color:#405E00;">Lost something?</div>
        <div style="font-size:12px;color:#62733D;margin-top:5px;">
            Your campus community can help you find it.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.caption("REPERIO · LOST HERE. FOUND TOGETHER.")



st.markdown("""
<div class="hero-tag">A CAMPUS COMMUNITY PLATFORM</div>
<div class="brand">REPERIO<span class="brand-dot">.</span></div>
<div class="brand-subtitle">LOST & FOUND</div>
<div class="hero-description">
    Lost something? Found something that isn't yours?
    Reperio helps campus belongings find their way back
    to the people they belong to.
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")


st.markdown(
    '<div class="section-title">What brings you here?</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="section-subtitle">Find an item or help someone find theirs.</div>',
    unsafe_allow_html=True
)

action1, action2 = st.columns(2, gap="large")

with action1:
    if st.button("📦  Report an Item", type="primary",
                 use_container_width=True):
        st.switch_page("pages/1_report_an_item.py")

with action2:
    if st.button("🔎  Browse All Items", use_container_width=True):
        st.switch_page("pages/2_Browse.py")

st.write("")
st.divider()



st.markdown(
    '<div class="section-title">Recently Reported</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="section-subtitle">The latest items reported by your campus community.</div>',
    unsafe_allow_html=True
)

reports = get_reports()


recent_reports = sorted(
    reports,
    key=lambda report: str(report[9] or ""),
    reverse=True
)[:6]

if not recent_reports:
    st.info("No reports yet. Be the first to add an item!")

else:
    icons = {
        "Electronics": "💻",
        "Accessories": "🎒",
        "Clothing": "👕",
        "Books & Stationery": "📚",
        "Documents": "📄",
        "ID Cards": "🪪",
        "Other": "📦"
    }

    for start in range(0, len(recent_reports), 3):
        cols = st.columns(3, gap="large")

        for col, report in zip(cols, recent_reports[start:start + 3]):
            item_name = report[1] or "Unnamed item"
            item_type = report[2] or "Not specified"
            category = report[3] or "Other"
            location = report[4] or "Location not specified"
            status = report[2] or "Unknown"

            icon = icons.get(category, "📦")

            status_class = "status-other"
            if status.strip().lower() == "lost":
                status_class = "status-lost"
            elif status.strip().lower() == "found":
                status_class = "status-found"

            with col:
                st.markdown(f"""
                <div class="item-card">
                    <div class="item-icon">{icon}</div>
                    <div class="item-name">{item_name}</div>
                    <div class="item-category">{category} · {item_type}</div>
                    <span class="status {status_class}">{status}</span>
                    <div class="item-location">📍 {location}</div>
                </div>
                """, unsafe_allow_html=True)

    if st.button("Explore all reports →", use_container_width=True):
        st.switch_page("pages/2_Browse.py")


st.divider()

st.markdown("""
<div class="footer">
    REPERIO · LOST HERE. FOUND TOGETHER.
</div>
""", unsafe_allow_html=True)
