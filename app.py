st.markdown("""
    <style>
    /* Main background and fonts */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Title styling */
    .main-title {
        text-align: center;
        color: white;
        font-size: 3.5rem;
        font-weight: bold;
        padding: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        animation: fadeIn 1s ease-in;
    }

    .subtitle {
        text-align: center;
        color: #f0f0f0;
        font-size: 1.3rem;
        margin-bottom: 30px;
    }

    /* Form card */
    .stForm {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }

    /* Form field labels inside 'Enter Your Health Information' */
    .stSelectbox label, 
    .stNumberInput label, 
    .stSlider label {
        color: #000000 !important;  /* Dark black color for headings */
        font-weight: bold;
    }

    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 10px 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        transition: transform 0.3s ease;
    }

    .metric-card:hover {
        transform: translateY(-5px);
    }

    /* Risk badge styling */
    .risk-badge {
        display: inline-block;
        padding: 10px 25px;
        border-radius: 25px;
        font-size: 1.2rem;
        font-weight: bold;
        margin: 10px 0;
    }

    .high-risk {
        background-color: #ff4757;
        color: white;
    }

    .low-risk {
        background-color: #2ed573;
        color: white;
    }

    /* Animation */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 1.2rem;
        font-weight: bold;
        padding: 15px 40px;
        border-radius: 30px;
        border: none;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 20px rgba(0,0,0,0.4);
    }

    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }

    /* Progress bar */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    </style>
""", unsafe_allow_html=True)
