
import streamlit as st
from database import get_reports

st.set_page_config(
    page_title="Reperio | Browse Items",
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

.page-brand {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 25px;
    font-weight: 700;
    color: #171717;
}

.page-brand span { color: #91CD00; }

.eyebrow {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 3px;
    color: #777;
}

.hero { padding: 38px 0 25px 0; }

.hero h1 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(42px, 6vw, 68px);
    line-height: 1;
    letter-spacing: -3px;
    color: #171717;
    margin: 0;
}

.hero h1 span { color: #91CD00; }

.hero p {
    color: #737373;
    font-size: 15px;
    margin-top: 15px;
}

.search-heading {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 21px;
    font-weight: 700;
}

.result-count {
    background: #F3FFD8;
    color: #547B00;
    border-radius: 30px;
    padding: 7px 13px;
    font-size: 12px;
    font-weight: 700;
    display: inline-block;
}

.item-card {
    background: #FFFFFF;
    border: 1px solid #EAEAEA;
    border-radius: 17px;
    padding: 20px;
    min-height: 245px;
    margin-bottom: 14px;
}

.item-icon {
    background: #F4F9E9;
    border-radius: 13px;
    width: 52px;
    height: 52px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 26px;
    margin-bottom: 17px;
}

.item-name {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 20px;
    font-weight: 700;
    color: #171717;
    overflow-wrap: anywhere;
    margin-bottom: 9px;
}

.item-category {
    color: #777;
    font-size: 12px;
    margin-bottom: 15px;
}

.item-location {
    color: #555;
    font-size: 13px;
    margin-top: 12px;
}

.item-description {
    color: #777;
    font-size: 13px;
    line-height: 1.5;
    margin-top: 10px;
}

.status {
    display: inline-block;
    border-radius: 20px;
    padding: 5px 10px;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 0.8px;
    text-transform: uppercase;
}

.status-lost { background: #FFF0D9; color: #A65A00; }
.status-found { background: #EFFFCA; color: #527900; }
.status-other { background: #EEEEEE; color: #555; }

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #FAFCF5;
    border-right: 1px solid #E8EEDB;
}

section[data-testid="stSidebar"] > div { padding: 25px 18px; }

[data-testid="stSidebarNav"] { display: none; }

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

section[data-testid="stSidebar"] hr { border-color: #E3EAD7; }

.stTextInput input,
.stSelectbox div[data-baseweb="select"] {
    border-radius: 10px;
}

.stButton > button {
    border-radius: 10px;
    font-weight: 700;
    min-height: 42px;
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

hr { border-color: #EEEEEE !important; }
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
<div class="page-brand">REPERIO<span>.</span></div>
<div class="eyebrow">CAMPUS LOST & FOUND</div>
<div class="hero">
    <h1>LOST <span>&</span> FOUND<span>.</span></h1>
    <p>Every item has a way back. Find what you're looking for.</p>
</div>
""", unsafe_allow_html=True)

st.divider()


reports = get_reports()

st.markdown(
    '<div class="search-heading">Find what you are looking for.</div>',
    unsafe_allow_html=True
)

st.write("")

search_col, category_col = st.columns([2, 1], gap="large")

with search_col:
    search_query = st.text_input(
        "Search",
        placeholder="🔎  Search for an item...",
        label_visibility="collapsed"
    )

with category_col:
    categories = sorted(set(
        report[3] for report in reports if report[3]
    ))

    selected_category = st.selectbox(
        "Category",
        ["All Categories"] + categories,
        label_visibility="collapsed"
    )



filtered_reports = []

for report in reports:
    item_name = report[1] or ""
    category = report[3] or ""

    matches_search = search_query.strip().lower() in item_name.lower()

    matches_category = (
        selected_category == "All Categories"
        or category == selected_category
    )

    if matches_search and matches_category:
        filtered_reports.append(report)


st.write("")

count_col, reset_col = st.columns([4, 1])

with count_col:
    st.markdown(
        f'<span class="result-count">{len(filtered_reports)} ITEMS FOUND</span>',
        unsafe_allow_html=True
    )

with reset_col:
    if st.button("Clear filters", use_container_width=True):
        st.rerun()

st.write("")



if not reports:
    st.info("No items have been reported yet. Be the first to report one!")

elif not filtered_reports:
    st.warning("No matching items found. Try another search or category.")

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

    for start in range(0, len(filtered_reports), 3):
        card_columns = st.columns(3, gap="large")

        for col, report in zip(
            card_columns,
            filtered_reports[start:start + 3]
        ):
            item_name = report[1] or "Unnamed item"
            item_type = report[2] or "Not specified"
            category = report[3] or "Other"
            location = report[4] or "Location not specified"
            description = report[5] or "No description provided."
            status = report[2] or "Unknown"
            date_reported = report[9] or "Date unavailable"

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
                    <div class="item-description">{description}</div>
                    <div class="item-category" style="margin-top:15px;">
                        REPORTED · {date_reported}
                    </div>
                </div>
                """, unsafe_allow_html=True)



st.divider()

st.markdown("""
<div style="text-align:center;color:#888;font-size:11px;
            letter-spacing:2px;padding:15px;">
    REPERIO · LOST HERE. FOUND TOGETHER.
</div>
""", unsafe_allow_html=True)

