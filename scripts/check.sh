#!/bin/sh -eu

run_check() {
    printf "================== $2 =================\n"
    printf "$1 Running check for $2\n"
    shift

    if ! "$@"; then
        printf "^^^ +++\n\e[31mCheck failed for %s\e[0m\n" "$1"
        ret=1
    else
        printf "\n\e[32mCheck passed for %s\e[0m\n" "$1"
    fi
    printf "=========================================\n\n"
}

ret=0

cd ./hax

run_check "🔧 linting - " flake8 . --config=../.flake8

run_check "🐉 check imports sorting - " isort --check --diff --color --settings-path=../pyproject.toml .

run_check "🎯 static type checker - " mypy . --install-types --ignore-missing-imports --config-file=../pyproject.toml

run_check "🔩 static code analysis - " pylint . --rcfile=../pyproject.toml

exit $ret
