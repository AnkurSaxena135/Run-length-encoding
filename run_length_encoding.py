class RunLengthEncoder:
    """ Run length encoder
    encode: "aaaaaaaaaaabbcccddddeff" -> "a11b2c3d4ef2"
    decode: "a11b2c3d4ef2" -> "aaaaaaaaaaabbcccddddeff"
    """
    @staticmethod
    def encode(s: str) -> str:
        """ Perform: "aaaaaaaaaaabbcccddddeff" -> "a11b2c3d4ef2"
        """
        out = []
        prev = s[0]
        count = 0
        for curr in s:
            if curr != prev:
                out.append(prev + (str(count) if count != 1 else ""))
                count = 0
                prev = curr
            count += 1
        out.append(prev + (str(count) if count != 1 else ""))
        return "".join(out)

    @staticmethod
    def decode(s: str) -> str:
        """ Perform: "a11b2c3d4ef2" -> "aaaaaaaaaaabbcccddddeff"
        """
        out = []
        count = ""
        alpha = ""
        for char in s:
            if char.isalpha():
                out.append(alpha*int(count or 1))
                alpha = char
                count = ""
            elif char.isnumeric():
                count += char
        out.append(alpha*int(count or 1))
        return "".join(out)


if __name__ == "__main__":

    e = "jjjjjjjkkkkkkkkkmmmmmmggggfcsszzaaaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzxcx"
    d = "j7k9m6g4fcs2z2a15z18xcx"
    assert RunLengthEncoder.encode(RunLengthEncoder.decode(d)) == d
    assert RunLengthEncoder.decode(RunLengthEncoder.encode(e)) == e
    assert RunLengthEncoder.encode(e) == d
    assert RunLengthEncoder.decode(d) == e
