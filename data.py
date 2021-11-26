# Made by Raúl Gilabert on 19/11/2021

def get():
    type0: list = [["code", 4], ["reg", 3], ["reg", 3], ["reg", 3],
                   ["operation", 3]]

    type1: list = [["code", 4], ["reg", 3], ["reg", 3], ["num", 6]]

    type2: list = [["code", 4], ["reg", 3], ["operation", 1], ["num", 8]]

    data: dict = dict(
        mnemonicToBinary=dict(
            AND=dict(code="0000", operation="000", dataInfo=type0),
            OR=dict(code="0000", operation="001", dataInfo=type0),
            XOR=dict(code="0000", operation="010", dataInfo=type0),
            NOT=dict(code="0000", operation="011", dataInfo=type0),
            ADD=dict(code="0000", operation="100", dataInfo=type0),
            SUB=dict(code="0000", operation="101", dataInfo=type0),
            SHA=dict(code="0000", operation="110", dataInfo=type0),
            SHL=dict(code="0000", operation="111", dataInfo=type0),
            CMPLT=dict(code="0001", operation="000", dataInfo=type0),
            CMPLE=dict(code="0001", operation="001", dataInfo=type0),
            CMPEQ=dict(code="0001", operation="011", dataInfo=type0),
            CMPLTU=dict(code="0001", operation="100", dataInfo=type0),
            CMPLEU=dict(code="0001", operation="101", dataInfo=type0),
            ADDI=dict(code="0010", dataInfo=type1),
            LD=dict(code="0011", dataInfo=type1),
            ST=dict(code="0100", dataInfo=type1),
            LDB=dict(code="0101", dataInfo=type1),
            STB=dict(code="0110", dataInfo=type1),
            BZ=dict(code="1000", operation="0", dataInfo=type2),
            BNZ=dict(code="1000", operation="1", dataInfo=type2),
            MOVI=dict(code="1001", operation="0", dataInfo=type2),
            MOVHI=dict(code="1001", operation="1", dataInfo=type2),
            IN=dict(code="1010", operation="0", dataInfo=type2),
            OUT=dict(code="1010", operation="1", dataInfo=type2)
        ),

        binary_to_mnemonic={
            "0000": {"000": "AND", "001": "OR", "010": "XOR", "011": "NOT",
                     "100": "ADD", "101": "SUB", "110": "SHA", "111": "SHL"},
            "0001": {"000": "CMPLT", "001": "CMPLE", "011": "CMPEQ", "100":
                     "CMPLTU", "101": "CMPLEU"},
            "0010": "ADDI",
            "0011": "LD",
            "0100": "ST",
            "0101": "LDB",
            "0110": "STB",
            "1000": {"0": "BZ", "1": "BNZ"},
            "1001": {"0": "MOVI", "1": "MOVHI"},
            "1010": {"0": "IN", "1": "OUT"}},

        registers={'R0': "000", 'R1': "001", 'R2': "010", 'R3': "011",
                   'R4': "100", 'R5': "101", 'R6': "110", 'R7': "111",
                   "-": "000"},

        registers_alu={'R0': "000", 'R1': "001", 'R2': "010", 'R3': "011",
                       'R4': "100", 'R5': "101", 'R6': "110", 'R7': "111",
                       "-": "XXX"},

        registers_bin={
            "000": "R0",
            "001": "R1",
            "010": "R2",
            "011": "R3",
            "100": "R4",
            "101": "R5",
            "110": "R6",
            "111": "R7"
        },

        alu_to_binary=dict(
            AND=dict(
                operation="00", function="000", a_address="???",
                b_address="???", d_address="???", rb_n="1", ila="00", wrd="1",
                wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="XXXXXXXXXXXXXXXX"
            ),
            OR=dict(
                operation="00", function="001", a_address="???",
                b_address="???", d_address="???", rb_n="1", ila="00",
                wrd="1", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="XXXXXXXXXXXXXXXX"
            ),
            XOR=dict(
                operation="00", function="010", a_address="???",
                b_address="???", d_address="???", rb_n="1", ila="00",
                wrd="1", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="XXXXXXXXXXXXXXXX"
            ),
            NOT=dict(
                operation="00", function="011", a_address="???",
                b_address="XXX", d_address="???", rb_n="1", ila="00",
                wrd="1", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="XXXXXXXXXXXXXXXX"
            ),
            ADD=dict(
                operation="00", function="100", a_address="???",
                b_address="???", d_address="???", rb_n="1", ila="00",
                wrd="1", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="XXXXXXXXXXXXXXXX"
            ),
            SUB=dict(
                operation="00", function="101", a_address="???",
                b_address="???", d_address="???", rb_n="1", ila="00",
                wrd="1", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="XXXXXXXXXXXXXXXX"
            ),
            SHA=dict(
                operation="00", function="110", a_address="???",
                b_address="???", d_address="???", rb_n="1", ila="00",
                wrd="1", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="XXXXXXXXXXXXXXXX"
            ),
            SHL=dict(
                operation="00", function="111", a_address="???",
                b_address="???", d_address="???", rb_n="1", ila="00",
                wrd="1", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="XXXXXXXXXXXXXXXX"
            ),
            ANDI=dict(
                operation="00", function="000", a_address="???",
                b_address="XXX", d_address="???", rb_n="0", ila="00", wrd="1",
                wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="????????????????"
            ),
            ORI=dict(
                operation="00", function="001", a_address="???",
                b_address="XXX", d_address="???", rb_n="0", ila="00",
                wrd="1", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="????????????????"
            ),
            XORI=dict(
                operation="00", function="010", a_address="???",
                b_address="XXX", d_address="???", rb_n="0", ila="00",
                wrd="1", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="????????????????"
            ),
            ADDI=dict(
                operation="00", function="100", a_address="???",
                b_address="XXX", d_address="???", rb_n="0", ila="00",
                wrd="1", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="????????????????"
            ),
            SUBI=dict(
                operation="00", function="101", a_address="???",
                b_address="XXX", d_address="???", rb_n="0", ila="00",
                wrd="1", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="????????????????"
            ),
            SHAI=dict(
                operation="00", function="110", a_address="???",
                b_address="XXX", d_address="???", rb_n="0", ila="00",
                wrd="1", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="????????????????"
            ),
            SHLI=dict(
                operation="00", function="111", a_address="???",
                b_address="XXX", d_address="???", rb_n="0", ila="00",
                wrd="1", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="????????????????"
            ),
            CMPLT=dict(
                operation="01", function="000", a_address="???",
                b_address="???", d_address="???", rb_n="1", ila="00", wrd="1",
                wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="XXXXXXXXXXXXXXXX"
            ),
            CMPLE=dict(
                operation="01", function="001", a_address="???",
                b_address="???", d_address="???", rb_n="1", ila="00",
                wrd="1", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="XXXXXXXXXXXXXXXX"
            ),
            CMPEQ=dict(
                operation="01", function="011", a_address="???",
                b_address="XXX", d_address="???", rb_n="1", ila="00",
                wrd="1", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="XXXXXXXXXXXXXXXX"
            ),
            CMPLTU=dict(
                operation="01", function="100", a_address="???",
                b_address="???", d_address="???", rb_n="1", ila="00",
                wrd="1", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="XXXXXXXXXXXXXXXX"
            ),
            CMPLEU=dict(
                operation="01", function="101", a_address="???",
                b_address="???", d_address="???", rb_n="1", ila="00",
                wrd="1", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="XXXXXXXXXXXXXXXX"
            ),
            CMPLTI=dict(
                operation="01", function="000", a_address="???",
                b_address="XXX", d_address="???", rb_n="0", ila="00", wrd="1",
                wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="????????????????"
            ),
            CMPLEI=dict(
                operation="01", function="001", a_address="???",
                b_address="XXX", d_address="???", rb_n="0", ila="00",
                wrd="1", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="????????????????"
            ),
            CMPEQI=dict(
                operation="01", function="011", a_address="???",
                b_address="XXX", d_address="???", rb_n="0", ila="00",
                wrd="1", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="????????????????"
            ),
            CMPLTUI=dict(
                operation="01", function="100", a_address="???",
                b_address="XXX", d_address="???", rb_n="0", ila="00",
                wrd="1", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="????????????????"
            ),
            CMPLEUI=dict(
                operation="01", function="101", a_address="???",
                b_address="XXX", d_address="???", rb_n="0", ila="00",
                wrd="1", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="????????????????"
            ),
            X=dict(
                operation="10", function="000", a_address="???",
                b_address="XXX", d_address="XXX", rb_n="0", ila="XX",
                wrd="0", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="????????????????"
            ),
            Y=dict(
                operation="10", function="001", a_address="XXX",
                b_address="???", d_address="XXX", rb_n="0", ila="XX",
                wrd="0", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="????????????????"
            ),
            LD=dict(
                operation="00", function="100", a_address="???",
                b_address="XXX", d_address="???", rb_n="0", ila="01",
                wrd="1", wrout="0", rd_in="0", wr_mem="0", byte="0", tknbr="0",
                addr_io="????????", n="XXXXXXXXXXXXXXXX"
            ),
            ST=dict(
                operation="00", function="100", a_address="???",
                b_address="???", d_address="XXX", rb_n="0", ila="XX",
                wrd="0", wrout="0", rd_in="0", wr_mem="1", byte="0", tknbr="0",
                addr_io="????????", n="XXXXXXXXXXXXXXXX"
            ),
            LDB=dict(
                operation="00", function="100", a_address="???",
                b_address="XXX", d_address="???", rb_n="0", ila="01",
                wrd="1", wrout="0", rd_in="0", wr_mem="0", byte="1", tknbr="0",
                addr_io="????????", n="XXXXXXXXXXXXXXXX"
            ),
            STB=dict(
                operation="00", function="100", a_address="???",
                b_address="???", d_address="XXX", rb_n="0", ila="XX",
                wrd="0", wrout="0", rd_in="0", wr_mem="1", byte="1", tknbr="0",
                addr_io="????????", n="XXXXXXXXXXXXXXXX"
            ),
            BZ=dict(
                operation="XX", function="XXX", a_address="???",
                b_address="XXX", d_address="XXX", rb_n="0", ila="XX",
                wrd="0", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="1",
                addr_io="XXXXXXXX", n="????????????????"
            ),
            BNZ=dict(
                operation="XX", function="XXX", a_address="???",
                b_address="XXX", d_address="XXX", rb_n="0", ila="XX",
                wrd="0", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="1",
                addr_io="XXXXXXXX", n="????????????????"
            ),
            MOVI=dict(
                operation="XX", function="XXX", a_address="XXX",
                b_address="XXX", d_address="???", rb_n="0", ila="XX",
                wrd="0", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="????????????????"
            ),
            MOVEI=dict(
                operation="XX", function="XXX", a_address="XXX",
                b_address="XXX", d_address="???", rb_n="0", ila="XX",
                wrd="0", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="????????????????"
            ),
            MOVHI=dict(
                operation="10", function="010", a_address="???",
                b_address="XXX", d_address="???", rb_n="0", ila="XX",
                wrd="1", wrout="0", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="XXXXXXXX", n="????????????????"
            ),
            IN=dict(
                operation="XX", function="XXX", a_address="XXX",
                b_address="XXX", d_address="???", rb_n="X", ila="10",
                wrd="1", wrout="0", rd_in="1", wr_mem="0", byte="X", tknbr="0",
                addr_io="????????", n="XXXXXXXXXXXXXXXX"
            ),
            OUT=dict(
                operation="XX", function="XXX", a_address="???",
                b_address="XXX", d_address="XXX", rb_n="0", ila="XX",
                wrd="0", wrout="1", rd_in="0", wr_mem="0", byte="X", tknbr="0",
                addr_io="????????", n="XXXXXXXXXXXXXXXX"
            ),
        )
    )

    return data
