def mostrar_boneco(vidas):
    if vidas == 6:
        print("""
           -----
           |   |
               |
               |
               |
               |
        =========
        """)
    elif vidas == 5:
        print("""
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """)
    elif vidas == 4:
        print("""
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """)
    elif vidas == 3:
        print("""
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """)
    elif vidas == 2:
        print("""
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """)
    elif vidas == 1:
        print("""
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """)
    elif vidas == 0:
        print("""
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """)

    