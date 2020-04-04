# Run-length-encoding

Run Length Encoding is a method of string compression as explained [here](https://en.wikipedia.org/wiki/Run-length_encoding).

## Example

```text
Encoder: "aaaaaaaaaaabbcccddddeff" -> "a11b2c3d4ef2"
Decoder: "a11b2c3d4ef2" -> "aaaaaaaaaaabbcccddddeff"
```

## Solution

### Encoder

Iterate over the list, count the number of each alphabet and when the alphabet change, update the result with the aplhabet and count.
If count is 1, change it to "" to avoid printing 1.

*Space Complexity: O(1)*  
*Time Complexity: O(n)*

```python3
def encode(s: str) -> str:
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
```

### Decoder

For each alphabet, get the number following it and repeat the alphabet those many times. Treat absence of number as 1.

*Space Complexity: O(1)*  
*Time Complexity: O(n)*

```python3
def decode(s: str) -> str:
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
```

## More Approaches

Links to some more approaches using built-in packages

1. [itertools.groupby](https://stackoverflow.com/questions/18948382/run-length-encoding-in-python)
2. [more_itertools.run_length](https://more-itertools.readthedocs.io/en/latest/api.html#more_itertools.run_length)
3. [Regular Expression](https://rosettacode.org/wiki/Run-length_encoding#Python)
4. [collections.OrderedDict](https://www.geeksforgeeks.org/run-length-encoding-python/?ref=rp)
