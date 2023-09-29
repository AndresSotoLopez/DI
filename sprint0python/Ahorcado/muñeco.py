#Archivo que guarda el muñeco en texto claro

def __muñeco__(numero):
    muñeco = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========", 
              "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========", "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 
              "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========", "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========" ,
              "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="]

    return muñeco[numero]

