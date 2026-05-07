#!/usr/bin/env bash

HOUR=$(date +%H)
TODAY=$(date +%Y-%m-%d)
STATE_FILE="/home/user/Main/memory/.news-delivered"
MORNING_START=8
MORNING_END=10

ALREADY_DELIVERED=false
if [ -f "$STATE_FILE" ] && [ "$(cat "$STATE_FILE")" = "$TODAY" ]; then
  ALREADY_DELIVERED=true
fi

if [ "$HOUR" -ge "$MORNING_START" ] && [ "$HOUR" -lt "$MORNING_END" ] && [ "$ALREADY_DELIVERED" = "false" ]; then
  echo "$TODAY" > "$STATE_FILE"
  printf "=== Morning News Delivery ===\n"
  printf "It is morning (%s). Before anything else, immediately run the /news-update command. Do not ask first — just run it.\n" "$(date +%I:%M%p)"
  printf "After displaying the news brief, proceed to read memory/profile.md and memory/tasks.md as normal.\n"
  printf "If the user says they already saw the news or don't want it, skip it and proceed normally.\n"
else
  printf "=== Memory System Active ===\n"
  printf "Start by reading memory/profile.md and memory/tasks.md to load context.\n"
  printf "Then ask: What do you want to work on today?\n"
fi
