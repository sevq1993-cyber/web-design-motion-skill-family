#!/usr/bin/env bash
set -euo pipefail

REPO_URL="${WEB_DESIGN_MOTION_SKILLS_REPO:-https://github.com/sevq1993-cyber/web-design-motion-skill-family.git}"
CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
DEST="$CODEX_HOME/skills"
TMP_DIR="$(mktemp -d)"

cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

mkdir -p "$DEST"

if command -v git >/dev/null 2>&1; then
  git clone --depth 1 "$REPO_URL" "$TMP_DIR/repo" >/dev/null 2>&1
else
  echo "git is required to install this skill family." >&2
  exit 1
fi

if [ ! -d "$TMP_DIR/repo/skills" ]; then
  echo "Repository does not contain a skills/ directory." >&2
  exit 1
fi

installed=0
skipped=0

for skill_dir in "$TMP_DIR/repo"/skills/*; do
  [ -d "$skill_dir" ] || continue
  [ -f "$skill_dir/SKILL.md" ] || continue
  name="$(basename "$skill_dir")"
  target="$DEST/$name"
  if [ -e "$target" ] && [ "${FORCE:-0}" != "1" ]; then
    echo "skip $name: already exists at $target"
    skipped=$((skipped + 1))
    continue
  fi
  rm -rf "$target"
  cp -R "$skill_dir" "$target"
  echo "installed $name"
  installed=$((installed + 1))
done

echo
echo "Installed: $installed"
echo "Skipped: $skipped"
echo "Restart Codex to pick up new skills."
echo
echo "To overwrite existing skills, run:"
echo "  curl -fsSL https://raw.githubusercontent.com/sevq1993-cyber/web-design-motion-skill-family/main/install.sh | FORCE=1 bash"
