import streamlit as st

st.header("Quiz")
c = 0
w = 0

qs1 = st.radio("What has keys but can't open locks?", ['A. Piano', 'B. Door', 'C. Computer', 'D. Wallet'], index=None)
if qs1 == "A. Piano":
    c += 1
else:
    w += 1

qs2 = st.radio("I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?", ['A. Echo', 'B. Shadow', 'C. Ghost', 'D. Breeze'], index=None)
if qs2 == "A. Echo":
    c += 1
else:
    w += 1

qs3 = st.radio("What can travel around the world while staying in a corner?", ['A. Stamp', 'B. Compass', 'C. Postcard', 'D. Envelope'], index=None)
if qs3 == "A. Stamp":
    c += 1
else:
    w += 1

qs4 = st.radio("What has a head, a tail, is brown, and has no legs?", ['A. Coin', 'B. Snake', 'C. Bird', 'D. Cat'], index=None)
if qs4 == "A. Coin":
    c += 1
else:
    w += 1

qs5 = st.radio("I’m light as a feather, yet the strongest man can’t hold me for much longer than a minute. What am I?", ['A. Breath', 'B. Leaf', 'C. Paper', 'D. Bubble'], index=None)
if qs5 == "A. Breath":
    c += 1
else:
    w += 1

qs6 = st.radio("What comes once in a minute, twice in a moment, but never in a thousand years?", ['A. M', 'B. E', 'C. O', 'D. N'], index=None)
if qs6 == "A. M":
    c += 1
else:
    w += 1

qs7 = st.radio("I can be cracked, made, told, and played. What am I?", ['A. Joke', 'B. Egg', 'C. Code', 'D. Game'], index=None)
if qs7 == "A. Joke":
    c += 1
else:
    w += 1

qs8 = st.radio("The more you take, the more you leave behind. What am I?", ['A. Footsteps', 'B. Memories', 'C. Time', 'D. Space'], index=None)
if qs8 == "A. Footsteps":
    c += 1
else:
    w += 1

qs9 = st.radio("What has a neck but no head?", ['A. Bottle', 'B. Shirt', 'C. Drum', 'D. Lamp'], index=None)
if qs9 == "A. Bottle":
    c += 1
else:
    w += 1

qs10 = st.radio("What is full of holes but still holds a lot of water?", ['A. Sponge', 'B. Bucket', 'C. Net', 'D. Boat'], index=None)
if qs10 == "A. Sponge":
    c += 1
else:
    w += 1

qs11 = st.radio("I’m tall when I’m young, and I’m short when I’m old. What am I?", ['A. Candle', 'B. Tree', 'C. Building', 'D. Pencil'], index=None)
if qs11 == "A. Candle":
    c += 1
else:
    w += 1

qs12 = st.radio("I have branches, but no fruit, trunk, or leaves. What am I?", ['A. Bank', 'B. Tree', 'C. River', 'D. Family'], index=None)
if qs12 == "A. Bank":
    c += 1
else:
    w += 1

qs13 = st.radio("I am not alive, but I grow; I don’t have lungs, but I need air; I don’t have a mouth, but water kills me. What am I?", ['A. Fire', 'B. Rock', 'C. Plant', 'D. Cloud'], index=None)
if qs13 == "A. Fire":
    c += 1
else:
    w += 1

qs14 = st.radio("I can fly without wings. I can cry without eyes. Whenever I go, darkness flies. What am I?", ['A. Cloud', 'B. Shadow', 'C. Kite', 'D. Wind'], index=None)
if qs14 == "D. Wind":
    c += 1
else:
    w += 1

qs15 = st.radio("I have cities but no houses; I have mountains but no trees; I have water but no fish. What am I?", ['A. Map', 'B. Ocean', 'C. Desert', 'D. Planet'], index=None)
if qs15 == "A. Map":
    c += 1
else:
    w += 1

qs16 = st.radio("What has one eye but can’t see?", ['A. Needle', 'B. Cyclops', 'C. Potato', 'D. Button'], index=None)
if qs16 == "A. Needle":
    c += 1
else:
    w += 1

qs17 = st.radio("I have keys but can't open locks. I have space but no room. You can enter, but you can't go outside. What am I?", ['A. Keyboard', 'B. Puzzle', 'C. Vault', 'D. Box'], index=None)
if qs17 == "A. Keyboard":
    c += 1
else:
    w += 1

qs18 = st.radio("What has a heart that doesn’t beat?", ['A. Artichoke', 'B. Watch', 'C. Statue', 'D. Car'], index=None)
if qs18 == "A. Artichoke":
    c += 1
else:
    w += 1

qs19 = st.radio("I’m not alive, but I can grow. I don’t have lungs, but I need air. I don’t have a mouth, but water kills me. What am I?", ['A. Fire', 'B. Rock', 'C. Mushroom', 'D. Rust'], index=None)
if qs19 == "A. Fire":
    c += 1
else:
    w += 1

qs20 = st.radio("What can you hold in your right hand, but never in your left hand?", ['A. Left elbow', 'B. Right hand', 'C. Left knee', 'D. Right foot'], index=None)
if qs20 == "A. Left elbow":
    c += 1
else:
    w += 1

if st.button("Get Results"):
    st.write(f"Correct answers: {c}")
    st.write(f"Wrong answers: {w}")
    st.write(f"Total score: {c}/20")
