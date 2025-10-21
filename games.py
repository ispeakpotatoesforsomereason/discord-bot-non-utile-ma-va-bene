import random
import requests

def gen_pass(pass_length):
    letters_and_symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"
    password = ""

    for i in range(pass_length):
        password += random.choice(letters_and_symbols)

    return password

def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "testa"
    else:
        return "croce"
 
def roll_dice():
    return random.randint(1, 6)

def eight_ball():
    responses = [
        "si sicuro",
        "decisamente si.",
        "boh, penso di si.",
        "si, ovvio.",
        "puoi fidarti di me.",
        "così lo vedo, si.",
        "probabilmente si.",
        "forse si dai.",
        "si.",
        "i segni dicono di si.",
        "non lo so, riprova.",
        "riprova dopo.",
        "meglio non dirlo ora.",
        "non posso prevedere ora.",
        "pensa meglio e riprova.",
        "non ci contare troppo.",
        "la mia risposta è no.",
        "le fonti dicono di no.",
        "non sembra proprio.",
        "molto dubbio."
    ]
    return random.choice(responses)

def yes_or_no(question):
    yes_no_questions = [
        "ananas va sulla pizza?",
        "esistono rocce?",
        "l'acqua è bagnata?",
        "il fuoco è caldo?",
        "il cielo è blu?",
        "gli esseri umani sono robot?"
    ]
    if question in yes_no_questions:
        return "si" if random.randint(0, 2) == 0 else "no"

def why_did_the_chicken_cross_the_road():
    answers = [
        "boh, per andare dall'altra parte",
        "voleva scappare dal contadino",
        "cercava cibo",
        "voleva vedere cose nuove",
        "voleva stare con gli amici",
        "per evitare il traffico",
        "per vedere il mondo",
        "per trovare qualcuno",
        "per allontanarsi dai guai",
        "per dimostrare che non era un pollo",
        "per conquistare il mondo",
        "per capire gli umani",
        "era in missione segreta",
        "aveva bevuto troppo",
        "era un robot programmato così",
        "voleva mangiare gli umani"
    ]
    return random.choice(answers)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def fake_poop_scale():
    scale = random.uniform(0, 10)
    return  "sfortunato te che devi vedere quanto la cacca di qualcuno (in kg) pesa:" * int(scale)
