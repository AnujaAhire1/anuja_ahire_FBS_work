#WAP to convert days into years, weeks, days

#Take input
days = int(input("Enter days:")) #days 1000

#Calculate year
years = days // 365 #1.5 : 1 year 6 months
print('Years:', years)
days = days % 365

#Calculate week
weeks =  days // 7
print('weeks:', weeks)

#Calculate days
days = days % 7
print('days:', days)