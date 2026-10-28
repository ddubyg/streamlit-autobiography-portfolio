from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image, ImageDraw, ImageFont, ImageOps

# =====================================================================
# EDIT THIS BLOCK: all personal content lives here
# =====================================================================
NAME = "Ernjen Crisdel B. Largo"
FIRST_NAME = "Ernjen"
PROGRAM = "BS Computer Science"
YEAR = "3rd Year"
SECTION = "F1"
SCHOOL = "Cebu Institute of Technology - University"
TAGLINE = "I build games, web apps, and small AI systems. Right now I'm a third year CS student who likes shipping things people can actually run."

BIO = (
    "I'm a third year Computer Science student at Cebu Institute of Technology - University. "
    "I mostly write Java, Kotlin, and C++, and I use HTML, CSS, and JavaScript when a project "
    "needs to live on the web. I enjoy the part of programming where an idea turns into "
    "something other people can click, play, or use."
)

BACKGROUND = (
    "I got into computers through games. At some point I stopped only playing them and started "
    "wondering how they were made. That curiosity pushed me into Computer Science, where I learned "
    "that the fun part is not just writing code, it is making something other people use."
)

# Self-assessment out of 100. Change these to your honest numbers.
SKILLS = pd.DataFrame(
    {
        "Skill": ["Java", "HTML / CSS", "Game Design", "JavaScript", "Kotlin", "C++", "Python", "AI / Search"],
        "Level": [85, 80, 80, 75, 70, 70, 70, 65],
        "Category": ["Languages", "Web", "Games", "Web", "Languages", "Languages", "Languages", "AI"],
    }
)

PROJECTS = [
    {
        "title": "Sabay",
        "type": "Web Development",
        "desc": "A student activity-matching platform that helps students find people for studying, sports, gaming, and other campus activities.",
        "role": "Developer",
        "tools": ["HTML", "CSS", "JavaScript"],
        "outcome": "Working web platform for matching students by activity.",
    },
    {
        "title": "Fuzzy Traffic Light System",
        "type": "Artificial Intelligence",
        "desc": "A fuzzy-logic traffic controller that adjusts traffic-light behavior based on traffic conditions.",
        "role": "Developer",
        "tools": ["Python", "Fuzzy Logic"],
        "outcome": "Controller that changes signal timing as traffic changes.",
    },
    {
        "title": "Tic-Tac-Toe with Minimax",
        "type": "Game Development / AI",
        "desc": "A Windows desktop game with an AI opponent that uses Minimax to evaluate possible moves.",
        "role": "Developer",
        "tools": ["Minimax", "Desktop GUI"],
        "outcome": "Playable desktop game with an AI opponent that picks the best move.",
    },
    {
        "title": "Roblox Co-op Game",
        "type": "Game Development",
        "desc": "A multiplayer game concept inspired by Gamble With Your Friends, built around debt, pressure, and cooperative gameplay.",
        "role": "Game Director and Playtester",
        "tools": ["Roblox Studio", "Luau"],
        "outcome": "Concept stage. A playable build is still in progress.",
    },
    {
        "title": "ClassSync",
        "type": "Desktop App",
        "desc": "A JavaFX desktop app that helps university group projects stay accountable.",
        "role": "Developer",
        "tools": ["Java", "JavaFX"],
        "outcome": "Capstone desktop application.",
    },
]

MILESTONES = [
    ("Started at CIT-U", "Began the BS Computer Science program."),
    ("Learned to build for real", "Moved from class exercises to apps and games I could run and show."),
    ("AI coursework", "Built a Minimax game opponent and a fuzzy-logic traffic controller."),
    ("Team roles", "Took on game director and playtester duties on a Roblox project."),
    ("Now", "Third year, working on ClassSync and this portfolio."),
]

ACCENT = "#5cd6a9"

# =====================================================================
# PAGE SETUP
# =====================================================================
st.set_page_config(page_title=f"{NAME} | Portfolio", page_icon=":material/terminal:", layout="wide")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "favs" not in st.session_state:
    st.session_state.favs = []

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

