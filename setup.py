import configparser
import signal
import argparse



def set_field(file, section, field, value):
    config = configparser.ConfigParser()
    config.read(file)

    if not config.has_section(section):
        print(f"Section '{section}' does not exist in the config file.")
        return
    config.set(section, field, str(value))

    with open(file, 'w') as config_file:
        config.write(config_file)


def get_field(file, section, field):
    config = configparser.ConfigParser()
    config.read(file)

    if config.has_option(section, field):
        return config.get(section, field)
    else:
        return None

# Function to handle Ctrl+C (KeyboardInterrupt)
def signal_handler(signal, frame):
    print("\nProgram terminated unexptectedly and could not finish.")
    print("Double check the config file before running the application. Exiting...")
    exit(0)

def config_field(file, section, field):
    current_value = get_field(file, section, field)

    # Register the signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    try:
        user_input = input(f"{field} [{current_value}]: ")
        if user_input:
            set_field(file, section, field, user_input)
    except KeyboardInterrupt:
        print("\nProgram terminated unexptectedly and could not finish.")
        print("Double check the config file before running the application. Exiting...")
        exit(0)


def dump_file(file):
    with open(file, 'r') as f:
        content = f.read()
    print(content)

def cmd_ui():
    config_file = 'config.ini'
    print (f"This script will help you configure the application.\nThe current config file is: \033[1m{config_file}\033[0m")
    print ("1. Configuring server...")
    config_field(config_file, 'Server', 'host')
    config_field(config_file, 'Server', 'port')
    print ("\n2. Configuring static...")
    config_field(config_file, 'Static', 'base_url')
    print ("\n3. Configuring database...")
    config_field(config_file, 'Database', 'endpoint')
    config_field(config_file, 'Database', 'port')
    config_field(config_file, 'Database', 'user')
    config_field(config_file, 'Database', 'password')
    print("\n##################################")
    print("##### Configuration finished #####")
    print("##################################")
    print("\nHere the current config file:")
    dump_file(config_file)

def update_config(args):
    config_file = 'config.ini'
    set_field(config_file, args.section, args.field, args.value)
    print(f"Updated config file: {config_file}")
    print(f"Section: {args.section}")
    print(f"Field: {args.field}")
    print(f"New value: {args.value}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Configuration script for the application.')
    parser.add_argument('--section', help='Configuration section name')
    parser.add_argument('--field', help='Configuration field name')
    parser.add_argument('--value', help='New value for the configuration field')
    args = parser.parse_args()

    if args.section and args.field and args.value:
        update_config(args)
    else:
        cmd_ui()
