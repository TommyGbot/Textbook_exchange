import streamlit as st
from streamlit.components.v1 import iframe

st.set_page_config(page_title="Mustang Books", page_icon="📚", layout="wide")

DONATE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScrXtPw9QgsmMme4X3-abRSI0fgCc7Ea5Q79m_AMDL51NL8VA/viewform?embedded=true"
REQUEST_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfp7rLxZz8xps7CC9UkaVRXNxXt30dzSPqdJOMqKI3U-7ezlQ/viewform?embedded=true"

BOOKS = [
    {
        "id": "1",
        "title": "Miller & Freund's Probability & Statistics for Engineers",
        "author": "Richard A. Johnson",
        "course": "IME 503",
        "dept": "IME",
        "edition": "9th",
        "subject": "Statistics",
        "condition": "Good",
        "available": True,
    },
    {
        "id": "2",
        "title": "The Goal",
        "author": "Dr. Eliyahu Goldratt",
        "course": "IME 410/420",
        "dept": "IME",
        "edition": "Graphic Novel",
        "subject": "Industrial Engineering",
        "condition": "Good",
        "available": True,
    },
    {
        "id": "3",
        "title": "Calculus",
        "author": "Thomas",
        "course": "MATH 141",
        "dept": "MATH",
        "edition": "8th",
        "subject": "Math",
        "condition": "Poor",
        "available": True,
    },
    {
        "id": "4",
        "title": "Calculus",
        "author": "James Stewart",
        "course": "MATH 143",
        "dept": "MATH",
        "edition": "8th",
        "subject": "Math",
        "condition": "Good",
        "available": True,
    },
       {
        "id": "5",
        "title": "Introduction to Fluid Mechanics",
        "author": "Robert W. Fox",
        "course": "ME 341",
        "dept": "ME",
        "edition": "6th",
        "subject": "Mechanical Engineering",
        "condition": "Good",
        "available": True,
    },
    {
        "id": "6",
        "title": "Miller & Freund's Probability and Statistics For Engineers",
        "author": "Richard A. Johnson",
        "course": "IME 503",
        "dept": "IME",
        "edition": "8th",
        "subject": "Statistics",
        "condition": "Great",
        "available": True,
    },
    {
        "id": "7",
        "title": "Probability and Statistics for Engineers",
        "author": "Miller & Freund",
        "course": "IME 503",
        "dept": "IME",
        "edition": "8th",
        "subject": "Statistics",
        "condition": "Good",
        "available": True,
    },
]

st.markdown(
    """
    <style>
    :root {
      --primary: #154734;
      --primary-dark: #0f3326;
      --accent: #b9975b;
      --muted: #667085;
      --border: #e4e7ec;
      --card: #ffffff;
      --bg: #f8faf9;
    }
    .stApp { background: var(--bg); }
    header[data-testid="stHeader"] { background: rgba(248,250,249,0.85); }
    .hero {
      background: linear-gradient(135deg, var(--primary), var(--primary-dark));
      color: white;
      border-radius: 0 0 28px 28px;
      padding: 3.2rem 2.2rem;
      margin: -1rem -1rem 2rem -1rem;
    }
    .eyebrow { font-size: .78rem; letter-spacing: .14em; text-transform: uppercase; opacity: .72; }
    .hero h1 { font-size: clamp(2.2rem, 6vw, 4.5rem); line-height: 1.02; margin: .5rem 0 1rem 0; font-weight: 550; }
    .hero p { opacity: .78; font-size: 1.05rem; max-width: 680px; }
    .metric-wrap { display: flex; gap: 2rem; flex-wrap: wrap; margin-top: 2rem; }
    .metric b { font-size: 2rem; display:block; }
    .metric span { opacity:.68; font-size:.9rem; }
    .step-card, .book-card, .info-card, .footer-card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 1.1rem;
      box-shadow: 0 8px 24px rgba(16,24,40,.04);
    }
    .book-card { min-height: 245px; display: flex; flex-direction: column; justify-content: space-between; }
    .book-title { font-size: 1.05rem; font-weight: 700; margin: .8rem 0 .2rem 0; color: #101828; }
    .muted { color: var(--muted); }
    .pill { display:inline-block; border-radius:999px; padding:.22rem .55rem; font-size:.75rem; font-weight:700; margin-right:.35rem; }
    .pill-available { background:#e8f5ef; color:#087443; }
    .pill-claimed { background:#eef2f6; color:#475467; }
    .pill-condition { background:#fff4d6; color:#93370d; }
    .course { color: var(--primary); background:#e8f5ef; padding:.18rem .45rem; border-radius:6px; font-family: monospace; font-weight:700; }
    .cta { background:#edf7f2; border:1px solid #cfe8db; border-radius:18px; padding:1.5rem; }
    .footer { border-top:1px solid var(--border); padding-top:1.5rem; margin-top:2.5rem; color:var(--muted); font-size:.9rem; }
    div[data-testid="stTabs"] button { font-size: 1rem; }
    </style>
    """,
    unsafe_allow_html=True,
)


