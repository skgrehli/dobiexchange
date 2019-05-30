from django.test import TestCase

# Create your tests here.

class Quote(models.Model):
	market = models.CharField(max_length=255)
	last	String	YES	20	Last price	0.001
ratio	String	YES	10	Chg	20%
eq	String	YES	100	The latest price is for other currencies, such as CNY for China Yuan exchange rate	{"cny":"50.00","usd":"7.69"}
high	String	YES	20	24h High	0.005
low	String	YES	20	24h Low	0.002
buy	String	YES	20	Buy price	0.001
sell	String	YES	20	Sell price	0.002
volume	String	YES	20	24h volume	6259250.6483
amount