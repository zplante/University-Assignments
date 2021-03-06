COPY Lab3.Stores FROM stdin USING DELIMITERS '|';
1|Walmart Supercenter|North|5095 Almaden Expy, San Jose|Ben Romaguera
2|Best Buy|East |2650 41st Ave, Soquel|Franklyn Waelchi
3|Apple Store|South|23 N Santa Cruz Ave, Los Gatos|Joan Kunde
4|KOHL Retailer|North|19661 Hesperian Blvd, Hayward|Rami James
\.

COPY Lab3.Products FROM stdin USING DELIMITERS '|';
100|Intelligent Music Player|Google|18.99|8
101|Smart Phone|Apple|73.99|9
102|Intelligent Headphone|Boss|96.99|7
103|Alien Computer|Google|47.99|7
104|Intelligent Phone Charger|Google|41.99|9
105|Smart Speaker with Alexa|Amazon|84.99|9
106|Ring Alarm|Apple|98.99|8
107|Smart Plug|Amazon|50.99|8
108|Kindle Paperwhite|Amazon|123.99|9
109|XBOX ONE|Microsoft|249.99|8
110|Full HD Monitor|Acer|129.99|\N
111|4K UHD TV|Samsung|229.99|\N
\.

COPY Lab3.Customers FROM stdin USING DELIMITERS '|';
1001|Ami Maggio|650 Kessler Common|2017-09-07|119.04|2018-03-11|H
1002|India Crona|15480 Moore Valley|2017-10-30|300.00|2018-03-10|H
1003|Morgan Bernhard|959 Miller Crescent|2017-06-24|324.66|2018-03-26|M
1004|Elfrieda Kuhn|78872 Joesph Mountain|2017-10-14|480.00|2018-06-03|M
1005|Laurice Hill|53518 Pouros Stravenue|2017-04-26|217.38|2018-03-03|L
1006|Tressa Hayes|462 Halvorson Knolls|2017-03-24|0.00|2018-03-10|H
1101|Orville Krajcik|3239 Tremblay Square|2017-09-09|0.00|2018-03-29|H
1102|Darnell Hagenes|123 Smitham Crescent|2017-05-29|0.00|2018-03-26|H
1103|Mee Spencer|10693 Marsha Fall|2017-10-19|141.50|\N|L
\.

COPY Lab3.Sales FROM stdin USING DELIMITERS '|';
101|1001|1|2018-01-16|18.91|9
102|1001|3|2018-01-18|73.10|7
103|1001|1|2018-01-11|96.71|9
104|1001|2|2018-01-12|47.00|7
105|1001|3|2018-01-14|41.21|8
101|1002|1|2018-01-13|18.91|2
102|1002|3|2018-01-15|67.10|3
103|1002|1|2018-01-17|91.71|4
104|1002|2|2018-01-19|40.00|5
105|1002|3|2018-01-22|41.21|6
101|1003|1|2018-01-01|18.91|8
102|1003|3|2018-01-04|73.30|5
103|1003|1|2018-01-23|91.11|3
104|1003|2|2018-01-26|45.00|1
105|1003|3|2018-01-30|37.00|2
104|1004|1|2018-01-06|48.30|5
103|1004|1|2018-01-23|91.11|3
104|1004|2|2018-01-22|45.00|1
105|1004|3|2018-01-21|37.00|2
111|1005|3|2018-01-16|229.99|6
108|1005|3|2018-01-16|54.91|6
109|1005|3|2018-01-16|249.99|1
108|1006|1|2018-01-16|45.81|7
108|1006|4|2018-01-18|100.81|3
\.

COPY Lab3.Payments FROM stdin USING DELIMITERS '|';
1001|Ami Maggio|2018-02-17|100.00|f
1001|Ami Maggio|2018-02-01|42.90|t
1001|Ami Maggio|2018-02-19|376.06|f
1001|Ami Maggio|2018-03-17|400.00|f
1001|Ami Maggio|2018-03-01|112.11|t
1001|Ami Maggio|2018-03-19|116.36|f
1001|Ami Maggio|2018-05-17|20.00|f
1001|Ami Maggio|2018-02-21|50.00|f
1001|Ami Maggio|2018-04-21|114.10|t
1002|India Crona|2018-02-19|12.32|t
1002|India Crona|2018-05-21|30.00|f
1002|India Crona|2018-03-19|117.67|t
1002|India Crona|2018-02-09|17.69|f
1002|India Crona|2018-02-17|10.00|f
1002|India Crona|2018-04-19|234.57|t
1003|Morgan Bernhard|2018-02-26|200.34|f
1003|Morgan Bernhard|2018-02-27|200.34|f
1003|Morgan Bernhard|2018-02-25|11.00|f
1004|Elfrieda Kuhn|2018-02-04|100.00|t
1004|Elfrieda Kuhn|2018-02-26|200.34|f
1004|Elfrieda Kuhn|2018-02-19|394.40|t
1005|Laurice Hill|2018-02-12|249.99|t
1005|Laurice Hill|2018-02-23|112.08|f
1005|Laurice Hill|2018-02-04|100.00|f
1006|Tressa Hayes|2018-03-23|10.00|f
1006|Tressa Hayes|2018-02-21|186.08|t
1006|Tressa Hayes|2018-02-06|100.00|f
\.

COPY Lab3.Days FROM stdin USING DELIMITERS '|';
2018-01-15|C
2018-01-16|N
2018-01-17|N
2018-01-18|N
2018-01-19|N
2018-01-20|C
2018-01-21|C
2018-01-22|N
2018-01-23|N
2018-01-24|N
2018-01-25|N
2018-01-26|N
2018-01-12|N
2018-01-14|N
2018-01-30|N
2018-01-04|N
2018-01-13|N
2018-01-06|N
2018-01-11|N
2018-01-01|N
\.

COPY Lab3.NewCustomers FROM stdin USING DELIMITERS '|';
1001|Ami Lynch|9985 Chelsey Field|2017-09-07
1007|Stephen Bergstrom|2663 Florencia Square|2017-11-16
1008|Pasquale Herman|53528 Pouros Stravenue|2017-04-26
1104|Eustolia Wisoky|\N|\N
\.
