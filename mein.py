import streamlit as st
import streamlit.components.v1 as components

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Birthday Surprise 🎂",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CUSTOM STREAMLIT CSS
# =========================================================

st.markdown("""
<style>

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

.stApp {
    background: #02030a;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# BIRTHDAY DETAILS
# =========================================================

NAME = "Komal"


# =========================================================
# ADVANCED HTML + CSS + JAVASCRIPT
# =========================================================

html_code = f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width,
               initial-scale=1.0">

<style>

* {{
    margin:0;
    padding:0;
    box-sizing:border-box;
}}

html,body {{

    width:100%;
    height:100%;

    overflow:hidden;

    background:
        radial-gradient(
            circle at center,
            #11152b 0%,
            #050611 45%,
            #010106 100%
        );

    font-family:
        Arial,
        Helvetica,
        sans-serif;
}}


/* =====================================================
   CANVAS
===================================================== */

canvas {{

    position:absolute;

    top:0;
    left:0;

    width:100%;
    height:100%;
}}


#bgCanvas {{
    z-index:1;
}}

#particleCanvas {{
    z-index:2;
}}

#fireworkCanvas {{
    z-index:3;
}}


/* =====================================================
   CONTENT
===================================================== */

#content {{

    position:absolute;

    top:50%;
    left:50%;

    transform:
        translate(-50%,-50%);

    z-index:10;

    width:100%;

    text-align:center;

    pointer-events:none;
}}


/* =====================================================
   COUNTDOWN
===================================================== */

#countdown {{

    font-size:
        clamp(80px,18vw,190px);

    font-weight:900;

    color:#ffffff;

    text-shadow:
        0 0 10px #00ffff,
        0 0 30px #00ffff,
        0 0 70px #0066ff;

    opacity:0;

    transition:
        opacity .4s,
        transform .4s;
}}


/* =====================================================
   MAIN TITLE
===================================================== */

#title {{

    font-size:
        clamp(45px,9vw,110px);

    font-weight:900;

    letter-spacing:5px;

    color:#ffffff;

    opacity:0;

    transform:
        scale(.3);

    transition:
        all 1s cubic-bezier(.17,.67,.3,1.3);

    text-shadow:
        0 0 10px #ffd700,
        0 0 30px #ff8c00,
        0 0 60px #ff4500;
}}


#title.show {{

    opacity:1;

    transform:
        scale(1);
}}


/* =====================================================
   NAME
===================================================== */

#name {{

    margin-top:15px;

    font-size:
        clamp(50px,11vw,130px);

    font-weight:900;

    letter-spacing:8px;

    background:
        linear-gradient(
            90deg,
            #00ffff,
            #7cff00,
            #ffd700,
            #ff8c00,
            #9d4edd
        );

    -webkit-background-clip:text;

    color:transparent;

    opacity:0;

    transform:
        translateY(50px)
        scale(.7);

    transition:
        all 1.2s ease;

    filter:
        drop-shadow(
            0 0 18px
            rgba(0,255,255,.7)
        );
}}


#name.show {{

    opacity:1;

    transform:
        translateY(0)
        scale(1);
}}


/* =====================================================
   WISH
===================================================== */

#wish {{

    margin:
        25px auto 0;

    width:90%;

    max-width:900px;

    font-size:
        clamp(17px,3vw,30px);

    line-height:1.5;

    color:#ffffff;

    opacity:0;

    transition:
        opacity 1s ease;

    text-shadow:
        0 0 12px #00ffff;
}}


/* =====================================================
   FINAL CARD
===================================================== */

#card {{

    position:absolute;

    left:50%;
    top:50%;

    transform:
        translate(-50%,-50%)
        scale(.5);

    z-index:20;

    width:
        min(90%,600px);

    padding:35px 25px;

    border-radius:30px;

    background:
        rgba(255,255,255,.07);

    border:
        1px solid
        rgba(255,255,255,.2);

    backdrop-filter:
        blur(20px);

    box-shadow:
        0 0 50px
        rgba(0,255,255,.25);

    text-align:center;

    opacity:0;

    pointer-events:none;

    transition:
        all 1s ease;
}}


#card.show {{

    opacity:1;

    transform:
        translate(-50%,-50%)
        scale(1);
}}


#cake {{

    font-size:
        clamp(80px,15vw,140px);

    animation:
        cakeBounce 1.5s infinite;
}}


@keyframes cakeBounce {{

    0%,100% {{
        transform:translateY(0);
    }}

    50% {{
        transform:translateY(-15px);
    }}
}}


.cardTitle {{

    margin-top:10px;

    font-size:
        clamp(28px,6vw,55px);

    font-weight:900;

    background:
        linear-gradient(
            90deg,
            #ffd700,
            #00ffff,
            #7cff00,
            #ff8c00
        );

    -webkit-background-clip:text;

    color:transparent;
}}


.cardText {{

    margin-top:18px;

    color:#ffffff;

    font-size:
        clamp(16px,3vw,23px);

    line-height:1.7;
}}


/* =====================================================
   START BUTTON
===================================================== */

#startBtn {{

    position:absolute;

    left:50%;
    bottom:40px;

    transform:
        translateX(-50%);

    z-index:30;

    padding:
        15px 35px;

    border:none;

    border-radius:50px;

    background:
        linear-gradient(
            90deg,
            #00c6ff,
            #7b2ff7,
            #ff8c00
        );

    color:white;

    font-size:17px;

    font-weight:bold;

    cursor:pointer;

    box-shadow:
        0 0 20px
        rgba(0,255,255,.5);

    transition:.3s;
}}


#startBtn:hover {{

    transform:
        translateX(-50%)
        scale(1.08);

    box-shadow:
        0 0 40px
        rgba(0,255,255,.8);
}}


/* =====================================================
   TOP BADGE
===================================================== */

#badge {{

    position:absolute;

    top:25px;

    left:50%;

    transform:
        translateX(-50%);

    z-index:15;

    color:#ffffff;

    font-size:13px;

    letter-spacing:3px;

    opacity:.8;
}}


/* =====================================================
   MOBILE
===================================================== */

@media(max-width:600px) {{

    #name {{
        letter-spacing:3px;
    }}

    #wish {{
        width:94%;
    }}

    #card {{
        padding:28px 18px;
    }}

}}

</style>

</head>


<body>


<!-- =====================================================
     CANVAS
===================================================== -->

<canvas id="bgCanvas"></canvas>

<canvas id="particleCanvas"></canvas>

<canvas id="fireworkCanvas"></canvas>


<!-- =====================================================
     BADGE
===================================================== -->

<div id="badge">

    ✨ A SPECIAL BIRTHDAY SURPRISE ✨

</div>


<!-- =====================================================
     MAIN CONTENT
===================================================== -->

<div id="content">

    <div id="countdown">
        3
    </div>

    <div id="title">
        HAPPY BIRTHDAY
    </div>

    <div id="name">
        {NAME.upper()}
    </div>

    <div id="wish">
        Wishing you a wonderful year filled with
        happiness, success, good health,
        exciting opportunities and countless
        reasons to smile! 🎉
    </div>

</div>


<!-- =====================================================
     FINAL CARD
===================================================== -->

<div id="card">

    <div id="cake">
        🎂
    </div>

    <div class="cardTitle">
        HAPPY BIRTHDAY {NAME.upper()}!
    </div>

    <div class="cardText">

        🌟 May every new day bring you
        something exciting.<br><br>

        🎯 May you achieve all your goals.<br>

        😊 May your smile always stay bright.<br>

        🚀 May your dreams take you higher.<br>

        🍀 May good luck follow you everywhere.<br>

        🎉 And may this year become
        one of your most memorable years!

        <br><br>

        <b>
        HAVE AN AMAZING BIRTHDAY! 🎈
        </b>

    </div>

</div>


<button id="startBtn">

    🎁 OPEN BIRTHDAY SURPRISE

</button>


<script>

/* =====================================================
   CANVAS SETUP
===================================================== */

const bg =
    document.getElementById("bgCanvas");

const pc =
    document.getElementById("particleCanvas");

const fw =
    document.getElementById("fireworkCanvas");

const bctx =
    bg.getContext("2d");

const pctx =
    pc.getContext("2d");

const fctx =
    fw.getContext("2d");


let W =
    window.innerWidth;

let H =
    window.innerHeight;


function resize() {{

    W =
        window.innerWidth;

    H =
        window.innerHeight;

    bg.width=W;
    bg.height=H;

    pc.width=W;
    pc.height=H;

    fw.width=W;
    fw.height=H;
}}

resize();

window.addEventListener(
    "resize",
    resize
);


/* =====================================================
   STAR FIELD
===================================================== */

const stars=[];


for(
    let i=0;
    i<250;
    i++
){{

    stars.push({{

        x:Math.random()*W,

        y:Math.random()*H,

        r:Math.random()*2,

        speed:
            .2+
            Math.random()*.7,

        alpha:
            .2+
            Math.random()*.8
    }});
}}


function drawStars(){{

    bctx.clearRect(
        0,0,W,H
    );

    for(
        const s of stars
    ){{

        s.y+=s.speed;

        if(s.y>H)
            s.y=0;

        bctx.beginPath();

        bctx.arc(
            s.x,
            s.y,
            s.r,
            0,
            Math.PI*2
        );

        bctx.fillStyle=
            `rgba(
                255,
                255,
                255,
                ${{s.alpha}}
            )`;

        bctx.fill();
    }}

    requestAnimationFrame(
        drawStars
    );
}}

drawStars();


/* =====================================================
   FLOATING PARTICLES
===================================================== */

const particles=[];

const particleColors=[

    "#00ffff",
    "#ffd700",
    "#7cff00",
    "#9d4edd",
    "#ff8c00",
    "#ffffff"

];


for(
    let i=0;
    i<180;
    i++
){{

    particles.push({{

        x:Math.random()*W,

        y:Math.random()*H,

        size:
            1+
            Math.random()*4,

        speed:
            .3+
            Math.random()*1.5,

        color:
            particleColors[
                Math.floor(
                    Math.random()*
                    particleColors.length
                )
            ],

        angle:
            Math.random()*
            Math.PI*2
    }});
}}


function drawParticles(){{

    pctx.clearRect(
        0,0,W,H
    );

    for(
        const p of particles
    ){{

        p.y-=p.speed;

        p.x+=
            Math.sin(
                p.angle+=.01
            )*.4;

        if(p.y<0)
            p.y=H;

        pctx.beginPath();

        pctx.arc(
            p.x,
            p.y,
            p.size,
            0,
            Math.PI*2
        );

        pctx.fillStyle=p.color;

        pctx.shadowBlur=15;

        pctx.shadowColor=p.color;

        pctx.fill();
    }}

    pctx.shadowBlur=0;

    requestAnimationFrame(
        drawParticles
    );
}}

drawParticles();


/* =====================================================
   FIREWORK SYSTEM
===================================================== */

const fireworks=[];

const colors=[

    "#00ffff",
    "#ffd700",
    "#ff8c00",
    "#7cff00",
    "#9d4edd",
    "#ffffff"

];


function createFirework(
    x,
    y
){{

    const color=
        colors[
            Math.floor(
                Math.random()*
                colors.length
            )
        ];

    for(
        let i=0;
        i<70;
        i++
    ){{

        const angle=
            Math.random()*
            Math.PI*2;

        const speed=
            2+
            Math.random()*6;

        fireworks.push({{

            x:x,

            y:y,

            vx:
                Math.cos(angle)*
                speed,

            vy:
                Math.sin(angle)*
                speed,

            life:1,

            color:color
        }});
    }}
}}


function drawFireworks(){{

    fctx.fillStyle=
        "rgba(0,0,0,.15)";

    fctx.fillRect(
        0,0,W,H
    );

    for(
        let i=fireworks.length-1;
        i>=0;
        i--
    ){{

        const p=
            fireworks[i];

        p.x+=p.vx;

        p.y+=p.vy;

        p.vy+=.04;

        p.life-=.015;


        fctx.beginPath();

        fctx.arc(
            p.x,
            p.y,
            2.5,
            0,
            Math.PI*2
        );

        fctx.fillStyle=
            p.color;

        fctx.shadowBlur=15;

        fctx.shadowColor=
            p.color;

        fctx.globalAlpha=
            p.life;

        fctx.fill();


        if(
            p.life<=0
        ){{
            fireworks.splice(i,1);
        }}
    }}

    fctx.globalAlpha=1;

    fctx.shadowBlur=0;

    requestAnimationFrame(
        drawFireworks
    );
}}

drawFireworks();


/* =====================================================
   RANDOM FIREWORKS
===================================================== */

setInterval(()=>{{

    if(
        document
        .getElementById("card")
        .classList.contains("show")
    ){{
        createFirework(
            Math.random()*W,
            100+
            Math.random()*
            H*.45
        );
    }}

}},700);


/* =====================================================
   ELEMENTS
===================================================== */

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

const startBtn =
    document.getElementById(
        "startBtn"
    );


/* =====================================================
   COUNTDOWN
===================================================== */

function showCountdown(
    number
){{

    countdown.innerText=
        number;

    countdown.style.opacity="1";

    countdown.style.transform=
        "scale(1.2)";

    setTimeout(()=>{{

        countdown.style.transform=
            "scale(1)";

    }},150);
}}


/* =====================================================
   START EXPERIENCE
===================================================== */

startBtn.addEventListener(
    "click",
    ()=>{{

        startBtn.style.display=
            "none";

        let number=3;

        showCountdown(number);


        const timer=
            setInterval(()=>{{

                number--;

                if(number>0){{

                    showCountdown(
                        number
                    );

                }}

                else{{

                    clearInterval(timer);

                    countdown.style.opacity=
                        "0";


                    /* HAPPY BIRTHDAY */

                    setTimeout(()=>{{

                        title.classList.add(
                            "show"
                        );

                    }},400);


                    /* NAME */

                    setTimeout(()=>{{

                        name.classList.add(
                            "show"
                        );

                    }},1300);


                    /* WISH */

                    setTimeout(()=>{{

                        wish.style.opacity=
                            "1";

                    }},2300);


                    /* FIREWORKS */

                    setTimeout(()=>{{

                        for(
                            let i=0;
                            i<8;
                            i++
                        ){{

                            setTimeout(()=>{{

                                createFirework(
                                    100+
                                    Math.random()*
                                    (W-200),

                                    100+
                                    Math.random()*
                                    (H*.5)
                                );

                            }},
                            i*250);
                        }}

                    }},2800);


                    /* FINAL CARD */

                    setTimeout(()=>{{

                        title.style.opacity=
                            "0";

                        name.style.opacity=
                            "0";

                        wish.style.opacity=
                            "0";

                        card.classList.add(
                            "show"
                        );


                        for(
                            let i=0;
                            i<15;
                            i++
                        ){{

                            setTimeout(()=>{{

                                createFirework(
                                    Math.random()*W,
                                    Math.random()*H*.65
                                );

                            }},
                            i*180);

                        }}

                    }},6500);

                }}

            }},1000);

    });

</script>

</body>

</html>
"""


# =========================================================
# RENDER
# =========================================================

components.html(
    html_code,
    height=760,
    scrolling=False
)
