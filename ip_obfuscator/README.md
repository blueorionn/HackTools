# IP obfuscator

An IP obfuscator is a tool used to mask, hide, or manipulate an IP address to make it difficult to trace the original source. It is commonly used in cybersecurity, privacy protection, and ethical hacking to anonymize network activity.

<!-- Some Information -->
*I am a student and knowledge isn't perfect. I am still learning, the knowledge shared below is entirely based on my understanding. If you found any mistake feel free to open an issue.*

## Encoding/Obfuscating IP Representation

An IP representation refers to the different ways an IP address can be written or formatted. Since an IPv4 address is just a 32-bit number, it can be represented in various ways.

1. Decimal Format

    Converts an IP address to a single decimal number.

    An IPv4 address is a 32-bit number that is conceptually divided into four 8-bit segments (or octets). Each octet can represent 256 possible values (0 to 255), which is why we say it's "base 256" in terms of the number of distinct values per octet. However, when you see an IPv4 address in dotted decimal notation (like 192.168.1.1), each of those octets is expressed as a decimal (base 10) number. So, while the underlying data is organized in bytes (base 256), the dotted decimal representation displays these numbers in base 10.

    To convert Pv4 Address into a Single Integer Representation:
    (O_1 \times 256^3) + (O_2 \times 256^2) + (O_3 \times 256^1) + (O_4 \times 256^0)

    Where:
    0_1,0_2,0_3,0_4 are the four octets of the IP address.
