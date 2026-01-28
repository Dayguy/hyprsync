#!/usr/bin/python

import os

home = os.environ["HOME"]


def get_hyprpaper_path():
    # Hyprpaper config
    hyprpaper_config = home + "/.config/hypr/hyprpaper.conf"
    line = ""
    # Open the file in read mode
    with open(hyprpaper_config, "r") as file:
        for line in file:
            if line.strip().startswith("path"):
                break
    # Close the file
    file.close()

    return line


def set_hyprlock_path(hyprpaper_setting):
    # Hyprlock config
    hyprlock_config = home + "/.config/hypr/hyprlock.conf"
    # Variable to hold the new file contents
    content = ""

    # Open the file in read mode
    with open(hyprlock_config, "r") as file:
        for line in file:
            if line.strip().startswith("path"):
                content += hyprpaper_setting
            else:
                content += line
    file.close()

    # Overwrite original content with the revised content
    with open(hyprlock_config, "w") as file:
        file.write(content)
    file.close()


def main():
    # Get the current wallpaper from Hyprpaper
    path_string = get_hyprpaper_path()
    # Use current wallpaper in Hyprlock for consistancy
    if path_string:
        set_hyprlock_path(path_string)


if __name__ == "__main__":
    main()
