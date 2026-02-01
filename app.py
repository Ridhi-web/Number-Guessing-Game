import streamlit as st
import random

st.set_page_config(page_title="Number Guessing Game", page_icon=":game_die:", layout="centered")

st.markdown("""<style>
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css');
    #MainMenu, header, footer {visibility: hidden;}
    
    .stApp {background: linear-gradient(to bottom, #000428 0%, #001845 50%, #000000 100%);}
    h1 {color: #14b8a6 !important; text-align: center; text-shadow: 0 0 20px rgba(20, 184, 166, 0.5);}
    
    .stButton>button {
        width: 100%; 
        background: linear-gradient(135deg, #14b8a6, #06b6d4); 
        color: white; 
        border: none; 
        padding: 1rem; 
        border-radius: 12px;
    }
    /* Separate rule to ensure text elements inside button inherit font correctly */
    .stButton>button * {
        font-family: "Font Awesome 6 Free", sans-serif !important;
        font-weight: 900 !important;
        font-style: normal !important;
    }
    
    .stat-card {background: rgba(20, 184, 166, 0.1); border: 1px solid rgba(20, 184, 166, 0.2); border-radius: 14px; padding: 1rem; text-align: center;}
    .stat-value {font-size: 1.5rem; font-weight: 700; color: #14b8a6;}
    
    .custom-alert {padding: 1rem; border-radius: 14px; font-weight: 600; text-align: center; margin: 1rem 0;}
    .alert-success {background: #22c55e26; border: 2px solid #22c55e80; color: #22c55e;}
    .alert-error {background: #ef444426; border: 2px solid #ef444480; color: #ef4444;}
    .alert-warning {background: #fbbf2426; border: 2px solid #fbbf2480; color: #fbbf24;}
    .alert-info {background: #14b8a626; border: 2px solid #14b8a680; color: #14b8a6;}
    
    a.anchor-link {display: none !important; height: 0px !important; width: 0px !important;}
    .anchor-link {display: none !important;}
    h1 > a, h2 > a, h3 > a, h4 > a, h5 > a, h6 > a {display: none !important;}
    
    .card-header {
        font-size: 1.3rem;
        font-weight: 700;
        margin: 0.5rem 0;
    }
</style>""", unsafe_allow_html=True)

if 'game_state' not in st.session_state:
    st.session_state.game_state = 'menu' 
    st.session_state.total_games = 0
    st.session_state.total_score = 0
    st.session_state.games_won = 0
    st.session_state.guesses = []
    st.session_state.feedback = None

SETTINGS = {
    'Easy':   {'icon': 'check-circle', 'min': 1, 'max': 50,  'tries': 10, 'bonus': 20, 'color': '#22c55e'},
    'Medium': {'icon': 'bolt',         'min': 1, 'max': 100, 'tries': 7,  'bonus': 30, 'color': '#fbbf24'},
    'Hard':   {'icon': 'fire',         'min': 1, 'max': 200, 'tries': 5,  'bonus': 50, 'color': '#ef4444'}
}

st.markdown("""
<div style='text-align: center;'>
    <i class='fas fa-dice' style='font-size: 4rem; color: #14b8a6;'></i>
    <div style='color: #14b8a6; font-size: 2.5rem; font-weight: 700; text-shadow: 0 0 20px rgba(20, 184, 166, 0.5); margin: 0.5rem 0;'>
        Number Guessing Game
    </div>
</div>
""", unsafe_allow_html=True)

