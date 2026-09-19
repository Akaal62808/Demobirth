import streamlit as st
import streamlit.components.v1 as components

# =========================================================
# STREAMLIT CONFIG
# =========================================================

st.set_page_config(
    page_title="Birthday Surprise 🎂",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# STREAMLIT CSS
# =========================================================

st.markdown("""
<style>
#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

.stApp {
    background: #02030a;
}

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# CHANGE NAME HERE
# =========================================================

NAME = "Komal"


# =========================================================
# HTML
# =========================================================

html_code = f"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>Happy Birthday</title>

<style>

* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

html,
body {{
    width: 100%;
    height: 100%;
    overflow: hidden;
    background:
        radial-gradient(
            circle at center,
            #11182f 0%,
            #050611 45%,
            #010106 100%
        );
    font-family: Arial, Helvetica, sans-serif;
}}

canvas {{
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100%;
}}

#stars {{
    z-index: 1;
}}

#particles {{
    z-index: 2;
}}

#fireworks {{
    z-index: 3;
}}

#top {{
    position: fixed;
    top: 22px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 10;
    width: 95%;
    text-align: center;
    color: #ffffff;
    font-size: 13px;
    letter-spacing: 3px;
    text-shadow:
        0 0 10px #00ffff,
        0 0 25px #00ffff;
}}

#content {{
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 10;
    width: 100%;
    text-align: center;
    pointer-events: none;
}}

#countdown {{
    font-size: clamp(80px, 20vw, 190px);
    font-weight: 900;
    color: #ffffff;
    opacity: 0;
    text-shadow:
        0 0 15px #00ffff,
        0 0 35px #0088ff,
        0 0 70px #0066ff;
    transition: .5s;
}}

#title {{
    font-size: clamp(35px, 8vw, 100px);
    font-weight: 900;
    letter-spacing: 4px;
    opacity: 0;
    transform: scale(.2);
    color: #ffd700;
    text-shadow:
        0 0 10px #ffd700,
        0 0 30px #ff8c00,
        0 0 60px #ff4500;
    transition:
        opacity 1s ease,
        transform 1s ease;
}}

#title.show {{
    opacity: 1;
    transform: scale(1);
}}

#name {{
    margin-top: 15px;
    font-size: clamp(45px, 11vw, 130px);
    font-weight: 900;
    letter-spacing: 7px;

    background:
        linear-gradient(
            90deg,
            #00ffff,
            #00ff88,
            #ffd700,
            #ff8c00,
            #9d4edd,
            #00ffff
        );

    background-size: 300% 100%;

    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;

    animation: rainbow 4s linear infinite;

    opacity: 0;
    transform: translateY(40px) scale(.7);

    transition:
        opacity 1s ease,
        transform 1s ease;
}}

#name.show {{
    opacity: 1;
    transform: translateY(0) scale(1);
}}

@keyframes rainbow {{
    0% {{
        background-position: 0% 50%;
    }}

    50% {{
        background-position: 100% 50%;
    }}

    100% {{
        background-position: 0% 50%;
    }}
}}

#wish {{
    width: 90%;
    max-width: 850px;
    margin: 25px auto 0;

    color: #ffffff;

    font-size: clamp(16px, 3vw, 27px);

    line-height: 1.5;

    opacity: 0;

    transition: opacity 1s ease;

    text-shadow:
        0 0 10px #00ffff;
}}

#card {{
    position: fixed;
    left: 50%;
    top: 50%;

    transform:
        translate(-50%, -50%)
        scale(.4);

    width: min(90%, 620px);

    max-height: 82vh;

    overflow-y: auto;

    z-index: 20;

    padding: 30px 24px;

    border-radius: 28px;

    background:
        rgba(255,255,255,.08);

    border:
        1px solid
        rgba(255,255,255,.25);

    backdrop-filter: blur(18px);

    box-shadow:
        0 0 50px
        rgba(0,255,255,.25);

    text-align: center;

    opacity: 0;

    transition: 1s;
}}

#card.show {{
    opacity: 1;

    transform:
        translate(-50%, -50%)
        scale(1);
}}

#cake {{
    font-size: clamp(75px, 15vw, 140px);

    animation:
        cakeBounce 1.3s infinite;
}}

@keyframes cakeBounce {{
    0%,100% {{
        transform: translateY(0);
    }}

    50% {{
        transform: translateY(-12px);
    }}
}}

.cardTitle {{
    font-size: clamp(25px, 6vw, 52px);

    font-weight: 900;

    background:
        linear-gradient(
            90deg,
            #ffd700,
            #00ffff,
            #7cff00,
            #ff8c00
        );

    -webkit-background-clip: text;
    background-clip: text;

    color: transparent;
}}

.cardText {{
    margin-top: 18px;

    color: #ffffff;

    font-size:
        clamp(15px, 3vw, 21px);

    line-height: 1.7;
}}

#wishes {{
    margin-top: 20px;
}}

.w {{
    margin: 8px 0;
}}

#start {{
    position: fixed;

    left: 50%;
    bottom: 35px;

    transform: translateX(-50%);

    z-index: 30;

    border: none;

    border-radius: 50px;

    padding:
        15px 32px;

    background:
        linear-gradient(
            90deg,
            #00c6ff,
            #7b2ff7,
            #ff8c00
        );

    color: white;

    font-size: 16px;

    font-weight: bold;

    cursor: pointer;

    box-shadow:
        0 0 20px
        rgba(0,255,255,.5);

    transition: .3s;
}}

#start:hover {{
    transform:
        translateX(-50%)
        scale(1.08);

    box-shadow:
        0 0 40px
        rgba(0,255,255,.9);
}}

@media(max-width:600px) {{

    #top {{
        font-size: 10px;
        letter-spacing: 2px;
    }}

    #name {{
        letter-spacing: 3px;
    }}

    #card {{
        padding: 25px 17px;
    }}

    #start {{
        bottom: 20px;
        padding: 13px 24px;
        font-size: 14px;
    }}
}}

</style>

</head>

<body>

<canvas id="stars"></canvas>
<canvas id="particles"></canvas>
<canvas id="fireworks"></canvas>

<div id="top">
    ✨ A SPECIAL BIRTHDAY SURPRISE ✨
</div>

<div id="content">

    <div id="countdown">3</div>

    <div id="title">
        HAPPY BIRTHDAY
    </div>

    <div id="name">
        {NAME.upper()}
    </div>

    <div id="wish">
        Wishing you a wonderful year filled with
        happiness, success, good health and
        unforgettable memories! 🎉
    </div>

</div>


<div id="card">

    <div id="cake">
        🎂
    </div>

    <div class="cardTitle">
        HAPPY BIRTHDAY {NAME.upper()}!
    </div>

    <div class="cardText">

        <div id="wishes">

            <div class="w">
                🌟 May your days always be bright and cheerful.
            </div>

            <div class="w">
                🎯 May you achieve every goal you work for.
            </div>

            <div class="w">
                😊 May you always have plenty of reasons to smile.
            </div>

            <div class="w">
                🚀 May your dreams turn into reality.
            </div>

            <div class="w">
                🍀 May good luck always be with you.
            </div>

            <div class="w">
                📚 May you keep learning and growing.
            </div>

            <div class="w">
                🏆 May success follow you in every new journey.
            </div>

            <div class="w">
                🌈 May every challenge make you stronger.
            </div>

            <div class="w">
                ✨ May this year bring exciting new opportunities.
            </div>

            <div class="w">
                🎁 May your birthday be full of fun and laughter.
            </div>

            <div class="w">
                💫 May you create many amazing memories this year.
            </div>

            <div class="w">
                🎉 Keep smiling, keep shining and keep being awesome!
            </div>

        </div>

        <br>

        <b>
            HAVE AN AMAZING BIRTHDAY! 🎈🎂🎊
        </b>

    </div>

</div>


<button id="start">
    🎁 OPEN BIRTHDAY SURPRISE
</button>


<script>

/* =====================================================
   CANVAS
===================================================== */

const starsCanvas =
    document.getElementById("stars");

const particleCanvas =
    document.getElementById("particles");

const fireworkCanvas =
    document.getElementById("fireworks");

const sctx =
    starsCanvas.getContext("2d");

const pctx =
    particleCanvas.getContext("2d");

const fctx =
    fireworkCanvas.getContext("2d");


let W = window.innerWidth;
let H = window.innerHeight;


function resize() {{

    W = window.innerWidth;
    H = window.innerHeight;

    starsCanvas.width = W;
    starsCanvas.height = H;

    particleCanvas.width = W;
    particleCanvas.height = H;

    fireworkCanvas.width = W;
    fireworkCanvas.height = H;
}}

resize();

window.addEventListener(
    "resize",
    resize
);


/* =====================================================
   STARS
===================================================== */

const stars = [];

for(let i = 0; i < 220; i++) {{

    stars.push({{

        x: Math.random() * W,

        y: Math.random() * H,

        r: Math.random() * 2 + .3,

        speed:
            Math.random() * .6 + .1,

        alpha:
            Math.random() * .8 + .2
    }});
}}


function animateStars() {{

    sctx.clearRect(
        0,
        0,
        W,
        H
    );

    for(const s of stars) {{

        s.y += s.speed;

        if(s.y > H) {{
            s.y = 0;
            s.x = Math.random() * W;
        }}

        sctx.beginPath();

        sctx.arc(
            s.x,
            s.y,
            s.r,
            0,
            Math.PI * 2
        );

        sctx.fillStyle =
            "rgba(255,255,255," +
            s.alpha +
            ")";

        sctx.fill();
    }}

    requestAnimationFrame(
        animateStars
    );
}}

animateStars();


/* =====================================================
   FLOATING PARTICLES
===================================================== */

const particles = [];

const particleColors = [
    "#00ffff",
    "#ffd700",
    "#00ff88",
    "#9d4edd",
    "#ff8c00",
    "#ffffff"
];


for(let i = 0; i < 170; i++) {{

    particles.push({{

        x: Math.random() * W,

        y: Math.random() * H,

        size:
            Math.random() * 3 + 1,

        speed:
            Math.random() * 1.2 + .2,

        color:
            particleColors[
                Math.floor(
                    Math.random() *
                    particleColors.length
                )
            ],

        angle:
            Math.random() * Math.PI * 2
    }});
}}


function animateParticles() {{

    pctx.clearRect(
        0,
        0,
        W,
        H
    );

    for(const p of particles) {{

        p.y -= p.speed;

        p.angle += .01;

        p.x +=
            Math.sin(p.angle) * .35;

        if(p.y < -10) {{
            p.y = H + 10;
            p.x = Math.random() * W;
        }}

        pctx.beginPath();

        pctx.arc(
            p.x,
            p.y,
            p.size,
            0,
            Math.PI * 2
        );

        pctx.fillStyle = p.color;

        pctx.shadowBlur = 14;

        pctx.shadowColor = p.color;

        pctx.fill();
    }}

    pctx.shadowBlur = 0;

    requestAnimationFrame(
        animateParticles
    );
}}

animateParticles();


/* =====================================================
   FIREWORKS
===================================================== */

const fireworks = [];

const fireColors = [
    "#00ffff",
    "#ffd700",
    "#ff8c00",
    "#7cff00",
    "#9d4edd",
    "#ffffff"
];


function createFirework(x, y) {{

    const color =
        fireColors[
            Math.floor(
                Math.random() *
                fireColors.length
            )
        ];

    const count = 65;

    for(let i = 0; i < count; i++) {{

        const angle =
            Math.random() *
            Math.PI * 2;

        const speed =
            Math.random() * 5 + 2;

        fireworks.push({{

            x: x,

            y: y,

            vx:
                Math.cos(angle) *
                speed,

            vy:
                Math.sin(angle) *
                speed,

            life: 1,

            color: color
        }});
    }}
}}


function animateFireworks() {{

    fctx.fillStyle =
        "rgba(0,0,0,.16)";

    fctx.fillRect(
        0,
        0,
        W,
        H
    );

    for(
        let i = fireworks.length - 1;
        i >= 0;
        i--
    ) {{

        const p =
            fireworks[i];

        p.x += p.vx;

        p.y += p.vy;

        p.vy += .045;

        p.life -= .017;


        fctx.beginPath();

        fctx.arc(
            p.x,
            p.y,
            2.5,
            0,
            Math.PI * 2
        );

        fctx.fillStyle = p.color;

        fctx.globalAlpha =
            Math.max(
                p.life,
                0
            );

        fctx.shadowBlur = 15;

        fctx.shadowColor =
            p.color;

        fctx.fill();


        if(p.life <= 0) {{
            fireworks.splice(i, 1);
        }}
    }}

    fctx.globalAlpha = 1;

    fctx.shadowBlur = 0;

    requestAnimationFrame(
        animateFireworks
    );
}}

animateFireworks();


/* =====================================================
   ELEMENTS
===================================================== */

const start =
    document.getElementById(
        "start"
    );

const countdown =
    document.getElementById(
        "countdown"
    );

const title =
    document.getElementById(
        "title"
    );

const name =
    document.getElementById(
        "name"
    );

const wish =
    document.getElementById(
        "wish"
    );

const card =
    document.getElementById(
        "card"
    );


/* =====================================================
   COUNTDOWN
===================================================== */

function showNumber(number) {{

    countdown.innerText =
        number;

    countdown.style.opacity =
        "1";

    countdown.style.transform =
        "scale(1.15)";

    setTimeout(() => {{

        countdown.style.transform =
            "scale(1)";

    }}, 150);
}}


/* =====================================================
   START
===================================================== */

start.addEventListener(
    "click",
    function() {{

        start.style.display =
            "none";

        let number = 3;

        showNumber(number);


        const timer =
            setInterval(
                function() {{

                    number--;

                    if(number > 0) {{

                        showNumber(
                            number
                        );

                    }}
                    else {{

                        clearInterval(
                            timer
                        );

                        countdown.style.opacity =
                            "0";


                        /* TITLE */

                        setTimeout(
                            function() {{

                                title.classList.add(
                                    "show"
                                );

                            }},
                            400
                        );


                        /* NAME */

                        setTimeout(
                            function() {{

                                name.classList.add(
                                    "show"
                                );

                            }},
                            1300
                        );


                        /* WISH */

                        setTimeout(
                            function() {{

                                wish.style.opacity =
                                    "1";

                            }},
                            2300
                        );


                        /* FIREWORKS */

                        setTimeout(
                            function() {{

                                for(
                                    let i = 0;
                                    i < 12;
                                    i++
                                ){{

                                    setTimeout(
                                        function() {{

                                            createFirework(
                                                80 +
                                                Math.random() *
                                                (W - 160),

                                                100 +
                                                Math.random() *
                                                (H * .45)
                                            );

                                        }},
                                        i * 220
                                    );
                                }}

                            }},
                            2500
                        );


                        /* FINAL CARD */

                        setTimeout(
                            function() {{

                                title.style.opacity =
                                    "0";

                                name.style.opacity =
                                    "0";

                                wish.style.opacity =
                                    "0";


                                card.classList.add(
                                    "show"
                                );


                                /* BIG FINAL FIREWORK */

                                for(
                                    let i = 0;
                                    i < 20;
                                    i++
                                ){{

                                    setTimeout(
                                        function() {{

                                            createFirework(
                                                Math.random() * W,

                                                80 +
                                                Math.random() *
                                                H * .55
                                            );

                                        }},
                                        i * 180
                                    );
                                }}

                            }},
                            6500
                        );

                    }}

                }},
                1000
            );

    }};


/* =====================================================
   CONTINUOUS FINAL FIREWORKS
===================================================== */

setInterval(
    function() {{

        if(
            card.classList.contains(
                "show"
            )
        ){{

            createFirework(
                80 +
                Math.random() *
                (W - 160),

                80 +
                Math.random() *
                (H * .5)
            );
        }}

    }},
    900
);

</script>

</body>

</html>
"""


# =========================================================
# DISPLAY
# =========================================================

components.html(
    html_code,
    height=760,
    scrolling=False
)
