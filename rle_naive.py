class RunLengthEncoder:
    """ Run length encoder
    encode: "aaaaaaaaaaabbcccddddeff" -> "a11b2c3d4ef2"
    decode: "a11b2c3d4ef2" -> "aaaaaaaaaaabbcccddddeff"
    """
    @staticmethod
    def encode(s: str) -> str:
        """ Perform: "aaaaaaaaaaabbcccddddeff" -> "a11b2c3d4ef2"
        Iterate over the list, count the number of each alphabet
        and when the alphabet change, update the result with the
        aplhabet and count. If count is 1, change it to "" to 
        avoid printing 1.
        """
        out = []
        prev = s[0]
        count = 0
        for curr in s:
            if curr != prev:
                out += [prev + (str(count) if count != 1 else "")]
                count = 0
                prev = curr
            count += 1
        out += [prev + (str(count) if count != 1 else "")]
        return "".join(out)

    @staticmethod
    def decode(s: str) -> str:
        """ Perform: "a11b2c3d4ef2" -> "aaaaaaaaaaabbcccddddeff"
        For each alphabet, get the number following it and repeat the
        alphabet those many times. Treat absence of number as 1
        """
        out = []
        count = ""
        alpha = ""
        for char in s:
            if char.isalpha():
                out += [alpha*int(count or 1)]
                alpha = char
                count = ""
            elif char.isnumeric():
                count += char
        out += [alpha*int(count or 1)]
        return "".join(out)


if __name__ == "__main__":

    e = "jjjjjjjkkkkkkkkkmmmmmmggggfcsszzaaaaaaaaaaaaaaazzzzzzzzzzzzzzzzzzxcx"
    d = "j7k9m6g4fcs2z2a15z18xcx"
    assert RunLengthEncoder.encode(RunLengthEncoder.decode(d)) == d
    assert RunLengthEncoder.decode(RunLengthEncoder.encode(e)) == e
    assert RunLengthEncoder.encode(e) == d
    assert RunLengthEncoder.decode(d) == e
