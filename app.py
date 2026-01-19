import streamlit as st
import requests
import streamlit.components.v1 as components

API_BASE = "http://127.0.0.1:8000/verify"

st.set_page_config(
    page_title="TruthScan",
    layout="centered"
)

# ---------- GAUGE ----------
def animated_gauge(value, label, color):
    radius = 45
    circumference = 2 * 3.1416 * radius
    offset = circumference * (1 - value / 100)

    return f"""
    <div style="text-align:center">
      <svg width="120" height="120">
        <!-- background -->
        <circle cx="60" cy="60" r="{radius}"
          stroke="#1f2937"
          stroke-width="10"
          fill="none"/>

        <!-- progress -->
        <circle cx="60" cy="60" r="{radius}"
          stroke="{color}"
          stroke-width="10"
          fill="none"
          stroke-dasharray="{circumference}"
          stroke-dashoffset="{circumference}"
          stroke-linecap="round"
          transform="rotate(-90 60 60)"
          style="animation: sweep 1.2s ease-out forwards;
                 stroke-dashoffset: {offset};"/>

        <!-- value -->
        <text x="50%" y="54%" text-anchor="middle"
          fill="#e5e7eb" font-size="18" font-weight="600">
          {value}%
        </text>
      </svg>

      <div style="color:#9ca3af;font-size:14px;margin-top:6px">
        {label}
      </div>
    </div>

    <style>
    @keyframes sweep {{
      from {{
        stroke-dashoffset: {circumference};
      }}
      to {{
        stroke-dashoffset: {offset};
      }}
    }}
    </style>
    """

# ---------- HEADER ----------
st.title("🛡️ TruthScan")
st.caption("AI-powered credibility analysis — surfaces risk, not truth")

analysis_type = st.radio(
    "Analysis type",
    ["Text Claim", "Image Verification"],
    horizontal=True
)

# ---------- TEXT ----------
if analysis_type == "Text Claim":
    text = st.text_area(
        "Paste a statement, headline, or claim",
        height=120
    )

    if st.button("Analyze credibility"):
        if not text.strip():
            st.warning("Enter some text.")
        else:
            with st.spinner("Analyzing…"):
                res = requests.post(
                    f"{API_BASE}/text",
                    json={"text": text},
                    timeout=30
                )

            if res.status_code != 200:
                st.error(res.text)
            else:
                data = res.json()

                # Verdict badge
                st.markdown(
                    f"""
                    <div style="
                        background:#065f46;
                        padding:12px;
                        border-radius:8px;
                        font-weight:600;
                        text-align:center;
                        color:#ecfdf5;
                        margin-bottom:20px;">
                        {data["verdict"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                col1, col2 = st.columns(2)

                with col1:
                    components.html(
                            animated_gauge(
                            int(data["confidence"] * 100),
                            "Model confidence",
                            "#22c55e"
                        ),
                    height=180,
                )


                with col2:
                    components.html(
                        animated_gauge(
                            int(data["risk_score"] * 100),
                            "Risk score",
                            "#f59e0b" if data["risk_score"] < 0.4 else "#ef4444"
                        ),
                        height=180,
                    )
                st.subheader("Why this was flagged")
                for f in data.get("flags", []):
                    st.write("•", f)

# ---------- IMAGE ----------
else:
    image = st.file_uploader(
        "Upload image",
        type=["jpg", "jpeg", "png"]
    )

    if image and st.button("Analyze image"):
        with st.spinner("Analyzing image…"):
            res = requests.post(
                f"{API_BASE}/image",
                files={"image": image},
                timeout=60
            )

        if res.status_code != 200:
            st.error(res.text)
        else:
            data = res.json()

            st.markdown(
                f"""
                <div style="
                    background:#1e3a8a;
                    padding:12px;
                    border-radius:8px;
                    font-weight:600;
                    text-align:center;
                    color:#dbeafe;
                    margin-bottom:20px;">
                    {data["verdict"]}
                </div>
                """,
                unsafe_allow_html=True
            )

            col1, col2 = st.columns(2)

            with col1:
                    components.html(
                        animated_gauge(
                        int(data["confidence"] * 100),
                            "Model confidence",
                        "#3b82f6"  # blue
                    ),
                height=180,
                )

            with col2:
                components.html(
                    animated_gauge(
                        int(data["risk_score"] * 100),
                        "Risk score",
                        "#ef4444" if data["risk_score"] > 0.5 else "#f59e0b"
                    ),
                height=180,
            )

            st.subheader("Image flags")
            for f in data.get("flags", []):
                st.write("•", f)
