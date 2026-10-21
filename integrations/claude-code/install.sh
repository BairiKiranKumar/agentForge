#!/usr/bin/env bash
# Install ai-team agents as Claude Code subagents.
#
# Usage:
#   ./install.sh --project /path/to/project [--departments dev,qa,design]
#   ./install.sh --user [--departments sales,client-onboarding]
#   ./install.sh --list
#
# --project copies into <project>/.claude/agents/ai-team/ (recommended: only that project sees them)
# --user    copies into ~/.claude/agents/ai-team/ (every project sees them)
# --departments limits which departments are installed (default: all). Installing everything adds
#   every agent description to Claude Code's routing context; prefer the departments a project needs.
#
# Run tools/build_indexes.py first so integrations/claude-code/agents/ is current.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$HERE/agents"
TEAM_ROOT="$(cd "$HERE/../.." && pwd)"
DEST=""
DEPTS=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --project) DEST="$2/.claude/agents/ai-team"; shift 2 ;;
    --user) DEST="$HOME/.claude/agents/ai-team"; shift ;;
    --departments) DEPTS="$2"; shift 2 ;;
    --list) ls "$SRC"; exit 0 ;;
    -h|--help) sed -n '2,15p' "$0"; exit 0 ;;
    *) echo "Unknown option: $1" >&2; exit 1 ;;
  esac
done

if [[ -z "$DEST" ]]; then
  echo "Choose --project <dir> or --user" >&2
  exit 1
fi
if [[ ! -d "$SRC" ]]; then
  echo "No generated agents in $SRC. Run: python3 $TEAM_ROOT/tools/build_indexes.py" >&2
  exit 1
fi

mkdir -p "$DEST"
count=0
if [[ -z "$DEPTS" ]]; then
  for d in "$SRC"/*/; do
    name="$(basename "$d")"
    mkdir -p "$DEST/$name"
    cp "$d"*.md "$DEST/$name/"
    count=$((count + $(ls "$d"*.md | wc -l)))
  done
else
  IFS=',' read -ra LIST <<< "$DEPTS"
  for name in "${LIST[@]}"; do
    if [[ ! -d "$SRC/$name" ]]; then echo "Unknown department: $name" >&2; exit 1; fi
    mkdir -p "$DEST/$name"
    cp "$SRC/$name/"*.md "$DEST/$name/"
    count=$((count + $(ls "$SRC/$name/"*.md | wc -l)))
  done
fi

# The orchestrator is useful in every install.
if [[ -f "$SRC/orchestration/orchestrator.md" && ! -f "$DEST/orchestration/orchestrator.md" ]]; then
  mkdir -p "$DEST/orchestration"
  cp "$SRC/orchestration/orchestrator.md" "$DEST/orchestration/"
  count=$((count + 1))
fi

echo "Installed $count agent files into $DEST"
echo
echo "Next steps:"
echo "  1. Restart Claude Code (or open /agents) so it picks up the new subagents."
echo "  2. Shared rules: add this line to the project's CLAUDE.md so every agent follows them:"
echo "       @$TEAM_ROOT/AGENTS.md"
echo "     (Claude Code asks once to approve imports from outside the project.)"
echo "  3. Try: claude --agent orchestrator   or   @agent-orchestrator <your brief>"
