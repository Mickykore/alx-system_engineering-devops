#!/bin/bash
    repos=("alx-system_engineering-devops" "alx-higher_level_programming" "alx-low_level_programming")
    for repo in "${repos[@]}"
    do
	    git clone git@github.com:Mickykore/$repo.git
    done
