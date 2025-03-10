# IP obfuscator

An IP obfuscator is a tool used to mask, hide, or manipulate an IP address to make it difficult to trace the original source. It is commonly used in cybersecurity, privacy protection, and ethical hacking to anonymize network activity.

<!-- Some Information -->
⚠️  *I am a student who is still learning and my knowledge isn't perfect. The knowledge shared below is entirely based on my understanding. If you found any mistake feel free to open an issue.*

## Encoding/Obfuscating IP Representation

An IP representation refers to the different ways an IP address can be written or formatted. Since an IPv4 address is just a 32-bit number, it can be represented in various ways.

1. Decimal Format: \
    An IPv4 address is a 32-bit number that is conceptually divided into four 8-bit segments (or octets). Each octet can represent 256 possible values (0 to 255), which is why we say it's "base 256" in terms of the number of distinct values per octet. However, when you see an IPv4 address in dotted decimal notation (like 192.168.1.1), each of those octets is expressed as a decimal (base 10) number. So, while the underlying data is organized in bytes (base 256), the dotted decimal representation displays these numbers in base 10.

    To convert Pv4 Address into a Single Integer Representation: \
    $(O_1 \times 256^3) + (O_2 \times 256^2) + (O_3 \times 256^1) + (O_4 \times 256^0)$

    Where: \
    $0_1,0_2,0_3,0_4$ are the four octets of the IP address.

    Example: \
    Converting `192.168.1.1` to single decimal number.

    Four octets of the IP address `192.168.1.1` are: \
    $0_1$ = 192 \
    $0_2$ = 168 \
    $0_3$ = 1 \
    $0_4$ = 1

    Conversion: \
    $(192 \times 256^3) + (168 \times 256^2) + (1 \times 256^1) + (1 \times 256^0) = 3232235777$

    Hence: IP address `192.168.1.1` can be represented as $3232235777$ in Single decimal number.

2. Hexadecimal Format: \
    To convert Pv4 Address into Hexadecimal Representation: \
    Hex Representation = $Hex(0_1).Hex(0_2).Hex(0_3).Hex(0_4)$

    Example: \
    Converting `192.168.1.1` to Hexadecimal format.

    Convert each decimal octet to hexadecimal:
    - $192_{10} = C0_{16}$
    - $168_{10} = A8_{16}$
    - $1_{10} = 01_{16}$
    - $1_{10} = 01_{16}$

    So, `192.168.1.1` in hex is $C0.A8.01.01$

3. Octadecimal Format: \
    To convert Pv4 Address into Octal Representation: \
    Octal Representation = $Oct(0_1).Oct(0_2).Oct(0_3).Oct(0_4)$

    Example: \
    Converting `192.168.1.1` to octal format.

    Convert each decimal octet to octal:
    - $192_{10} = 0300_{8}$
    - $168_{10} = 0250_{8}$
    - $1_{10} = 0001_{8}$
    - $1_{10} = 0001_{8}$

    So, `192.168.1.1` in octal is $0300.0250.0001.0001$
