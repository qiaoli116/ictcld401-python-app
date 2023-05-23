#!/bin/bash

# Function to prompt the user for input and set the value
prompt_input() {
  local section=$1
  local field=$2
  local default_value=$3
  local value

  read -p "$field [$default_value]: " value
  value="${value:-$default_value}"

  sed -i "s|^\[$section\].*$field\s*=.*|[$section]\n$field = $value|" config.ini
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
prompt_input "Server" "host" "$current_value"
get_current_value "Server" "port"
prompt_input "Server" "port" "$current_value"

# Prompt for Static section value
echo
echo "## Configure the static assets base URI:"
get_current_value "Static" "base_url"
prompt_input "Static" "base_url" "$current_value"

# Prompt for Database section values
echo
echo "## Configure the database information:"
get_current_value "Database" "endpoint"
prompt_input "Database" "endpoint" "$current_value"
get_current_value "Database" "port"
prompt_input "Database" "port" "$current_value"
get_current_value "Database" "user"
prompt_input "Database" "user" "$current_value"
get_current_value "Database" "password"
prompt_input "Database" "password" "$current_value"

echo
echo "Setup completed successfully!"
