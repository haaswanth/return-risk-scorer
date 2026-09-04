import streamlit as st
import pandas as pd
import joblib
from datetime import date


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Return Risk Scorer",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #f8fafc 0%, #eef2ff 100%);
}

/* MAIN TITLE */

.main-title {
    font-size: 44px;
    font-weight: 800;
    color: #111827;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 18px;
    color: #475569;
    margin-bottom: 30px;
}


/* HEADINGS */

.section-title {
    font-size: 26px;
    font-weight: 750;
    color: #111827;
    margin-top: 25px;
    margin-bottom: 15px;
}

h1, h2, h3, h4, h5, h6 {
    color: #111827 !important;
}


/* LABELS */

label {
    color: #334155 !important;
}


/* INFORMATION CARDS */

.info-card {
    padding: 20px;
    border-radius: 16px;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    margin-bottom: 15px;
}

.metric-title {
    font-size: 14px;
    color: #64748b;
    margin-bottom: 5px;
}

.metric-value {
    font-size: 25px;
    font-weight: 700;
    color: #111827;
}


/* RISK CARDS */

.risk-high {
    padding: 30px;
    border-radius: 20px;
    background: #fee2e2;
    border: 2px solid #fca5a5;
    text-align: center;
}

.risk-medium {
    padding: 30px;
    border-radius: 20px;
    background: #fef3c7;
    border: 2px solid #fcd34d;
    text-align: center;
}

.risk-low {
    padding: 30px;
    border-radius: 20px;
    background: #dcfce7;
    border: 2px solid #86efac;
    text-align: center;
}

.risk-title {
    font-size: 30px;
    font-weight: 800;
    color: #111827;
}

.risk-probability {
    font-size: 44px;
    font-weight: 800;
    color: #111827;
    margin: 10px 0;
}


/* BUTTON */

.stButton > button {
    width: 100%;
    border-radius: 12px;
    height: 55px;
    font-size: 18px;
    font-weight: 700;
}


/* SIDEBAR */

[data-testid="stSidebar"] {
    background-color: #ffffff;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] h4 {
    color: #111827 !important;
}

[data-testid="stSidebar"] p {
    color: #334155 !important;
}


/* METRICS */

[data-testid="stMetricLabel"] {
    color: #64748b !important;
}

[data-testid="stMetricValue"] {
    color: #111827 !important;
}


/* FOOTER */

.footer {
    text-align: center;
    color: #475569;
    font-size: 15px;
    line-height: 1.8;
    padding: 20px;
}

