#a global function for calculate monthly payment at monthly rate r
def find_payment(loan, r, m):
    return loan*((r*(1+r)**m)/((1+r)**m-1))

#Mortgage super calss 
class Mortgage(object):
    def __init__(self, loan, ann_rate, months):
        self._loan = loan
        self._rate = ann_rate/12
        self._months = months
        self._paid = [0.0]
        self._outstanding = [loan]
        self._payment = find_payment(loan, self._rate, months)
        self._legend = None

    #a method for payment mechanism
    def make_payment(self):
        self._paid.append(self._payment)
        reduction = self._payment - self._outstanding[-1]*self._rate
        self._outstanding.append(self._outstanding[-1] - reduction)
    
    #how much we paid at all
    def get_total_paid(self):
        return sum(self._paid)
    
    #description of mortgage
    def __str__(self):
        return self._legend

#now we describe 3 type of mortgages

#fixed rate mortgage
class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self._legend = f'Fixed, {r*100:.1f}%'

#fixed rate with pts number of points
class Fixed_with_pts(Mortgage):
    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self._pts = pts
        self._paid = [loan*(pts/100)]
        self._legend = f'Fixed, {r*100:.1f}%, {pts} points'

#two rates mortgage
class Two_rate(Mortgage):
    def __init__(self, loan, r, months, teaser_rate, teaser_months):
        Mortgage.__init__(self, loan, teaser_rate, months)
        self._teaser_months = teaser_months
        self._teaser_rate = teaser_rate
        self._nextRate = r/12
        self._legend = (f'{100*teaser_rate:.1f}% for'+ f'{self._teaser_months} months, then {100*r:.1f}%')

    #override payment mechanism
    def make_payment(self):
        if len(self._paid) == self._teaser_months + 1:
            self._rate = self._nextRate
            self._payment = find_payment(self._outstanding[-1], self._rate, self._months-self._teaser_months)
        Mortgage.make_payment(self)


#a global function for compairing types of mortgages
def compare_mortgages(amt, years, fixed_rate, pts, pts_rate, var_rate1, var_rate2, var_months):
    tot_months = years*12
    fixed1 = Fixed(amt, fixed_rate, tot_months)
    fixed2 = Fixed_with_pts(amt, pts_rate, tot_months, pts)
    two_rate = Two_rate(amt, var_rate2, tot_months, var_rate1, var_months)
    morts = [fixed1, fixed2, two_rate]
    
    for m in range(tot_months):
        for mort in morts:
            mort.make_payment()
    for m in morts:
        print(m)
        print(f' Total payments = ${m.get_total_paid():.1f}')

'''We have a test case: in 25 years, we borrowed $350,000 
'''
compare_mortgages(amt=350000, years=25, fixed_rate=0.035, pts = 4, pts_rate=0.03, var_rate1=0.03, var_rate2=0.05, var_months=60)

''' the output should be:
Fixed, 3.5%
 Total payments = $525654.7
Fixed, 3.0%, 4 points
 Total payments = $511921.9
3.0% for60 months, then 5.0%
 Total payments = $573594.9

 witch means that, in fixed rate(3.5%) mortgage total mony tou should pay back is: $525654.7
 in fixed rate with points(3% point rate) and 4 points total mony tou should pay back is: $511921.9
 in two ratio mortgage in 60 teaser months with 3% teaser rate, your payment is $573594.9
 maby you shouldn't try Two-rate! :) 
'''