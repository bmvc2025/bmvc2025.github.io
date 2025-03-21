#!/bin/bash

# Define the master folder
MASTER_FOLDER="/home/gerardo/BMVC2024/bmvc2024_upload"
TEMP_FOLDER="/tmp/unzip_temp"

# Create the temporary folder
mkdir -p "$TEMP_FOLDER"

# Iterate over each subfolder in the master folder
for SUBFOLDER in "$MASTER_FOLDER"/*; do
  if [ -d "$SUBFOLDER" ]; then
    VIDEO_FILE="$SUBFOLDER/video.mp4"
    if [ -f "$VIDEO_FILE" ]; then
      echo "Uncompressing $VIDEO_FILE"
      # Uncompress the video file to the temporary folder
      unzip -o "$VIDEO_FILE" -d "$TEMP_FOLDER"
      # Find the uncompressed video file, ignoring hidden files and directories
      UNCOMPRESSED_VIDEO=$(find "$TEMP_FOLDER" -type f -name "*.mp4" ! -name ".*")
      if [ -n "$UNCOMPRESSED_VIDEO" ]; then
        # Rename and move the uncompressed file to the subfolder
        echo "Moving $UNCOMPRESSED_VIDEO to $SUBFOLDER/video_new.mp4"
        mv "$UNCOMPRESSED_VIDEO" "$SUBFOLDER/video.mp4"
      else
        echo "No .mp4 file found in the uncompressed contents of $VIDEO_FILE"
      fi
    #   # Optionally, remove the original compressed file
    #   rm "$VIDEO_FILE"
    else
      echo "No video.mp4.zip found in $SUBFOLDER"
    fi
  fi
done

# Remove the temporary folder
rm -rf "$TEMP_FOLDER"