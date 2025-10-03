meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "HYPE": "Emoción o expectativa alta",
    "GLAZE": "Mencionar o destacar mucho de un famoso",
    "CORE": "Para nombrar un tipo de moda o estética",
    "SHIP": "Apoyar una relación entre dos personas",
    "VIBE": "Energía o ambiente que transmite algo",
    "SPAM": "Mensajes repetitivos o molestos",
    "SKIN": "Apariencia de un personaje de los juegos",
    "CAP": "Mentira",
    "NO CAP": "No mentira",
    "ALT": "Cuenta secundaria",
    "AFK": "'Away From Keyboard', estar ausente",
    "METAVERSE": "Mundo virtual",
    "LORE": "El trasfondo detrás de algo",
    "LAG": "Retraso en internet o videojuegos",
    "BUG": "Un error en videojuegos",
    "SPEEDRUN": "Completar un nivel lo más rápido posible",
    "CANON": "Lo oficial / lo que inventan los fans",
    "HEADCANON": "Interpretación de los fans que no es oficial",
    "1v1": "'One versus One', 1 contra 1 en un juego generalmente de batallas",
    "PvP": "'Player versus Player', juego entre jugadores",
    "GHOSTEAR": "Desaparecer de una relación o chat sin explicación",
    "IRL": "'In Real Life', en la vida real",
    "GG": "'Good Game', buen juego, se usa al final de partidas",
    "EZ": "'Easy', fácil; también se usa para presumir o provocar",
    "OP": "'Overpowered', significa que algo (personaje o enemigo) está muy fuerte o roto"
}

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict:
    print(word + ": " + meme_dict[word])
else:
    print("Lo siento, no conozco esa palabra.")

