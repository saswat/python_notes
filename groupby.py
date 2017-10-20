#groupby and lambda function to calculate weight by doing quant * weight for a df
print(df.groupby('Category').apply(lambda df,a,b: sum(df[a] * df[b]), 'Weight (oz.)', 'Quantity'))
