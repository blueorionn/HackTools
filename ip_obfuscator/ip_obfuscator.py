import sys
import argparse
import random

# GENERAL KNOWLEDGE:
# An IPv4 address is a 32-bit numerical address used for identifying devices on a network.
# It is typically represented in dotted decimal notation to make it human-readable.
#  It is expressed as a series of four decimal numbers, each ranging from 0 to 255,
# separated by periods (dots). Each decimal number represents an 8-bit binary value (octet),
# and the entire IP address comprises 32 bits.


# For simplicity you can use int(ipaddress.ip_address(ip))
def check_ip_validity(ip: str):
    """Check whether ip argument is a valid ipv4 address or not."""

    if type(ip) != str:
        sys.stdout.write(f"{ip} is not a valid ipv4 address \n")
        sys.exit(1)

    elif len(ip.split(".")) != 4:
        sys.stdout.write(
            f"{ip} is not a valid ipv4 address."
            + "Address must be a series of four decimal number \n"
        )
        sys.exit(1)

    for d in ip.split("."):
        try:
            octet = int(d)
            # Check range of octet (0-255)
            if octet < 0 or octet > 255:
                sys.stdout.write(
                    f"{ip} is not a valid ipv4 address."
                    + "Range of octet should be 0-255 \n"
                )
                sys.exit(1)

        except ValueError:
            sys.stdout.write(f"{ip} is not a valid ipv4 address \n")
            sys.exit(1)


# IP address is actually structured as a base-256 number
# because each "place" (octet) represents a power of 256.
def convert_ip_to_int(ip: str):
    octets = [int(o) for o in ip.split(".")]

    # Converting to base 10
    ip_int = (
        (256**3) * (octets[0])
        + (256**2) * (octets[1])
        + (256**1) * (octets[2])
        + (256**0) * (octets[3])
    )

    sys.stdout.write(f"Integer: {ip_int} \n")


def convert_ip_to_octet(ip: str):
    octets = [int(o) for o in ip.split(".")]

    # Convert to base 8
    ip_oct = ".".join([f"{oct(o)[2:].zfill(4)}" for o in octets])
    sys.stdout.write(f"Octal: {ip_oct} \n")


def convert_ip_to_hex(ip: str):
    octets = [int(o) for o in ip.split(".")]

    # Convert to base 8
    ip_hex = ".".join([f"{hex(o)}".upper() for o in octets])
    sys.stdout.write(f"Hexadecimal: {ip_hex} \n")


def convert_ip_to_binary(ip: str):
    octets = [int(o) for o in ip.split(".")]

    # Convert to base 2
    s_format = ".".join([f"{bin(x)[2:].zfill(8)}" for x in octets])
    b_format = "".join([bin(x)[2:].zfill(8) for x in octets])

    sys.stdout.write(f"Binary: {b_format} \n")
    sys.stdout.write(f"Dotted Binary: {s_format} \n")


def convert_ip_to_mapped_ipv6(ip: str):
    """Using IPv4-mapped IPv6 address to epresent an IPv4 address within an IPv6 address"""

    # An IPv4-mapped IPv6 address is a special IPv6 format designed to
    # represent an IPv4 address within an IPv6 address. It is used
    # primarily to enable dual-stack systems (those that support both IPv4 and IPv6)
    # to handle IPv4 connections within an IPv6 context.

    octets = [int(o) for o in ip.split(".")]

    # Converting ipv4 to ipv6
    first, second, third, fourth = [f"{hex(o)[2:].zfill(2)}".upper() for o in octets]

    sys.stdout.write(f"IPv6 (short): ::FFFF:{first}{second}:{third}{fourth} \n")
    sys.stdout.write(
        f"IPv6 (long): 0000:0000:0000:0000:0000:FFFF:{first}{second}:{third}{fourth} \n"
    )


def random_ip_base(ip: str):
    """Converting one of the octets to a random base."""

    octets = [int(o) for o in ip.split(".")]
    bases = ["hex", "oct"]

    # chosen base and octet
    chosen_octets = random.randint(0, (len(octets) - 1))
    chosen_base = random.choice(bases)

    if chosen_base == "hex":
        converted_ip = []

        for i, o in enumerate(octets):
            # For chosen index of octects array
            if i == chosen_octets:
                converted_ip.append(f"{hex(o)}")
            else:
                converted_ip.append(f"{o}")
    elif chosen_base == "oct":
        converted_ip = []

        for i, o in enumerate(octets):
            # For chosen index of octects array
            if i == chosen_octets:
                converted_ip.append(f"{oct(o)}")
            else:
                converted_ip.append(f"{o}")

    sys.stdout.write(f"Random Base: {'.'.join(converted_ip)} \n")


def main():
    parser = argparse.ArgumentParser(
        prog="Ip_obfuscator",
        description=(
            "Python cli tool to convert Ipv4 address to various alternative notations"
            + "like Decimal, Octal, Hexadecimal and various others."
        ),
        epilog="Thanks for using Ip_obfuscator! :)",
    )
    parser.add_argument("ip", help="Takes a valid ipv4 address.")
    args = parser.parse_args()

    # Ip address argument
    ip: str = args.ip
    check_ip_validity(ip)

    # conversion of Ip
    convert_ip_to_int(ip)
    convert_ip_to_octet(ip)
    convert_ip_to_hex(ip)
    convert_ip_to_binary(ip)
    convert_ip_to_mapped_ipv6(ip)
    random_ip_base(ip)


if __name__ == "__main__":
    main()
