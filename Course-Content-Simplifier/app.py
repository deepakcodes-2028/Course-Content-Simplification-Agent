import os
import re
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="AI Course Content Simplifier",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Hero Header */
    .hero-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.5rem 0 1.2rem 0;
        margin-bottom: 1rem;
        flex-wrap: wrap;
        gap: 1rem;
    }
    .hero-title-group {
        flex: 1;
        min-width: 300px;
    }
    .hero-title {
        font-size: clamp(34px, 4vw, 46px);
        font-weight: 800;
        color: #FFFFFF;
        display: flex;
        align-items: center;
        gap: 12px;
        margin: 0 0 0.4rem 0;
        line-height: 1.15;
        letter-spacing: -0.5px;
    }
    .hero-title span.grad {
        background: linear-gradient(135deg, #A78BFA 0%, #F472B6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-subtitle {
        font-size: clamp(16px, 1.8vw, 18px);
        color: #94A3B8;
        max-width: 820px;
        line-height: 1.55;
        margin: 0;
    }
    .hero-illustration {
        background: rgba(30, 41, 59, 0.4);
        border: 1px solid rgba(148, 163, 184, 0.2);
        border-radius: 16px;
        padding: 12px 18px;
        display: flex;
        align-items: center;
        gap: 12px;
        backdrop-filter: blur(8px);
    }
    .hero-illustration-text {
        font-size: 15px;
        font-weight: 600;
        color: #C084FC;
        line-height: 1.3;
    }

    /* Main Card Form Container */
    .main-form-card {
        background: rgba(19, 27, 46, 0.75);
        border: 1px solid rgba(59, 130, 246, 0.25);
        border-radius: 18px;
        padding: 24px 28px;
        margin-bottom: 24px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
    }

    /* Circular Step Badges & Headings */
    .step-header {
        display: flex;
        align-items: center;
        margin: 1.2rem 0 0.6rem 0;
    }
    .step-badge {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 34px;
        height: 34px;
        border-radius: 50%;
        background: #3B82F6;
        color: white;
        font-weight: 700;
        font-size: 16px;
        margin-right: 12px;
        flex-shrink: 0;
    }
    .step-title {
        font-size: clamp(20px, 2.2vw, 24px);
        font-weight: 700;
        color: #F8FAFC;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* Textarea Customization */
    div[data-baseweb="textarea"] textarea {
        font-size: 17px !important;
        line-height: 1.65 !important;
        min-height: 230px !important;
        border-radius: 12px !important;
        border: 1px solid rgba(148, 163, 184, 0.3) !important;
        background-color: #0E1526 !important;
        color: #F1F5F9 !important;
        padding: 16px !important;
    }
    div[data-baseweb="textarea"] textarea:focus {
        border-color: #3B82F6 !important;
        box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.25) !important;
    }

    /* Selectbox Styling */
    div[data-baseweb="select"] {
        font-size: 17px !important;
        border-radius: 10px !important;
    }

    /* Radio Buttons Sizing & Spacing */
    div[data-testid="stRadio"] label p {
        font-size: 18px !important;
        font-weight: 600 !important;
        color: #E2E8F0 !important;
        cursor: pointer;
    }
    div[data-testid="stRadio"] > div {
        gap: 28px !important;
        padding: 4px 0 8px 0;
    }

    /* Primary Simplify Button */
    div.stButton > button[kind="primary"] {
        width: 100% !important;
        border-radius: 14px !important;
        font-size: clamp(18px, 2vw, 21px) !important;
        font-weight: 800 !important;
        letter-spacing: 0.4px !important;
        padding: 0.85rem 1.8rem !important;
        background: linear-gradient(135deg, #EC4899 0%, #A855F7 50%, #6366F1 100%) !important;
        border: none !important;
        color: #FFFFFF !important;
        box-shadow: 0 6px 20px rgba(168, 85, 247, 0.4) !important;
        transition: all 0.25s ease-in-out !important;
        margin-top: 14px !important;
    }
    div.stButton > button[kind="primary"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 26px rgba(168, 85, 247, 0.6) !important;
    }

    /* Output Section Container (Full-Width) */
    .output-card-container {
        background: rgba(19, 27, 46, 0.85);
        border: 1px solid rgba(59, 130, 246, 0.3);
        border-radius: 18px;
        padding: 28px 32px;
        margin-top: 24px;
        margin-bottom: 24px;
        box-shadow: 0 12px 36px rgba(0, 0, 0, 0.3);
        width: 100%;
    }
    .output-header-title {
        font-size: clamp(24px, 2.5vw, 28px);
        font-weight: 800;
        color: #FFFFFF;
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 16px;
    }

    /* Section Card Containers */
    .section-card {
        background: rgba(30, 41, 59, 0.6);
        border: 1px solid rgba(148, 163, 184, 0.2);
        border-radius: 14px;
        padding: 22px 26px;
        margin-bottom: 20px;
        width: 100%;
    }
    .section-card-title {
        font-size: 21px;
        font-weight: 700;
        color: #F8FAFC;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .section-card-body {
        font-size: 18px;
        line-height: 1.75;
        color: #E2E8F0;
    }
    .section-card-body p {
        font-size: 18px !important;
        line-height: 1.75 !important;
        color: #E2E8F0 !important;
        margin-bottom: 8px;
    }
    .section-card-body li {
        font-size: 18px !important;
        line-height: 1.7 !important;
        color: #CBD5E1 !important;
        margin-bottom: 6px;
    }

    /* Analogy Callout Card */
    .analogy-box {
        background: linear-gradient(135deg, rgba(234, 179, 8, 0.12), rgba(249, 115, 22, 0.12));
        border-left: 4px solid #F59E0B;
        border-radius: 0 14px 14px 0;
        padding: 20px 24px;
        margin-bottom: 20px;
        width: 100%;
    }
    .analogy-title {
        font-size: 20px;
        font-weight: 700;
        color: #FBBF24;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .analogy-text {
        font-size: 18px;
        line-height: 1.75;
        color: #FEF3C7;
    }

    /* Revision Banner Card */
    .revision-box {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.14), rgba(6, 182, 212, 0.14));
        border: 1px solid rgba(16, 185, 129, 0.35);
        border-radius: 14px;
        padding: 20px 24px;
        margin-bottom: 20px;
        width: 100%;
    }
    .revision-title {
        font-size: 20px;
        font-weight: 700;
        color: #34D399;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .revision-text {
        font-size: 18px;
        line-height: 1.7;
        color: #D1FAE5;
    }

    /* Sidebar Styling */
    .sidebar-title {
        font-size: 22px;
        font-weight: 800;
        color: #FFFFFF;
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 2px;
    }
    .sidebar-sub {
        font-size: 15px;
        color: #94A3B8;
        margin-bottom: 16px;
    }
    .status-card {
        background: rgba(30, 41, 59, 0.6);
        border: 1px solid rgba(148, 163, 184, 0.2);
        border-radius: 12px;
        padding: 14px 16px;
        margin-bottom: 16px;
    }
    .status-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 6px;
    }
    .status-badge-green {
        background: rgba(16, 185, 129, 0.2);
        color: #34D399;
        font-size: 12px;
        font-weight: 700;
        padding: 2px 8px;
        border-radius: 10px;
        border: 1px solid rgba(16, 185, 129, 0.4);
    }
    .status-badge-yellow {
        background: rgba(245, 158, 11, 0.2);
        color: #FBBF24;
        font-size: 12px;
        font-weight: 700;
        padding: 2px 8px;
        border-radius: 10px;
        border: 1px solid rgba(245, 158, 11, 0.4);
    }
    .nav-pill-active {
        background: #2563EB;
        color: white;
        padding: 10px 14px;
        border-radius: 10px;
        font-weight: 600;
        font-size: 16px;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .nav-pill-inactive {
        color: #94A3B8;
        padding: 10px 14px;
        border-radius: 10px;
        font-weight: 500;
        font-size: 16px;
        margin-bottom: 16px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .sidebar-footer {
        margin-top: 40px;
        font-size: 14px;
        color: #64748B;
        display: flex;
        align-items: center;
        gap: 6px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

SAMPLE_PRESETS = {
    "-- Select a sample topic (or write your own) --": "",
    "🔬 Biology: Cellular Respiration & ATP Synthesis": (
        "Cellular respiration is the biological process by which cells convert biochemical energy "
        "from nutrients, primarily glucose, into adenosine triphosphate (ATP), and then release waste products. "
        "The catabolic reactions involved in respiration include glycolysis, the citric acid cycle, and oxidative phosphorylation. "
        "During this process, energy is captured to phosphorylate adenosine diphosphate (ADP) into ATP, "
        "providing the essential chemical energy required for vital cellular work and metabolic activities."
    ),
    "💻 Computer Science: Virtual Memory & Paging Mechanisms": (
        "Virtual memory decouples the programmer's logical view of memory from physical RAM "
        "by utilizing hardware memory management units (MMU) and paging algorithms. The logical "
        "address space is partitioned into uniform contiguous blocks called pages, which are "
        "mapped onto physical memory page frames via multi-level page tables. When a thread "
        "references a valid address whose corresponding page is non-resident in physical RAM, "
        "a page fault hardware interrupt is asserted, triggering the operating system kernel "
        "to execute page replacement policies (such as LRU or Clock) to evict a victim page, "
        "read the missing block from auxiliary storage, and update the Translation Lookaside Buffer (TLB)."
    ),
    "⚛️ Physics: Quantum Superposition & Wavefunction Collapse": (
        "In quantum mechanics, quantum superposition is a fundamental principle stating that any two or more "
        "quantum states can be added together ('superposed') and the result will be another valid quantum state. "
        "Conversely, every quantum state can be represented as a sum of two or more other distinct states. "
        "A particle exists in all possible states simultaneously until it is measured. Upon physical observation, "
        "the wavefunction collapses into a definite single state according to the probabilistic Born rule."
    ),
    "📈 Economics: Monetary Policy, Inflation & Interest Rates": (
        "Monetary policy is the policy adopted by the monetary authority of a nation to control the money supply "
        "and interest rates. When inflation escalates beyond sustainable economic targets, central banks raise policy "
        "rates and restrict lending capacity. Higher borrowing costs curb commercial credit creation, reduce "
        "consumer discretionary spending, and cool aggregate market demand to bring core consumer prices back into equilibrium."
    ),
}

env_api_key = os.getenv("WATSONX_API_KEY", "").strip()
env_project_id = os.getenv("WATSONX_PROJECT_ID", "").strip()
env_url = os.getenv("WATSONX_URL", "https://us-south.ml.cloud.ibm.com").strip()
env_model_id = os.getenv("WATSONX_MODEL_ID", "ibm/granite-13b-instruct-v2").strip()

with st.sidebar:
    st.markdown("<div class='sidebar-title'>🎓 Student Dashboard</div>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-sub'>AI-Powered Course Assistant</div>", unsafe_allow_html=True)

    has_live_credentials = bool(env_api_key and env_project_id)

    if has_live_credentials:
        st.markdown(
            """
            <div class='status-card'>
                <div class='status-header'>
                    <span style='font-weight: 700; color: #F1F5F9; font-size: 15px;'>🟢 Live IBM Granite Mode</span>
                    <span class='status-badge-green'>Connected</span>
                </div>
                <div style='font-size: 14px; color: #94A3B8; line-height: 1.4;'>
                    Using IBM watsonx.ai for real-time AI generation.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class='status-card'>
                <div class='status-header'>
                    <span style='font-weight: 700; color: #F1F5F9; font-size: 15px;'>🟡 Demo Mode Active</span>
                    <span class='status-badge-yellow'>Offline</span>
                </div>
                <div style='font-size: 14px; color: #94A3B8; line-height: 1.4;'>
                    Using the built-in educational engine.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div class='nav-pill-active'>🏠 Course Simplifier</div>", unsafe_allow_html=True)
    st.markdown("<div class='nav-pill-inactive'>📖 Saved Results</div>", unsafe_allow_html=True)

    with st.expander("⚙️ Advanced Settings", expanded=False):
        st.markdown("<div style='font-size: 16px; font-weight: 700; margin-bottom: 8px;'>AI Model Options</div>", unsafe_allow_html=True)

        granite_models = [
            "ibm/granite-13b-instruct-v2",
            "ibm/granite-3-8b-instruct",
            "ibm/granite-3-2b-instruct",
            "ibm/granite-20b-multilingual",
        ]
        default_model_idx = 0
        if env_model_id in granite_models:
            default_model_idx = granite_models.index(env_model_id)

        model_id = st.selectbox(
            "IBM Granite Model",
            granite_models,
            index=default_model_idx,
            help="Certified IBM Granite model tuned for educational explanations.",
        )

        max_tokens = st.slider("Max Output Tokens", min_value=300, max_value=2048, value=1024, step=64)
        decoding = st.selectbox("Decoding Method", ["greedy", "sample"], index=0)
        repetition_penalty = st.slider("Repetition Penalty", min_value=1.0, max_value=1.5, value=1.1, step=0.05)

        with st.expander("🔐 Developer Configuration", expanded=False):
            st.caption("Credentials are normally loaded from .env. You can optionally override them here for testing:")
            override_api_key = st.text_input("watsonx.ai API Key", value="", type="password")
            override_project_id = st.text_input("watsonx.ai Project ID", value="")
            override_url = st.text_input("watsonx.ai Region URL", value=env_url)

    active_api_key = override_api_key.strip() if ('override_api_key' in locals() and override_api_key.strip()) else env_api_key
    active_project_id = override_project_id.strip() if ('override_project_id' in locals() and override_project_id.strip()) else env_project_id
    active_url = override_url.strip() if ('override_url' in locals() and override_url.strip()) else env_url
    use_live_model = bool(active_api_key and active_project_id)

    st.markdown("<div class='sidebar-footer'>Powered by <b>IBM</b></div>", unsafe_allow_html=True)

col_hero, col_illo = st.columns([4, 1.2])

with col_hero:
    st.markdown(
        """
        <div class="hero-container">
            <div class="hero-title-group">
                <h1 class="hero-title">
                    🎓 AI Course Content <span class="grad">Simplifier</span>
                </h1>
                <p class="hero-subtitle">
                    Transform dense academic lectures, textbook chapters, and research notes into clear, 
                    understandable study material tailored to your proficiency level — powered by <b>IBM Granite</b>.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col_illo:
    st.markdown(
        """
        <div style="text-align: right; padding-top: 10px;">
            <div class="hero-illustration">
                <span style="font-size: 32px;">📖</span>
                <div class="hero-illustration-text">
                    Learn Smarter<br><span style="color: #94A3B8; font-size: 13px;">Not Harder</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<div class='main-form-card'>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="step-header">
        <span class="step-badge">1</span>
        <h2 class="step-title">📖 Choose Sample Content</h2>
    </div>
    """,
    unsafe_allow_html=True,
)

col_preset, col_clear = st.columns([4.2, 1])
with col_preset:
    selected_preset = st.selectbox(
        "Select sample topic:",
        list(SAMPLE_PRESETS.keys()),
        index=0,
        label_visibility="collapsed",
    )
with col_clear:
    clear_button = st.button("🗑️ Clear", use_container_width=True)

if "content_input" not in st.session_state:
    st.session_state["content_input"] = ""

if clear_button:
    st.session_state["content_input"] = ""
elif selected_preset and SAMPLE_PRESETS[selected_preset]:
    st.session_state["content_input"] = SAMPLE_PRESETS[selected_preset]

st.markdown(
    """
    <div class="step-header">
        <span class="step-badge">2</span>
        <h2 class="step-title">📝 Enter Your Course Content</h2>
    </div>
    """,
    unsafe_allow_html=True,
)

content = st.text_area(
    "Course content textarea:",
    value=st.session_state["content_input"],
    height=240,
    placeholder="Paste your lecture notes, syllabus, unit notes, or research excerpt here...",
    label_visibility="collapsed",
)
st.session_state["content_input"] = content

curr_text = content.strip()
word_count = len(curr_text.split()) if curr_text else 0
char_count = len(curr_text)
col_cnt_left, col_cnt_right = st.columns([1, 1])
with col_cnt_right:
    st.markdown(
        f"<div style='text-align: right; color: #64748B; font-size: 15px; font-weight: 500; padding: 4px 2px;'>"
        f"{char_count}/2000 characters · {word_count} words</div>",
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="step-header">
        <span class="step-badge">3</span>
        <h2 class="step-title">🎯 Choose Your Learning Level</h2>
    </div>
    <div style="font-size: 17px; color: #94A3B8; margin-bottom: 8px;">Choose your preferred learning level:</div>
    """,
    unsafe_allow_html=True,
)

level = st.radio(
    "Choose your preferred learning level:",
    ["Beginner", "Intermediate", "Advanced", "Expert"],
    horizontal=True,
    label_visibility="collapsed",
)

level_descriptions = {
    "Beginner": "🧒 **Beginner**: High school or newcomer. Everyday vocabulary, relatable analogies, zero unexplained jargon.",
    "Intermediate": "📗 **Intermediate**: Undergraduate student. Explains underlying mechanisms clearly while contextualizing key terms.",
    "Advanced": "🔬 **Advanced**: Senior student or researcher. Maintains academic rigor, multi-step mechanisms, and formal nomenclature.",
    "Expert": "🎓 **Expert**: Domain specialist. High-density distillation, formal boundary conditions, and executive brevity.",
}
st.markdown(f"<div style='font-size: 16px; color: #94A3B8; margin-top: 4px;'>{level_descriptions[level]}</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
run_button = st.button("✨ Simplify My Content", type="primary", use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)


def build_prompt(text: str, target_level: str) -> str:
    """Builds a strict prompt instructing IBM Granite to focus ONLY on the user's course content."""
    level_guidelines = {
        "Beginner": (
            "- Reframe the explanation for someone completely new to the topic.\n"
            "- Use simple everyday conversational language and a relatable real-life analogy.\n"
            "- Strictly avoid unexplained technical jargon; translate every complex concept into plain terms."
        ),
        "Intermediate": (
            "- Tailor the explanation for an undergraduate learner with foundational knowledge.\n"
            "- Use standard technical terminology, but clarify key mechanisms and operational concepts.\n"
            "- Maintain clear structured paragraphs explaining cause-and-effect relationships."
        ),
        "Advanced": (
            "- Structure the explanation for an advanced student or academic practitioner.\n"
            "- Maintain rigorous technical depth, formal mechanisms, and domain-specific vocabulary.\n"
            "- Connect underlying principles to broader theoretical frameworks and applications."
        ),
        "Expert": (
            "- Deliver a dense, precise, and highly concise distillation for domain experts.\n"
            "- Retain all scientific, mathematical, and architectural terminology without dilution.\n"
            "- Focus on executive takeaways, critical boundaries, and nuanced mechanisms."
        ),
    }

    instructions = level_guidelines.get(target_level, level_guidelines["Intermediate"])

    return (
        "You are an AI Course Content Simplifier.\n"
        "Analyze ONLY the course content provided by the user below.\n"
        "Do not introduce unrelated projects, agents, technologies, or topics.\n"
        "Return structured educational content based solely on the provided input.\n\n"
        f"Target Audience Level: {target_level}\n"
        f"Pedagogical Guidelines:\n{instructions}\n\n"
        "Original Course Content:\n"
        f'"""\n{text}\n"""\n\n'
        "Instructions: Output the actual content directly in these exact sections without markdown code blocks, placeholder brackets, or meta-commentary:\n\n"
        "### 📄 Simple Explanation\n"
        f"A cohesive explanation of the provided content rewritten strictly for {target_level} level.\n\n"
        "### 🔑 Key Concepts\n"
        "• Core concept 1 from the provided content\n"
        "• Core concept 2 from the provided content\n"
        "• Core concept 3 from the provided content\n\n"
        "### 📌 Important Points\n"
        "• Key takeaway or rule 1 from the provided content\n"
        "• Key takeaway or rule 2 from the provided content\n"
        "• Key takeaway or rule 3 from the provided content\n\n"
        "### 💡 Examples\n"
        "A relatable analogy or practical example directly illustrating the provided topic.\n\n"
        "### 📚 Quick Revision\n"
        "A crisp 1 to 2 sentence executive revision summary of the provided topic."
    )


def sanitize_ai_output(text: str) -> str:
    """Removes any prompt bracketed placeholders, dummy stems, and stray template tags."""
    cleaned = re.sub(
        r"\[(?:Provide|Point\s*\d+|Term\s*\d+|Plain-language|Insert|Your|A crisp|Write)[^\]]*\]",
        "",
        text,
        flags=re.IGNORECASE,
    )
    cleaned = re.sub(r"^\s*-\s*$\n", "", cleaned, flags=re.MULTILINE)
    cleaned = re.sub(r"\.{3,}", ".", cleaned)
    return cleaned.strip()


def call_granite(
    prompt: str,
    api_key: str,
    project_id: str,
    url: str,
    model_id: str,
    max_tokens: int = 1024,
    decoding_method: str = "greedy",
    rep_penalty: float = 1.1,
) -> str:
    """Calls IBM Granite models via the official ibm-watsonx-ai SDK."""
    from ibm_watsonx_ai import Credentials
    from ibm_watsonx_ai.foundation_models import ModelInference

    credentials = Credentials(url=url.strip(), api_key=api_key.strip())

    params = {
        "decoding_method": decoding_method,
        "max_new_tokens": max_tokens,
        "min_new_tokens": 50,
        "repetition_penalty": rep_penalty,
    }

    model = ModelInference(
        model_id=model_id.strip(),
        credentials=credentials,
        project_id=project_id.strip(),
        params=params,
    )

    response = model.generate_text(prompt=prompt)
    if isinstance(response, str):
        return response.strip()
    return str(response).strip()


def demo_simplify(text: str, target_level: str) -> str:
    """
    Dynamic educational simplifier strictly derived from user's input.
    Generates level-calibrated explanation, key concepts, points, analogy,
    and quick revision without any hard-coded unrelated project text.
    """
    clean_text = text.strip()
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", clean_text) if len(s.strip()) > 3]
    first_sentence = sentences[0].rstrip(".") if sentences else clean_text
    second_sentence = sentences[1].rstrip(".") if len(sentences) > 1 else ""

    # Detect domain keywords in user input to craft topic-specific analogies
    lower_text = clean_text.lower()
    if any(k in lower_text for k in ["respiration", "glucose", "atp", "mitochondria", "cell"]):
        analogy = (
            "Think of glucose like food in a storage pantry or crude fuel, and ATP like portable rechargeable batteries. "
            "Your cells cannot run machinery directly on raw food, so cellular respiration breaks down the glucose "
            "to charge up thousands of tiny ATP batteries that power every action in your body."
        )
    elif any(k in lower_text for k in ["memory", "paging", "page", "ram", "mmu", "operating system", "cache"]):
        analogy = (
            "Think of physical RAM like your immediate desktop workspace and virtual memory like a giant filing cabinet nearby. "
            "Whenever you need a document (page) that is not currently on your desk, the system pauses for a second (page fault), "
            "fetches the file from the cabinet, and places it neatly on your desk so work can continue seamlessly."
        )
    elif any(k in lower_text for k in ["quantum", "superposition", "wavefunction", "state", "particle"]):
        analogy = (
            "Think of a rapidly spinning coin on a table: while spinning, it is neither purely heads nor tails, "
            "but a blend of both possibilities at the same time (superposition). Only when you slap your hand down "
            "to stop it (measurement) does it suddenly choose one definite face."
        )
    elif any(k in lower_text for k in ["inflation", "monetary", "interest", "bank", "currency", "price"]):
        analogy = (
            "Think of the economy like a car engine running hot: raising interest rates acts like gently tapping the brakes. "
            "It makes borrowing more expensive, which cools down rapid spending and brings overheated prices back to normal speed."
        )
    else:
        analogy = (
            f"Think of this process like a well-organized factory line: raw inputs ({first_sentence[:60]}...) are received, "
            "systematically refined through coordinated steps, and delivered as high-value, reliable outputs for immediate use."
        )

    if target_level == "Beginner":
        explanation = (
            f"In simple everyday terms: {first_sentence}. "
            "Instead of getting confused by complex technical terms, the key idea is that the system takes starting materials "
            f"and transforms them into a useful form. {second_sentence + '.' if second_sentence else ''} "
            "This ensures that all essential tasks get the power and resources they need without any wasted effort."
        )
    elif target_level == "Intermediate":
        explanation = (
            f"This topic explains how: {first_sentence}. "
            f"The underlying mechanism functions through clear operational stages. {second_sentence + '.' if second_sentence else ''} "
            "By systematically converting starting substrates through dedicated pathways, the system maintains metabolic balance, "
            "delivers reliable energy or state transitions, and supports ongoing operational stability."
        )
    elif target_level == "Advanced":
        explanation = (
            f"At an advanced academic level, this represents a coordinated transformation mechanism: {clean_text} "
            "The operational throughput relies on continuous gradient maintenance and targeted feedback loops, "
            "preventing entropy loss and ensuring high thermodynamic or structural efficiency."
        )
    else:  # Expert
        explanation = (
            f"Technical distillation: {clean_text} "
            "The process adheres strictly to governing conservation principles and boundary conditions, "
            "enabling optimal free-energy coupling and deterministic state transitions at minimal dissipation."
        )

    concepts = [
        f"**Core Process**: {first_sentence}.",
    ]
    if second_sentence:
        concepts.append(f"**Operational Mechanism**: {second_sentence}.")
    else:
        concepts.append("**Functional Role**: Transforms essential inputs into high-utility, ready-to-use biological or technical energy.")
    concepts.append(f"**Comprehension Focus**: Calibrated specifically for {target_level} learners to emphasize cause-and-effect understanding.")

    points = [
        f"The primary driver is the systematic conversion of starting components ({first_sentence[:70]}...).",
        "Each stage in the pathway is tightly regulated to prevent resource waste and maintain equilibrium.",
        "Essential foundational knowledge frequently tested in academic exams and applied coursework.",
    ]

    revision = f"Remember: {first_sentence}. This conversion is the essential foundation for all downstream work."

    return (
        "### 📄 Simple Explanation\n"
        f"{explanation}\n\n"
        "### 🔑 Key Concepts\n"
        + "\n".join([f"• {item}" for item in concepts])
        + "\n\n"
        "### 📌 Important Points\n"
        + "\n".join([f"• {item}" for item in points])
        + "\n\n"
        "### 💡 Examples\n"
        f"{analogy}\n\n"
        "### 📚 Quick Revision\n"
        f"{revision}"
    )


def extract_section(markdown_text: str, *header_keywords: str) -> str:
    """Extracts a section from markdown text matching any of the header keywords."""
    for kw in header_keywords:
        pattern = rf"(?:^|\n)#{1,4}\s*.*{re.escape(kw)}.*?\n(.*?)(?=\n#{1,4}\s+|\Z)"
        match = re.search(pattern, markdown_text, flags=re.DOTALL | re.IGNORECASE)
        if match and match.group(1).strip():
            return match.group(1).strip()
    return ""


if not run_button:
    st.markdown("<div class='output-card-container'>", unsafe_allow_html=True)
    st.markdown("<div class='output-header-title'><span>📖</span> Simplified Content</div>", unsafe_allow_html=True)
    st.markdown(
        "<div style='color: #94A3B8; font-size: 17px; padding: 6px 0;'>"
        "Your simplified content will appear here after processing..."
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)
else:
    clean_input = content.strip()
    if not clean_input:
        st.warning("⚠️ Please enter or select course content to simplify.")
    elif len(clean_input) < 15:
        st.warning("⚠️ The input content is too short. Please paste at least one complete academic sentence.")
    else:
        with st.spinner(f"Simplifying for {level} level using {'IBM Granite' if use_live_model else 'Educational Engine'}..."):
            prompt = build_prompt(clean_input, level)
            error_message = None

            if use_live_model:
                try:
                    result_text = call_granite(
                        prompt=prompt,
                        api_key=active_api_key,
                        project_id=active_project_id,
                        url=active_url,
                        model_id=model_id,
                        max_tokens=max_tokens,
                        decoding_method=decoding,
                        rep_penalty=repetition_penalty,
                    )
                except Exception as ex:
                    error_message = str(ex)
                    st.warning("⚠️ Live Granite call encountered an issue. Using built-in educational engine.")
                    result_text = demo_simplify(clean_input, level)
            else:
                result_text = demo_simplify(clean_input, level)

        result_text = sanitize_ai_output(result_text)

        simple_explanation = extract_section(result_text, "Simple Explanation", "Explanation")
        key_concepts = extract_section(result_text, "Key Concepts", "Core Concepts")
        important_points = extract_section(result_text, "Important Points", "Points", "Key Takeaways")
        examples = extract_section(result_text, "Examples", "Analogy", "Practical Example")
        quick_revision = extract_section(result_text, "Quick Revision", "Revision", "Summary")

        if not simple_explanation and not key_concepts and not important_points:
            simple_explanation = result_text

        orig_words = len(clean_input.split())
        simp_words = len(result_text.split())
        read_time = max(1, round(simp_words / 150))
        engine_label = f"IBM Granite ({model_id.split('/')[-1]})" if (use_live_model and not error_message) else "Educational Engine"

        st.markdown("<div class='output-card-container'>", unsafe_allow_html=True)

        st.markdown("<div class='output-header-title'><span>📖</span> Simplified Content</div>", unsafe_allow_html=True)
        st.markdown(
            f"<div style='color: #94A3B8; font-size: 16px; margin-top: -8px; margin-bottom: 16px;'>"
            f"Tailored for <b>{level}</b> proficiency · Generated by {engine_label} · {simp_words} words (~{read_time} min read)"
            f"</div>",
            unsafe_allow_html=True,
        )
        st.markdown("<hr style='border: 0; height: 1px; background: rgba(148, 163, 184, 0.2); margin: 0 0 20px 0;'>", unsafe_allow_html=True)

        if simple_explanation:
            st.markdown(
                f"""
                <div class="section-card">
                    <div class="section-card-title">📄 Simple Explanation</div>
                    <div class="section-card-body">{simple_explanation}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        if key_concepts:
            st.markdown(
                f"""
                <div class="section-card">
                    <div class="section-card-title">🔑 Key Concepts</div>
                    <div class="section-card-body">{key_concepts}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        if important_points:
            st.markdown(
                f"""
                <div class="section-card">
                    <div class="section-card-title">📌 Important Points</div>
                    <div class="section-card-body">{important_points}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        if examples:
            st.markdown(
                f"""
                <div class="analogy-box">
                    <div class="analogy-title">💡 Examples</div>
                    <div class="analogy-text">{examples}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        if quick_revision:
            st.markdown(
                f"""
                <div class="revision-box">
                    <div class="revision-title">📚 Quick Revision</div>
                    <div class="revision-text">{quick_revision}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("<br>", unsafe_allow_html=True)
        col_d1, col_d2 = st.columns(2)

        study_notes_md = (
            f"# Course Content Simplification Notes\n\n"
            f"- **Target Level:** {level}\n"
            f"- **Engine:** {engine_label}\n"
            f"- **Original Words:** {orig_words}\n"
            f"- **Simplified Words:** {simp_words}\n\n"
            f"---\n\n"
            f"## Original Course Material\n{clean_input}\n\n"
            f"---\n\n"
            f"## Simplified Content\n\n"
            f"{result_text}\n"
        )

        with col_d1:
            st.download_button(
                label="📥 Download Study Notes (.md)",
                data=study_notes_md,
                file_name=f"course_notes_{level.lower()}.md",
                mime="text/markdown",
                use_container_width=True,
            )
        with col_d2:
            st.download_button(
                label="📄 Download Plain Text (.txt)",
                data=result_text,
                file_name=f"course_notes_{level.lower()}.txt",
                mime="text/plain",
                use_container_width=True,
            )

        with st.expander("🔍 Compare with Original Course Material", expanded=False):
            st.markdown("##### Original Course Input:")
            st.info(clean_input)

        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.divider()
st.markdown(
    "<div style='text-align: center; color: #64748B; font-size: 15px; padding: 6px 0;'>"
    "AI Course Content Simplifier · Powered by IBM Granite"
    "</div>",
    unsafe_allow_html=True,
)
