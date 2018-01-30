#!/usr/bin/env bash

# short
l1tool -f chun_east_detrend.dat -l 2000 -r 80 -p 365.25,186.725 -s mosek -v -o chun_out.dat

# long
# l1tool --file chun_east_detrend.dat --lam 2000 --rho 80 --periods 365.25,186.725 --verbose --solve cvxopt --out chun_out.dat