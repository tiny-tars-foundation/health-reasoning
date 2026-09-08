#!/usr/bin/env bash
set -euo pipefail

# Lints this repo's finding-dag/ vault using the public @pablotech/neuro-pil engine
# (github.com/pablo-tech/pilos) — unknown inputs, orphaned nodes, cycles. Needs nothing but git
# and node/npm: no private-repo checkout, no GitHub org membership, no credentials of any kind.
#
# Usage, from anywhere inside a clone of this repo:
#   scripts/validate-vault.sh
#
# A second brain folder later: scripts/validate-vault.sh <folder-name>
#
# Exits non-zero and prints the findings if the vault is broken; exits 0 if it's clean. Clones
# pilos into a throwaway temp dir each run and deletes it after — this repo's working tree is
# never touched.

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VAULT_PATH="$REPO_ROOT/${1:-finding-dag}"

if [[ ! -d "$VAULT_PATH" ]]; then
  echo "no such brain folder: $VAULT_PATH" >&2
  exit 1
fi

WORK_DIR="$(mktemp -d)"
trap 'rm -rf "$WORK_DIR"' EXIT

git clone --quiet https://github.com/pablo-tech/pilos.git "$WORK_DIR/pilos"
npm install --silent --prefix "$WORK_DIR/pilos/neuro-pil"
npm --prefix "$WORK_DIR/pilos/neuro-pil" run cli -- lint "$VAULT_PATH"
