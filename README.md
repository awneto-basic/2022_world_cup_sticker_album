# 2022_world_cup_sticker_album
Calculating the probabilities of events related to collecting stickers from the 2022 World Cup sticker album


What if you wanted to complete the a sticker album collection without trading stickers with other collectors? What is the expected number of packets you would have to purchase in this scenario?

Read the full explanation [here](https://alexandrewillikneto.wordpress.com/2022/10/22/got-got-need-trying-to-complete-a-sticker-album-without-trading_duplicates/).

To answer this question, we can refer to the Coupon collector’s problem, a classical problem with studies dating back to the 18th century. The goal of the problem is to calculate the average number of purchases a collector of coupons (or stickers, cards, tickets etc.) needs to make to complete the coupon collection, given that there is a finite number of coupons to be collected, and that each coupon is randomly selected (i.e., the collector does not know which coupon it will get on each purchase).


For the 2022 FIFA World Cup album, the probabilities associated with various waiting times (from buying 1 sticker packet to buying 2000 sticker packets) for obtaining all stickers from the collection are shown on the plot below:
![image](https://github.com/awneto-basic/2022_world_cup_sticker_album/assets/29670261/ed1bdae4-1423-425e-b82e-dadc06fcf58d)

The probabilities associated with various waiting times for obtaining all stickers of a defined national team without trading duplicate stickers are shown on the plot below:
![image](https://github.com/awneto-basic/2022_world_cup_sticker_album/assets/29670261/f32b0c2e-ed81-4847-ab1f-89f2e5819f53)

The plots shown below present the probability of completing this year’s sticker album and expected number of distinct stickers to be obtained for various amounts of packets to be bought, assuming that no duplicates are traded.
![image](https://github.com/awneto-basic/2022_world_cup_sticker_album/assets/29670261/a711ea4a-b3d5-40c9-9f34-51bc914e2107)

The plots shown below present the probability of obtaining all 20 stickers from a defined national team (e.g. Brazil) and expected number of distinct stickers from the subset to be obtained for various amounts of packets to be bought, assuming that the trading of duplicate stickers does not take place.
![image](https://github.com/awneto-basic/2022_world_cup_sticker_album/assets/29670261/99e94cd9-f367-48cc-ad7f-703150d0e858)

The _paniny.py_ Python script listed in this repository was to calculate the probabilities and expected values and to produce the plots above.
Note that the Decimal module was needed to compute the large numbers involved in the calculations (e.g. the factorial of 670).

The above results confirms the common sense: it pays off to swap duplicate stickers with other collectors. Speaking from experience, it may also make the whole collecting experience more fun. Happy trading!