if st.session_state.game_state == 'menu':
    
    col1, col2, col3 = st.columns(3)
    
    difficulties = list(SETTINGS.items()) 
    
    for i, (level_name, config) in enumerate(difficulties):
        with [col1, col2, col3][i]:
            st.markdown(f"""
            <div class='stat-card' style='border-color:{config['color']}4d; background:{config['color']}1a'>
                <i class='fas fa-{config['icon']}' style='font-size:2rem; color:{config['color']}'></i>
                <div class='card-header' style='color:{config['color']}'>{level_name}</div>
                <small>{config['min']}-{config['max']}</small>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Play {level_name}", key=level_name):
                st.session_state.game_state = 'playing'
                st.session_state.difficulty_name = level_name
                st.session_state.min_val = config['min']
                st.session_state.max_val = config['max']
                st.session_state.max_tries = config['tries']
                st.session_state.target = random.randint(config['min'], config['max'])
                st.session_state.used_tries = 0
                st.session_state.guesses = []
                st.session_state.feedback = None
                st.rerun() 

    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    
    if st.session_state.total_games > 0:
        win_rate = (st.session_state.games_won / st.session_state.total_games) * 100
    else:
        win_rate = 0
        
    c1.markdown(f"<div class='stat-card'><div class='stat-value'>{st.session_state.total_games}</div>Played</div>", unsafe_allow_html=True)
    c2.markdown(f"<div class='stat-card'><div class='stat-value'>{st.session_state.total_score}</div>Score</div>", unsafe_allow_html=True)
    c3.markdown(f"<div class='stat-card'><div class='stat-value'>{win_rate:.0f}%</div>Win Rate</div>", unsafe_allow_html=True)

elif st.session_state.game_state == 'playing':
    
    ss = st.session_state 
    current_config = SETTINGS[ss.difficulty_name]
    
    c1, c2 = st.columns([1, 4])
    if c1.button("\uf0a8 Back"): 
        ss.game_state = 'menu'
        st.rerun()
        
    attempts_left = ss.max_tries - ss.used_tries
    c2.markdown(f"<div style='text-align:right; color:{current_config['color']}'><i class='fas fa-{current_config['icon']}'></i> {ss.difficulty_name} | <b>{attempts_left}</b> left</div>", unsafe_allow_html=True)
    
    st.markdown(f"<div style='text-align:center; color:#94a3b8; margin:0; font-size: 1.3rem; font-weight: 600;'>Guess between {ss.min_val} and {ss.max_val}</div>", unsafe_allow_html=True)

    if ss.feedback: 
        alert_class, message = ss.feedback
        st.markdown(f"<div class='custom-alert alert-{alert_class}'>{message}</div>", unsafe_allow_html=True)
    
    guess = st.number_input("Enter your guess:", min_value=ss.min_val, max_value=ss.max_val, label_visibility="collapsed")
    
    if st.button("Submit Guess", use_container_width=True):
        if guess not in ss.guesses:
            ss.used_tries += 1
            ss.guesses.append(guess)
            
            if guess == ss.target: 
                points = (ss.max_tries - ss.used_tries) * 10 + current_config['bonus']
                ss.total_score += points
                ss.games_won += 1
                ss.total_games += 1
                ss.game_state = 'won'
                
            elif ss.used_tries >= ss.max_tries: 
                ss.total_games += 1
                ss.game_state = 'lost'
                
            else: 
                diff = abs(guess - ss.target)
                
                if diff <= 5:
                    hint_text, icon, alert_type = "VERY CLOSE", "fire", "warning"
                elif diff <= 10:
                    hint_text, icon, alert_type = "Warm", "temperature-high", "info"
                else:
                    hint_text, icon, alert_type = "Cold", "snowflake", "info"
                
                if guess < ss.target:
                    arrow_text, arrow_icon = "TOO LOW", "arrow-up"
                else:
                    arrow_text, arrow_icon = "TOO HIGH", "arrow-down"
                
                ss.feedback = (alert_type, f"<i class='fas fa-{arrow_icon}'></i> <b>{arrow_text}</b> • <i class='fas fa-{icon}'></i> {hint_text}")
            
            st.rerun() 
        else: 
            st.warning("You already guessed that number!")

    if ss.guesses:
        chips_html = ' '.join([f'<span style="background:#14b8a633; color:#14b8a6; padding:2px 8px; border-radius:4px; margin:2px">{g}</span>' for g in ss.guesses])
        st.markdown(f"<div style='text-align:center; margin-top:1rem'>{chips_html}</div>", unsafe_allow_html=True)

else:
    won = st.session_state.game_state == 'won'
    
    if won:
        color = '#22c55e'
        title = "Congratulations!"
        icon = "trophy"
    else:
        color = '#ef4444'
        title = "Game Over"
        icon = "times-circle"
        
    st.markdown(f"""
    <div style='text-align:center; margin:2rem; color:{color}'>
        <i class='fas fa-{icon}' style='font-size: 3rem; margin-bottom: 1rem;'></i>
        <div style='font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem;'>{title}</div>
        <p>The number was <b>{st.session_state.target}</b></p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("\uf021 Play Again", use_container_width=True): 
            current_config = SETTINGS[st.session_state.difficulty_name]
            st.session_state.game_state = 'playing'
            st.session_state.target = random.randint(current_config['min'], current_config['max'])
            st.session_state.used_tries = 0
            st.session_state.guesses = []
            st.session_state.feedback = None
            st.rerun()
        
    with col2:
        if st.button("\uf015 Main Menu", use_container_width=True): 
            st.session_state.game_state = 'menu'
            st.rerun()
