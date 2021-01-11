def monthly_payment(property_val, mortgage_interest, mortgage_duration, down_payment):
    payment = mortgage_interest / 12 * (property_val - down_payment) / ((1 - (1 + mortgage_interest / 12)**(mortgage_duration * -12)) * (1 + mortgage_interest / 12))
    payment = round(payment, 2)
    return payment

def future_value_annuity(payment, rate, num_periods):
    fv = payment * ((1 + rate)**num_periods - 1) / rate
    fv = round(fv, 2)
    return fv

def future_value(present_value, rate, num_periods):
    fv = present_value * (1 + rate) ** num_periods
    fv = round(fv, 2)
    return fv

def rent_or_buy(property_val, investment_duration, rent, time_value_money=.07, tax_rate=.011, mortgage_interest=.03, mortgage_duration=30, down_payment=0, hoa_cost=0, property_increase_rate=.04, rent_increase_rate=.04):
    insurance_monthly = 200
    tax_semi_annual = property_val * tax_rate / 2
    mortgage_monthly = monthly_payment(property_val, mortgage_interest, mortgage_duration, down_payment)
    hoa_monthly = hoa_cost

    property_cost_fv = -(future_value_annuity(insurance_monthly + mortgage_monthly + hoa_monthly, time_value_money / 12, investment_duration * 12) + future_value_annuity(tax_semi_annual, time_value_money / 2, investment_duration * 2))
    property_fv = future_value(property_val, property_increase_rate, investment_duration)
    overall_property_fv = property_fv + property_cost_fv

    rent_fv = -(future_value_annuity(rent, ((1 + time_value_money) * (1 + rent_increase_rate) - 1) / 12, investment_duration * 12))

    print(property_cost_fv)
    print(property_fv)
    print(overall_property_fv)
    print("\n")
    print(rent_fv)


rent_or_buy(300000, 30, 1000)