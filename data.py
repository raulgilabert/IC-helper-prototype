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
            "0000": [type0, {"000": "AND", "001": "OR", "010": "XOR", "011":
                             "NOT", "100": "ADD", "101": "SUB", "110": "SHA",
                             "111": "SHL"}],
            "0001": [type0, {"000": "CMPLT", "001": "CMPLE", "011": "CMPEQ",
                             "100": "CMPLTU", "101": "CMPLEU"}],
            "0010": [type1],
            "0011": [type1],
            "0100": [type1],
            "0101": [type1],
            "0110": [type1],
            "1000": [type2, {"0": "BZ", "1": "BNZ"}],
            "1001": [type2, {"0": "MOVI", "1": "MOVHI"}],
            "1010": [type2, {"0": "IN", "1": "OUT"}]
        },

        registers=dict(R0="000", R1="001", R2="010", R3="011", R4="100",
                       R5="101", R6="110", R7="111"))

    return data
