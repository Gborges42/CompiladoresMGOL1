tokens = {
    1: "Num", 
    3: "Num",
    6: "Num",
    8: "Lit",
    9: "id", 
    11: "comentário",
    12: "EOF",
    13: "OPR",
    14: "OPR",
    15: "OPR",
    16: "RCB",
    17: "OPM",
    18: "AB_P",
    19: "FC_P",
    20: "PT_V",
    21: "VIR"
}

class Token:
    def __init__(self, lexema, classe, tipo):
        self.tokens = {
            1: "Num", 
            3: "Num",
            6: "Num",
            8: "Lit",
            9: "id", 
            11: "comentário",
            12: "EOF",
            13: "OPR",
            14: "OPR",
            15: "OPR",
            16: "RCB",
            17: "OPM",
            18: "AB_P",
            19: "FC_P",
            20: "PT_V",
            21: "VIR"
        }
        self.lexema = lexema
        self.classe = self.tokens[classe]
        self.tipo = tipo