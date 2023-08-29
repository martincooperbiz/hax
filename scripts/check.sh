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


run_check "🔧 linting - " flake8 ./hax --config=.flake8

run_check "🐉 check imports sorting - " isort ./hax --check --diff --color --settings-path=pyproject.toml

run_check "🎯 static type checker - " mypy ./hax --ignore-missing-imports --install-types --config-file=pyproject.toml

run_check "🔩 static code analysis - " pylint ./hax --rcfile=pyproject.toml

exit $ret