def book_card(book: dict) -> None:
    status_class = "pill-available" if book["available"] else "pill-claimed"
    status = "Available" if book["available"] else "Claimed"
    claim = (
        f"""
        <a href="{REQUEST_FORM_URL}" target="_blank" 
           style="color:var(--primary);font-weight:700;margin-top:.75rem;display:inline-block;text-decoration:none;">
           Claim →
        </a>
        """
        if book["available"]
        else ""
    )

    st.markdown(
        f"""
        <div class="book-card">
          <div>
            <span class="pill {status_class}">{status}</span>
            <span class="pill pill-condition">{book['condition']}</span>
            <div class="book-title">{book['title']}</div>
            <div class="muted">{book['author']}</div>
            <div class="muted" style="font-size:.86rem;margin-top:.25rem;">{book.get('edition','')} edition</div>
          </div>
          <div style="border-top:1px solid var(--border);padding-top:.8rem;margin-top:1rem;">
            <span class="course">{book['course']}</span>
            <div class="muted" style="font-size:.86rem;margin-top:.45rem;">{book['subject']}</div>
            {claim}
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_form(src: str, title: str) -> None:
    st.markdown(f"### {title}")
    iframe(src, height=820, scrolling=True)


available_count = sum(book["available"] for book in BOOKS)

tab_browse, tab_donate, tab_request = st.tabs(["Browse Books", "Donate", "Request"])

with tab_browse:
    st.markdown(
        f"""
        <section class="hero">
          <div class="eyebrow">Cal Poly · San Luis Obispo</div>
          <h1>Textbooks that keep<br>circulating.</h1>
          <p>Students donate books at quarter-end. Mustangs claim them at no cost.</p>
          <div class="metric-wrap">
            <div class="metric"><b>{available_count}</b><span>books available now</span></div>
            <div class="metric"><b>500+</b><span>books circulated</span></div>
            <div class="metric"><b>$50k+</b><span>estimated savings</span></div>
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns(3)
    steps = [
        ("01", "Donate at quarter-end", "Fill out our Google Form on campus during scheduled collection windows."),
        ("02", "Inventory managed weekly", "Our team updates availability. Books are stored off-campus between events."),
        ("03", "Claim what you need", "Browse below and submit a request. First come, first served at no cost."),
    ]
    for col, (step, heading, body) in zip(cols, steps):
        with col:
            st.markdown(f"<div class='step-card'><b>{step}</b><h4>{heading}</h4><p class='muted'>{body}</p></div>", unsafe_allow_html=True)

    st.markdown("### Browse inventory")
    search = st.text_input("Search title, author, course, or subject", placeholder="Search textbooks…")
    departments = ["All"] + sorted({book["dept"] for book in BOOKS})
    dept = st.radio("Department", departments, horizontal=True)

    q = search.lower().strip()
    filtered = []
    for book in BOOKS:
        haystack = " ".join(str(book.get(key, "")) for key in ["title", "author", "course", "subject"]).lower()
        if (not q or q in haystack) and (dept == "All" or book["dept"] == dept):
            filtered.append(book)

    st.caption(f"{len(filtered)} {'book' if len(filtered) == 1 else 'books'} found" + (f" in {dept}" if dept != "All" else ""))

    if filtered:
        rows = [filtered[i:i+3] for i in range(0, len(filtered), 3)]
        for row in rows:
            cols = st.columns(3)
            for col, book in zip(cols, row):
                with col:
                    book_card(book)
    else:
        st.info("No books found. Try a different search term or department, or submit a request.")

    st.markdown(
        """
        <div class="cta">
          <h3>Done with a textbook?</h3>
          <p class="muted">Donate at the end of this quarter during scheduled drop-off windows on campus.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with tab_donate:
    st.markdown("<section class='hero'><div class='eyebrow'>Mustang Books</div><h1>Donate your textbooks.</h1></section>", unsafe_allow_html=True)
    st.success("Donations are accepted during Finals Week and the first two weeks of each quarter at scheduled on-campus drop-off locations.")
    render_form(DONATE_FORM_URL, "Donate a Textbook")

with tab_request:
    st.markdown("<section class='hero'><div class='eyebrow'>Mustang Books</div><h1>Request a title.</h1></section>", unsafe_allow_html=True)
    st.success("Submit a request for any title. The team processes requests weekly and will email you when a copy is ready for pickup.")
    render_form(REQUEST_FORM_URL, "Request a Textbook")

st.markdown(
    """
    <div class="footer">
      <b>Mustang Books</b><br>
      A student-run initiative to promote sustainability and affordability across Cal Poly departments.<br><br>
      Contact: mustangbooks@calpoly.edu · Mon-Fri, 9 AM-5 PM · Cal Poly San Luis Obispo<br>
      © 2025 Mustang Books
    </div>
    """,
    unsafe_allow_html=True,
)
