
import streamlit as st
from datetime import date
from database import insert_reports

st.set_page_config(
    page_title="Reperio | Report an Item",
    page_icon="📦",
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
    max-width: 1050px;
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
    font-size: clamp(40px, 6vw, 62px);
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

.form-heading {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 21px;
    font-weight: 700;
    color: #171717;
}

.form-caption {
    color: #777;
    font-size: 13px;
    margin-bottom: 20px;
}

/* Form surface */
div[data-testid="stForm"] {
    background: #FFFFFF;
    border: 1px solid #EAEAEA;
    border-radius: 18px;
    padding: 25px;
}

.stTextInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"],
.stDateInput input {
    border-radius: 10px;
}

.stButton > button,
div[data-testid="stFormSubmitButton"] button {
    border-radius: 10px;
    min-height: 45px;
    font-weight: 700;
}

div[data-testid="stFormSubmitButton"] button {
    background: #C6FF00;
    color: #171717;
    border: 1px solid #C6FF00;
}

div[data-testid="stFormSubmitButton"] button:hover {
    background: #B2E900;
    border-color: #B2E900;
    color: #171717;
}

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
        <div style="font-weight:700;color:#405E00;">Found something?</div>
        <div style="font-size:12px;color:#62733D;margin-top:5px;">
            Report it and help someone get it back.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.caption("REPERIO · LOST HERE. FOUND TOGETHER.")



st.markdown("""
<div class="page-brand">REPERIO<span>.</span></div>
<div class="eyebrow">CAMPUS LOST & FOUND</div>
<div class="hero">
    <h1>REPORT AN <span>ITEM.</span></h1>
    <p>Every report brings a lost belonging one step closer to its owner.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

st.markdown(
    '<div class="form-heading">Item details</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="form-caption">Fill in the details below to submit your report.</div>',
    unsafe_allow_html=True
)


with st.form("report_item_form"):

    st.markdown("#### About the item")

    item_name = st.text_input(
        "Item Name *",
        placeholder="e.g. Black Wallet"
    )

    col1, col2 = st.columns(2)

    with col1:
        item_type = st.selectbox(
            "Report Type *",
            ["Lost", "Found"]
        )

    with col2:
        category = st.selectbox(
            "Category *",
            [
                "Electronics",
                "Accessories",
                "Books & Stationery",
                "Clothing",
                "ID Cards",
                "Other"
            ]
        )

    location = st.text_input(
        "Location *",
        placeholder="Where was it lost or found?"
    )

    description = st.text_area(
        "Description *",
        placeholder="Describe the item and any identifying details...",
        height=120
    )

    st.markdown("#### Your contact details")

    col3, col4 = st.columns(2)

    with col3:
        contact_name = st.text_input(
            "Your Name *",
            placeholder="Enter your name"
        )

    with col4:
        contact_phone = st.text_input(
            "Contact Phone Number *",
            placeholder="Enter your phone number"
        )

    date_reported = st.date_input(
        "Date Reported",
        value=date.today()
    )

    st.caption("* Required fields")

    submitted = st.form_submit_button(
        "Submit Report →",
        use_container_width=True
    )



if submitted:

    if not item_name.strip():
        st.error("Please enter the item name.")

    elif not location.strip():
        st.error("Please enter the location.")

    elif not description.strip():
        st.error("Please enter a description.")

    elif not contact_name.strip():
        st.error("Please enter your name.")

    elif not contact_phone.strip():
        st.error("Please enter your contact phone number.")

    else:
        resolution_code = insert_reports(
            item_name.strip(),
            item_type,
            category,
            location.strip(),
            description.strip(),
            contact_name.strip(),
            contact_phone.strip(),
            "Open",
            date_reported.isoformat()
        )

        if resolution_code:
            st.markdown("""
            <style>
            .success-wrap {
                display: flex;
                flex-direction: column;
                align-items: center;
                padding: 22px 0;
                animation: fadeIn 0.5s ease-out;
            }

            .check-circle {
                width: 62px;
                height: 62px;
                border: 2px solid #B7F000;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                animation: circleIn 0.55s ease-out forwards;
            }

            .check {
                color: #8DBB00;
                font-size: 34px;
                font-weight: 500;
                animation: checkIn 0.35s ease-out 0.35s both;
            }

            .success-text {
                margin-top: 14px;
                color: #26321A;
                font-size: 17px;
                font-weight: 600;
                animation: fadeIn 0.5s ease-out 0.45s both;
            }

            @keyframes circleIn {
                from { transform: scale(0.75); opacity: 0; }
                to { transform: scale(1); opacity: 1; }
            }

            @keyframes checkIn {
                from { opacity: 0; transform: scale(0.7); }
                to { opacity: 1; transform: scale(1); }
            }

            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            </style>

            <div class="success-wrap">
                <div class="check-circle">
                    <span class="check">✓</span>
                </div>
                <div class="success-text">Report submitted successfully</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### Your resolution code")
            st.code(resolution_code)

            if item_type == "Found":
                st.caption("Save this code. You will need it after handing the item over to its owner.")
            else:
                st.caption("Save this code. You will need it after recovering your lost item.")

        else:
            st.warning(
                "This exact report already exists. Please check your submitted reports."
            )

st.divider()

if st.button("← Back to Homepage"):
    st.switch_page("app.py")
