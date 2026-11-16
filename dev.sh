DIR="$(cd "$(dirname "$0")" && pwd)"

kitty @ launch --type=tab --tab-title "Dev" --cwd "$DIR" sh -c "npm run dev; exec $SHELL"
kitty @ goto-layout splits
kitty @ launch --type=window --location=vsplit --cwd "$DIR/Api" sh -c "uv run fastapi dev; exec $SHELL"
