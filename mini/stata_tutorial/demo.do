use ./data/food.dta, clear

* regression
regress food_exp income

* obtain fitted values
predict yhat, xb

* obtain residuals
predict ehat, residuals

* list in 1/10
list income food_exp yhat ehat in 1/10

scalar yhat20 = _b[_cons] + _b[income] * 20
scalar list yhat20

lincom income - 10

use ./data/andy, clear

* regression
regress sales price advert c.advert#c.advert

* F test
test price c.advert#c.advert

clear all
use ./data/cps5_small, clear

* regression
reg wage educ i.black##i.female

* F test
test 1.female 1.black 1.black#1.female

reg wage i.female##c.educ
bysort female: reg wage educ

use ./data/food, clear
* regression
quietly reg food_exp income
estimates store m1
quietly reg food_exp income, vce(robust)
estimates store m2
esttab m1 m2, b(%7.4f) se(%7.3f) scalars(F) mtitles("Incorrect" "Robust")

use http://fmwww.bc.edu/ec-p/data/wooldridge/hprice1, clear
reg price lotsize sqrft bdrms

* white test
whitetst
whitetst, fitted