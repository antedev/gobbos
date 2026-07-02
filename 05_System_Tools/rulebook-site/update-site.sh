#!/bin/bash
set -e

# Configuration
REPO_DIR="/home/ante/projects/gobbos"
SITE_DIR="$REPO_DIR/05_System_Tools/rulebook-site"
LOG_FILE="$SITE_DIR/update.log"
EMAIL_SCRIPT="$SITE_DIR/send_email.py"

# Add common local paths to PATH so git, node, and npm can be located by cron
export PATH="/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$PATH"

# Redirect stdout and stderr to the log file (append mode)
exec >> "$LOG_FILE" 2>&1

echo "============================================="
echo "Update check triggered on $(date)"
echo "============================================="

# Helper function to send email
send_notification() {
    local subject="$1"
    local body="$2"
    if [ -f "$EMAIL_SCRIPT" ]; then
        python3 "$EMAIL_SCRIPT" "$subject" "$body"
    else
        echo "WARNING: $EMAIL_SCRIPT not found. Cannot send email."
    fi
}

# Trap handler for failures
handle_failure() {
    local exit_code=$?
    if [ $exit_code -ne 0 ]; then
        echo "Update failed with exit code $exit_code."
        
        # Write error to status.json so the website displays a banner
        mkdir -p "$SITE_DIR/dist"
        cat <<EOF > "$SITE_DIR/dist/status.json"
{
  "status": "error",
  "exit_code": $exit_code,
  "timestamp": "$(date)"
}
EOF
        
        send_notification "Gobbos Update FAILED" "The automated Gobbos update script failed on $(date) with exit code $exit_code.\n\nPlease check the logs in $LOG_FILE to resolve the issue."
    fi
}
trap handle_failure EXIT

cd "$REPO_DIR"

# 1. Fetch remote state
git fetch origin

# 2. Check if local branch is behind origin/main
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse @{u})
BASE=$(git merge-base HEAD @{u})

if [ "$LOCAL" = "$REMOTE" ]; then
    echo "No remote changes detected."
    # Build anyway to ensure any manual local edits are compiled
    echo "Rebuilding site to ensure local sync..."
    cd "$SITE_DIR"
    npm run build
elif [ "$LOCAL" = "$BASE" ]; then
    echo "Local is behind. Stashing local changes and pulling remote..."
    
    # Check if there are changes to stash
    if ! git diff --quiet || ! git diff --cached --quiet || [ -n "$(git status --porcelain)" ]; then
        echo "Local changes detected. Stashing..."
        git stash -u
        STASHED=true
    else
        STASHED=false
    fi

    # Attempt pull
    git pull origin main

    if [ "$STASHED" = true ]; then
        echo "Reapplying stashed local changes..."
        if ! git stash pop; then
            echo "CONFLICT ERROR: Git stash pop failed due to merge conflicts."
            # We explicitly exit with non-zero here so the failure trap triggers
            exit 2
        fi
        
        # Notify the user that local changes were stashed/popped
        send_notification "Gobbos Update: Local Changes Stashed & Merged" "The update script pulled remote updates and reapplied your local modifications.\n\nSince local changes were stashed and popped, please check the repository status to ensure no conflicts require manual attention."
    fi
    
    echo "Rebuilding site..."
    cd "$SITE_DIR"
    npm run build
else
    echo "Local has diverged or is ahead of remote. Rebuilding only..."
    cd "$SITE_DIR"
    npm run build
fi

echo "Finished check at $(date)"
echo "---------------------------------------------"
