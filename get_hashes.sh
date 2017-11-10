#!/bin/bash
git ls-remote $1 | awk "{print \$0, \"$1\"}"