.stApp { font-family: 'Inter', system-ui, sans-serif; }
#MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent; }
[data-testid="stToolbar"], [data-testid="stAppDeployButton"], .stDeployButton { display: none; }
[data-testid="stSidebar"] a { color: #b4bccb; text-decoration: none; }
[data-testid="stSidebar"] a:hover { color: ACCENT; }
[data-testid="stExpander"] { margin-top: 1.2rem; }
.block-container { max-width: 1060px; padding-top: 3.5rem; padding-bottom: 4rem; }

p, li, label { line-height: 1.65; }
a { color: ACCENT; text-decoration: none; }
a:hover { text-decoration: underline; }

.eyebrow { font-family: 'JetBrains Mono', monospace; font-size: .82rem; color: ACCENT; letter-spacing: .04em; margin-bottom: 1rem; }
.hero-name { font-size: clamp(2.4rem, 5vw, 3.9rem); font-weight: 700; letter-spacing: -0.035em; line-height: 1.04; margin: 0 0 1.1rem 0; }
.hero-tag { font-size: 1.15rem; color: #9aa3b2; max-width: 34rem; margin-bottom: 1.8rem; }
a.btn, a.btn:hover, a.btn:visited { text-decoration: none !important; }
.btn { display: inline-block; padding: .62rem 1.15rem; border-radius: 8px; font-weight: 500; font-size: .92rem; margin-right: .6rem; }
.btn-solid { background: ACCENT; color: #0d1015 !important; }
.btn-solid:hover { text-decoration: none; filter: brightness(1.08); }
.btn-ghost { border: 1px solid #2c3441; color: #e6e8ec !important; }
.btn-ghost:hover { text-decoration: none; border-color: ACCENT; }

.sec { display: flex; align-items: center; gap: .9rem; margin: 5rem 0 1.8rem 0; }
.sec .num { font-family: 'JetBrains Mono', monospace; color: ACCENT; font-size: .95rem; }
.sec h2 { font-size: 1.55rem; font-weight: 600; letter-spacing: -0.015em; margin: 0; padding: 0; }
.sec .rule { flex: 1; height: 1px; background: #232a35; }

.kicker { font-family: 'JetBrains Mono', monospace; font-size: .72rem; color: ACCENT; text-transform: uppercase; letter-spacing: .08em; }
.card-title { font-size: 1.22rem; font-weight: 600; letter-spacing: -0.01em; margin: .25rem 0 .6rem 0; }
.muted { color: #9aa3b2; }
.label { font-size: .8rem; color: #7c8596; margin: .8rem 0 .3rem 0; }
.chip { display: inline-block; font-family: 'JetBrains Mono', monospace; font-size: .72rem; padding: 3px 9px; border: 1px solid #2c3441; border-radius: 6px; color: #b4bccb; margin: 0 6px 6px 0; }

[data-testid="stImage"] img { border-radius: 14px; }
[data-testid="stMetricValue"] { font-weight: 600; letter-spacing: -0.02em; }
[data-testid="stMetricLabel"] p { color: #8d96a6; }
.timeline-item { border-left: 1px solid #2c3441; padding: 0 0 1.25rem 1.1rem; position: relative; }
.timeline-item::before { content: ''; position: absolute; left: -5px; top: .45rem; width: 9px; height: 9px; border-radius: 50%; background: ACCENT; }
.timeline-item b { display: block; font-weight: 600; }
.timeline-item span { color: #9aa3b2; font-size: .95rem; }
</style>
""".replace("ACCENT", ACCENT)
st.markdown(CSS, unsafe_allow_html=True)


def section(num: str, title: str, anchor: str):
    st.markdown(
        f'<div class="sec" id="{anchor}"><span class="num">{num}</span><h2>{title}</h2><span class="rule"></span></div>',
        unsafe_allow_html=True,
    )


def chips(items):
    return "".join(f'<span class="chip">{i}</span>' for i in items)


def load_photo():
    base = Path(__file__).parent
    for name in ("profile.jpg", "profile.jpeg", "profile.png", "profile.JPG", "profile.PNG"):
        path = base / name
        if path.exists():
            img = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
            return ImageOps.fit(img, (900, 1000), centering=(0.5, 0.3))
    return None


def placeholder(initials: str) -> Image.Image:
    img = Image.new("RGB", (900, 1000), "#141922")
    d = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", 280)
    except OSError:
        font = ImageFont.load_default()
    d.text((450, 500), initials, fill=ACCENT, font=font, anchor="mm")
    return img


def toggle_fav(title: str):
    if title in st.session_state.favs:
        st.session_state.favs.remove(title)
    else:
        st.session_state.favs.append(title)


# =====================================================================
# SIDEBAR
# =====================================================================
with st.sidebar:
    st.markdown(f"**{NAME}**")
    st.caption(f"{PROGRAM}  \n{YEAR}, Section {SECTION}")
    st.markdown("[About](#about)  \n[Autobiography](#autobiography)  \n[Skills](#skills)  \n[Projects](#projects)  \n[Contact](#contact)")
    st.divider()
    st.caption("Display options")
    layout_mode = st.radio("Project layout", ["Cards", "Table"], horizontal=True)
    show_outcomes = st.checkbox("Show project outcomes", value=True)

# =====================================================================
# HERO
# =====================================================================
hero_l, hero_r = st.columns([1.5, 1], gap="large", vertical_alignment="center")

with hero_l:
    st.markdown(
        f"""
        <div class="eyebrow">{PROGRAM}  /  {YEAR}  /  Section {SECTION}</div>
        <h1 class="hero-name">{NAME}</h1>
        <p class="hero-tag">{TAGLINE}</p>
        <a class="btn btn-solid" href="#projects">View projects</a>
        <a class="btn btn-ghost" href="#contact">Get in touch</a>
        """,
        unsafe_allow_html=True,
    )

with hero_r:
    photo = load_photo()
    if photo is not None:
        st.image(photo, width="stretch")
    else:
        st.image(placeholder("EL"), width="stretch")
        st.caption("Placeholder. Put profile.jpg in the same folder as app.py.")

st.write("")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Year level", "3rd")
m2.metric("Projects", len(PROJECTS))
m3.metric("Languages", 5, help="Java, Kotlin, C++, JavaScript, Python")
m4.metric("Section", SECTION)

# =====================================================================
# 01 ABOUT
# =====================================================================
section("01", "About", "about")
a1, a2 = st.columns([1.5, 1], gap="large")
with a1:
    st.write(BIO)
    st.write(
        "Outside of coursework I direct and playtest a Roblox game, so I tend to think about the code "
        "and the player at the same time."
    )
with a2:
    st.markdown(
        f"""
        <div class="label">Studying</div>
        <div>{PROGRAM}</div>
        <div class="label">School</div>
        <div>{SCHOOL}</div>
        <div class="label">Year and section</div>
        <div>{YEAR}, Section {SECTION}</div>
        <div class="label">Works in</div>
        <div>{chips(["Java", "Kotlin", "C++", "JavaScript", "Python"])}</div>
        """,
        unsafe_allow_html=True,
    )

# =====================================================================
# 02 AUTOBIOGRAPHY
# =====================================================================
section("02", "Autobiography", "autobiography")
tab_bg, tab_edu, tab_int, tab_mile = st.tabs(["Background", "Education", "Interests", "Milestones"])

with tab_bg:
    st.write(BACKGROUND)

with tab_edu:
    st.markdown(f"**{SCHOOL}**")
    st.write(f"{PROGRAM}, {YEAR}, Section {SECTION}.")
    st.write(
        "Coursework so far has covered object-oriented programming, data structures, AI search and logic, "
        "web development, and desktop application development."
    )

with tab_int:
    picks = st.multiselect(
        "Highlight interests",
        ["Game development", "Web development", "Artificial intelligence", "Desktop apps", "Playtesting", "Data and analytics"],
        default=["Game development", "Web development", "Artificial intelligence"],
    )
    st.markdown(chips(picks) if picks else '<span class="muted">Nothing selected.</span>', unsafe_allow_html=True)

with tab_mile:
    st.write("")
    html = "".join(f'<div class="timeline-item"><b>{t}</b><span>{d}</span></div>' for t, d in MILESTONES)
    st.markdown(html, unsafe_allow_html=True)

# =====================================================================
# 03 SKILLS
# =====================================================================
section("03", "Skills", "skills")
st.write(
    "Java, Kotlin, and C++ are what I reach for most. HTML, CSS, and JavaScript cover the web side. "
    "The ratings are my own self-assessment out of 100."
)

all_cats = sorted(SKILLS["Category"].unique())
chosen = st.pills("Category", all_cats, selection_mode="multi", default=all_cats)
filtered = SKILLS[SKILLS["Category"].isin(chosen)] if chosen else SKILLS.iloc[0:0]

s1, s2 = st.columns([1, 1.2], gap="large")
with s1:
    st.dataframe(
        filtered.sort_values("Level", ascending=False),
        hide_index=True,
        width="stretch",
        column_config={"Level": st.column_config.ProgressColumn("Level", min_value=0, max_value=100, format="%d")},
    )
with s2:
    if filtered.empty:
        st.info("Pick at least one category.")
    else:
        st.bar_chart(filtered, x="Skill", y="Level", color=ACCENT, horizontal=True, sort="-Level", height=300, x_label="", y_label="Self-rated level")

# =====================================================================
# 04 PROJECTS
# =====================================================================
section("04", "Projects", "projects")
types = ["All types"] + sorted({p["type"] for p in PROJECTS})
f_col, _ = st.columns([1, 2])
chosen_type = f_col.selectbox("Filter by type", types, label_visibility="collapsed")
shown = [p for p in PROJECTS if chosen_type == "All types" or p["type"] == chosen_type]

if layout_mode == "Table":
    st.dataframe(
        pd.DataFrame(
            [
                {"Project": p["title"], "Type": p["type"], "Role": p["role"], "Tools": ", ".join(p["tools"]), "Outcome": p["outcome"]}
                for p in shown
            ]
        ),
        hide_index=True,
        width="stretch",
    )
else:
    cols = st.columns(2, gap="medium")
    for i, p in enumerate(shown):
        with cols[i % 2]:
            with st.container(border=True, height=470 if show_outcomes else 390):
                st.markdown(
                    f"""
                    <div class="kicker">{p["type"]}</div>
                    <div class="card-title">{p["title"]}</div>
                    <div class="muted">{p["desc"]}</div>
                    <div class="label">My role</div>
                    <div>{p["role"]}</div>
                    <div class="label">Built with</div>
                    <div>{chips(p["tools"])}</div>
                    {f'<div class="label">Outcome</div><div>{p["outcome"]}</div>' if show_outcomes else ""}
                    """,
                    unsafe_allow_html=True,
                )
                is_fav = p["title"] in st.session_state.favs
                st.write("")
                st.button(
                    "Remove favorite" if is_fav else "Favorite",
                    key=f"fav_{p['title']}",
                    on_click=toggle_fav,
                    args=(p["title"],),
                    icon=":material/star:" if is_fav else ":material/star_outline:",
                    type="primary" if is_fav else "secondary",
                )

if st.session_state.favs:
    st.caption("Your favorites: " + ", ".join(st.session_state.favs))

summary = f"{NAME}\n{PROGRAM}, {YEAR}, Section {SECTION}\n{SCHOOL}\n\n{BIO}\n\nProjects\n" + "\n".join(
    f"- {p['title']} ({p['type']}): {p['desc']} Role: {p['role']}. Tools: {', '.join(p['tools'])}." for p in PROJECTS
)
st.write("")
st.download_button("Download summary", summary, file_name="ernjen_largo_summary.txt", icon=":material/download:")

# =====================================================================
# 05 CONTACT
# =====================================================================
section("05", "Contact", "contact")
c1, c2 = st.columns([1.25, 1], gap="large")

with c1:
    with st.form("contact_form", clear_on_submit=True):
        who = st.text_input("Name")
        email = st.text_input("Email")
        topic = st.selectbox("Topic", ["Feedback on the portfolio", "Project collaboration", "Just saying hi"])
        rating = st.slider("How would you rate this site?", 1, 5, 5)
        msg = st.text_area("Message", height=110)
        ok_reply = st.checkbox("You can reply to my email")
        sent = st.form_submit_button("Send message", type="primary")

    if sent:
        if not who.strip() or not msg.strip():
            st.error("Please add your name and a message.")
        else:
            st.session_state.messages.append(
                {
                    "Time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "Name": who,
                    "Email": email,
                    "Topic": topic,
                    "Rating": rating,
                    "Message": msg,
                    "Reply OK": ok_reply,
                }
            )
            st.toast("Message sent")
            st.success(f"Thanks, {who}. Your message was received.")

with c2:
    st.markdown(
        f"""
        <div class="label" style="margin-top:0">Open to</div>
        <div>Feedback on my projects, collaborations, and conversations about games, web, and AI.</div>
        <div class="label">Based at</div>
        <div>{SCHOOL}</div>
        """,
        unsafe_allow_html=True,
    )
    with st.expander(f"Messages this session ({len(st.session_state.messages)})"):
        if st.session_state.messages:
            df = pd.DataFrame(st.session_state.messages)
            st.dataframe(df[["Time", "Name", "Topic", "Rating"]], hide_index=True, width="stretch")
            st.caption(f"Average rating: {np.mean(df['Rating']):.1f} / 5")
            st.download_button("Download as CSV", df.to_csv(index=False), file_name="messages.csv", mime="text/csv")
        else:
            st.caption("Nothing yet.")

st.markdown(
    f'<div class="muted" style="margin-top:4rem;font-size:.85rem">{NAME}  /  {PROGRAM}, {YEAR}, Section {SECTION}  /  CSIT 349 Applied AI  /  Built with Streamlit</div>',
    unsafe_allow_html=True,
)