.footer-title {
    color: #111827;
    font-size: 18px;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD MODEL AND SCALER
# =========================================================

@st.cache_resource
def load_model():

    model = joblib.load("final_random_forest.pkl")
    scaler = joblib.load("scaler.pkl")

    return model, scaler


try:

    model, scaler = load_model()

except Exception as e:

    st.error("❌ Model or scaler file could not be loaded.")

    st.info(
        "Make sure these files are present in the same folder as app.py:\n\n"
        "• final_random_forest.pkl\n"
        "• scaler.pkl"
    )

    st.stop()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 📦 Return Risk Scorer")

    st.markdown("---")

    st.markdown("### 🎯 About")

    st.write(
        "An AI-powered machine learning system that "
        "predicts the probability of an e-commerce order being returned."
    )

    st.markdown("---")

    st.markdown("### 🤖 Model")

    st.write("**Tuned Random Forest Classifier**")

    st.markdown("---")

    st.markdown("### 📊 Features")

    st.write("**12 final features**")

    st.markdown("---")

    st.markdown("### 🚦 Risk Levels")

    st.write("🟢 **Low Risk**")
    st.write("🟡 **Medium Risk**")
    st.write("🔴 **High Risk**")

    st.markdown("---")

    st.caption("Razorpay Buildathon Project")


# =========================================================
# MAIN HEADER
# =========================================================

st.markdown(
    '<div class="main-title">📦 Return Risk Scorer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-powered system for predicting e-commerce return risk'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# ORDER INFORMATION
# =========================================================

st.markdown(
    '<div class="section-title">📝 Order Information</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


# =========================================================
# PRODUCT DETAILS
# =========================================================

with col1:

    st.markdown("#### 💰 Product Details")

    product_price = st.number_input(
        "Product Price (₹)",
        min_value=0.0,
        value=500.0,
        step=100.0
    )

    order_quantity = st.number_input(
        "Order Quantity",
        min_value=1,
        value=1,
        step=1
    )

    discount_applied = st.number_input(
        "Discount Applied (₹)",
        min_value=0.0,
        value=0.0,
        step=10.0
    )


# =========================================================
# CUSTOMER DETAILS
# =========================================================

with col2:

    st.markdown("#### 👤 Customer Details")

    user_age = st.number_input(
        "User Age",
        min_value=1,
        max_value=100,
        value=25,
        step=1
    )

    order_value = st.number_input(
        "Order Value (₹)",
        min_value=0.0,
        value=500.0,
        step=100.0
    )

    order_date = st.date_input(
        "Order Date",
        value=date.today()
    )


# =========================================================
# CATEGORY DETAILS
# =========================================================

with col3:

    st.markdown("#### 📦 Category Details")

    product_category = st.selectbox(
        "Product Category",
        [
            "Books",
            "Clothing",
            "Electronics",
            "Toys"
        ]
    )

    st.markdown("#### 📅 Selected Date")

    st.info(
        f"📅 {order_date.strftime('%d %B %Y')}"
    )


# =========================================================
# INPUT SUMMARY
# =========================================================

st.markdown(
    '<div class="section-title">📋 Input Summary</div>',
    unsafe_allow_html=True
)

sum1, sum2, sum3, sum4 = st.columns(4)

with sum1:

    st.metric(
        "Product Price",
        f"₹{product_price:,.0f}"
    )

with sum2:

    st.metric(
        "Quantity",
        order_quantity
    )

with sum3:

    st.metric(
        "Order Value",
        f"₹{order_value:,.0f}"
    )

with sum4:

    st.metric(
        "Category",
        product_category
    )


# =========================================================
# PREDICTION BUTTON
# =========================================================

st.markdown("---")

predict_button = st.button(
    "🔍 Predict Return Risk"
)


# =========================================================
# PREDICTION
# =========================================================

if predict_button:

    # =====================================================
    # DATE FEATURES
    # =====================================================

    year = order_date.year
    month = order_date.month
    day = order_date.day


    # =====================================================
    # ONE-HOT ENCODING
    # =====================================================

    category_books = 1 if product_category == "Books" else 0

    category_clothing = 1 if product_category == "Clothing" else 0

    category_electronics = 1 if product_category == "Electronics" else 0

    category_toys = 1 if product_category == "Toys" else 0


    # =====================================================
    # CREATE INPUT DATAFRAME
    # =====================================================

    input_data = pd.DataFrame(
        [[
            product_price,
            order_quantity,
            discount_applied,
            user_age,
            order_value,
            year,
            month,
            day,
            category_books,
            category_clothing,
            category_electronics,
            category_toys
        ]],
        columns=[
            "Product_Price",
            "Order_Quantity",
            "Discount_Applied",
            "User_Age",
            "Order_Value",
            "year",
            "month",
            "day",
            "Product_Category_Books",
            "Product_Category_Clothing",
            "Product_Category_Electronics",
            "Product_Category_Toys"
        ]
    )


    # =====================================================
    # SCALE INPUT
    # =====================================================

    input_scaled = scaler.transform(input_data)


    # =====================================================
    # MODEL PREDICTION
    # =====================================================

    prediction = model.predict(input_scaled)[0]


    # =====================================================
    # RETURN PROBABILITY
    # =====================================================

    probability = model.predict_proba(input_scaled)[0][1]


    # =====================================================
    # RISK LEVEL
    # =====================================================

    if probability >= 0.70:

        risk_level = "High"
        risk_emoji = "🔴"

    elif probability >= 0.40:

        risk_level = "Medium"
        risk_emoji = "🟡"

    else:

        risk_level = "Low"
        risk_emoji = "🟢"


    # =====================================================
    # PREDICTION RESULT
    # =====================================================

    st.markdown(
        '<div class="section-title">🎯 Prediction Result</div>',
        unsafe_allow_html=True
    )


    result_col1, result_col2 = st.columns([2, 1])


    # =====================================================
    # RISK RESULT
    # =====================================================

    with result_col1:

        if risk_level == "High":

            st.error(
                f"🔴 HIGH RETURN RISK\n\n"
                f"Return Probability: {probability:.1%}"
            )

        elif risk_level == "Medium":

            st.warning(
                f"🟡 MEDIUM RETURN RISK\n\n"
                f"Return Probability: {probability:.1%}"
            )

        else:

            st.success(
                f"🟢 LOW RETURN RISK\n\n"
                f"Return Probability: {probability:.1%}"
            )


    # =====================================================
    # RESULT DETAILS
    # =====================================================

    with result_col2:

        st.metric(
            "Risk Level",
            f"{risk_emoji} {risk_level}"
        )

        st.metric(
            "Product Category",
            product_category
        )

        st.metric(
            "Order Value",
            f"₹{order_value:,.0f}"
        )


    # =====================================================
    # RETURN PROBABILITY
    # =====================================================

    st.markdown(
        '<div class="section-title">📊 Return Probability</div>',
        unsafe_allow_html=True
    )

    st.progress(float(probability))

    st.markdown(
        f"### {probability:.2%} chance of return"
    )


    # =====================================================
    # RISK INTERPRETATION
    # =====================================================

    st.markdown(
        '<div class="section-title">💡 Risk Interpretation</div>',
        unsafe_allow_html=True
    )

    if risk_level == "High":

        st.error(
            "This order has a high predicted return probability. "
            "It may require additional attention or review."
        )

    elif risk_level == "Medium":

        st.warning(
            "This order has a moderate predicted return probability. "
            "Consider monitoring this order."
        )

    else:

        st.success(
            "This order has a low predicted return probability. "
            "The order appears relatively less likely to be returned."
        )


    # =====================================================
    # ORDER DETAILS
    # =====================================================

    st.markdown(
        '<div class="section-title">📦 Order Details</div>',
        unsafe_allow_html=True
    )

    detail1, detail2, detail3, detail4 = st.columns(4)

    with detail1:

        st.metric(
            "Product Price",
            f"₹{product_price:,.0f}"
        )

    with detail2:

        st.metric(
            "Quantity",
            order_quantity
        )

    with detail3:

        st.metric(
            "Discount",
            f"₹{discount_applied:,.0f}"
        )

    with detail4:

        st.metric(
            "User Age",
            user_age
        )


    # =====================================================
    # MODEL INFORMATION
    # =====================================================

    st.markdown(
        '<div class="section-title">🤖 Model Information</div>',
        unsafe_allow_html=True
    )

    model1, model2, model3 = st.columns(3)

    with model1:

        st.info(
            "🤖 Machine Learning Model\n\n"
            "Random Forest"
        )

    with model2:

        st.info(
            "📊 Input Features\n\n"
            "12 Features"
        )

    with model3:

        st.info(
            "🎯 Prediction Type\n\n"
            "Return Risk"
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <div style="
        text-align: center;
        color: #334155;
        font-size: 15px;
        line-height: 1.8;
        padding: 15px;
    ">
        📦 <b>Return Risk Scorer</b><br>
        AI-Powered E-Commerce Return Prediction<br>
        Built with Machine Learning • Random Forest<br>
        Razorpay Buildathon
    </div>
    """,
    unsafe_allow_html=True
)