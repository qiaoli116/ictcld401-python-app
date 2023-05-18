#!/bin/bash

# Function to prompt the user for input and set the value
prompt_input() {
  read -p "$1 [$2]: " value
  value="${value:-$2}"
  sed -i "s|^$1\s*=.*|$1 = $value|" config.ini
}

# Create a backup of the original INI file
cp config.ini config.ini.backup

# Function to retrieve the current value from the INI file
get_current_value() {
  current_value=$(awk -F '=' -v section="$1" -v field="$2" '
    $0 ~ "^\\[" section "\\]" { in_section = 1 }
    in_section && $0 ~ "^" field "[[:space:]]*=" {
      gsub(/^[[:blank:]]+|[[:blank:]]+$/, "", $2)
      print $2
      exit
    }
    ' config.ini)
}

# Prompt for Server section values
echo "## Configure the server:"
get_current_value "Server" "host"
prompt_input "host" "$current_value"
get_current_value "Server" "port"
prompt_input "port" "$current_value"

# Prompt for Static section value
echo
echo "## Configure the static assets base URI:"
get_current_value "Static" "base_uri"
prompt_input "base_uri" "$current_value"

# Prompt for Database section values
echo
echo "## Configure the database information:"
get_current_value "Database" "endpoint"
prompt_input "endpoint" "$current_value"
get_current_value "Database" "port"
prompt_input "port" "$current_value"
get_current_value "Database" "user"
prompt_input "user" "$current_value"
get_current_value "Database" "password"
prompt_input "password" "$current_value"

echo
echo "Setup completed successfully!"
