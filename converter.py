import argparse

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(
        description="Convert temperatures between Celsius and Fahrenheit."
    )

    # Create a mutually exclusive group to ensure only one conversion type is chosen
    group = parser.add_mutually_exclusive_group(required=True)

    # Option for converting Celsius to Fahrenheit
    group.add_argument(
        "--c2f", type=float, metavar="C",
        help="Convert Celsius to Fahrenheit. Provide the Celsius value."
    )

    # Option for converting Fahrenheit to Celsius
    group.add_argument(
        "--f2c", type=float, metavar="F",
        help="Convert Fahrenheit to Celsius. Provide the Fahrenheit value."
    )

    # Parse the command-line arguments
    args = parser.parse_args()

    # Perform the appropriate conversion based on the option used
    if args.c2f is not None:
        f = celsius_to_fahrenheit(args.c2f)
        print(f"{args.c2f}°C = {f:.2f}°F")

    elif args.f2c is not None:
        c = fahrenheit_to_celsius(args.f2c)
        print(f"{args.f2c}°F = {c:.2f}°C")

# Entry point of the script
if __name__ == "__main__":
    main()
