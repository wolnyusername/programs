# programs

Forex calculator allows user to calculate forex bid before it is placed in market.
It downloads forex rates from website "inveting.com", after that user is asked to chose on what currencies pair would he likes to bet.
After collecting bet details program prints stop loss and take profit value, expected win and loss expresed in base currency.

Odds calculator allows user to download bets for world cup from polish bookmaker (fortuna, fuksiarz, super bet) and transform them into pandas data frame groupby "match name".
After that program is calculating arbitrage for every bet possibility and print bets where arbitrege can be applied, with specific detais about odds, bookmaker name and value of bets. Odds calculator DOES NOT work during live game and need constant update in download content section.
