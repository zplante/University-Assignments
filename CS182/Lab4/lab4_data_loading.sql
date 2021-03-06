COPY Lab4.Products FROM stdin USING DELIMITERS '|';
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

COPY Lab4.Customers FROM stdin USING DELIMITERS '|';
1001|Ami Maggio|650 Kessler Common|2017-09-07|319.04|2018-03-11|H
1002|India Crona|15480 Moore Valley|2017-10-30|500.00|2018-03-10|M
1003|Ms. Dung Quitzon|9133 Herman Mountain|2017-04-17|0.00|2018-03-17|L
1004|Mee Spencer|10693 Marsha Fall|2017-03-01|51.44|2018-03-08|\N
1005|Kirk Batz|46945 Cole Landing|2017-06-09|79.00|2018-03-17|M
1006|Mr. Tressa Hayes|4917 Blake Skyway|2017-03-24|300.00|2018-03-10|L
1007|Orville Krajcik|3239 Tremblay Square|2017-09-09|0.00|2018-03-29|\N
1008|Jerrod White|6122 Fausto Flat|2017-03-31|70.99|2018-03-14|M
1009|Xavier Wyman V|951 Langworth Well|2017-11-19|108.95|2018-03-14|L
1010|Darnell Hagenes|123 Smitham Crescent|2017-05-29|0.00|2018-03-26|H
\.

COPY Lab4.Stores FROM stdin USING DELIMITERS '|';
1|Walmart Supercenter|North|5095 Almaden Expy, San Jose|Ben Romaguera
2|Best Buy|East|2650 41st Ave, Soquel|Franklyn Waelchi
3|Apple Store|South|23 N Santa Cruz Ave, Los Gatos|Joan Kunde
4|KOHL Retailer|North|19661 Hesperian Blvd, Hayward|Rami James
\.

COPY Lab4.Days FROM stdin USING DELIMITERS '|';
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

COPY Lab4.Sales FROM stdin USING DELIMITERS '|';
101|1001|1|2018-01-16|18.91|9
102|1001|3|2018-01-18|73.1|7
103|1001|1|2018-01-11|96.71|9
104|1001|2|2018-01-12|47|7
105|1001|4|2018-01-14|41.21|8
101|1002|1|2018-01-13|18.91|2
102|1002|3|2018-01-15|67.1|3
103|1002|1|2018-01-17|91.71|4
104|1002|4|2018-01-19|40|5
105|1002|3|2018-01-22|41.21|6
101|1003|1|2018-01-01|18.91|8
102|1003|3|2018-01-04|73.3|5
103|1003|1|2018-01-23|91.11|3
104|1003|4|2018-01-26|45|1
105|1003|3|2018-01-30|37|2
104|1004|1|2018-01-06|48.3|5
103|1004|1|2018-01-23|91.11|3
104|1004|2|2018-01-22|45|1
105|1004|3|2018-01-21|37|2
105|1005|4|2018-01-16|229.99|6
108|1005|3|2018-01-16|54.91|6
109|1005|3|2018-01-16|249.99|1
108|1006|1|2018-01-16|45.81|7
108|1006|4|2018-01-18|100.81|3
101|1007|1|2018-01-13|18.91|2
102|1007|3|2018-01-15|67.1|3
103|1007|1|2018-01-17|91.71|4
104|1007|2|2018-01-19|40|5
105|1007|4|2018-01-22|41.21|6
101|1008|1|2018-01-01|18.91|5
102|1008|3|2018-01-04|73.3|5
103|1008|1|2018-01-23|91.11|3
104|1008|2|2018-01-26|45|1
105|1009|3|2018-01-30|37|7
104|1009|4|2018-01-06|48.3|5
103|1009|1|2018-01-23|91.11|3
104|1009|2|2018-01-22|45|4
105|1009|3|2018-01-21|37|2
105|1010|4|2018-01-16|229.99|3
108|1010|3|2018-01-16|54.91|6
109|1010|3|2018-01-16|249.99|1
\.

COPY Lab4.Payments FROM stdin USING DELIMITERS '|';
1001|Ami Maggio|2018-02-17|100|f
1001|Ami Maggio|2018-02-01|42.9|t
1001|Ami Maggio|2018-02-19|376.06|f
1001|Ami Maggio|2018-03-17|400|f
1001|Ami Maggio|2018-03-01|112.11|t
1001|Ami Maggio|2018-03-19|116.36|f
1001|Ami Maggio|2018-05-17|20|f
1001|Ami Maggio|2018-02-21|50|f
1001|Ami Maggio|2018-04-21|114.1|t
1002|India Crona|2018-02-19|12.32|t
1002|India Crona|2018-05-21|30|f
1002|India Crona|2018-03-19|117.67|t
1002|India Crona|2018-02-09|17.69|f
1002|India Crona|2018-02-17|10|f
1002|India Crona|2018-04-19|234.57|t
1003|Morgan Bernhard|2018-02-26|200.34|f
1003|Morgan Bernhard|2018-02-27|200.34|f
1003|Morgan Bernhard|2018-02-25|11|f
1004|Elfrieda Kuhn|2018-02-04|100|t
1004|Elfrieda Kuhn|2018-02-26|200.34|f
1004|Elfrieda Kuhn|2018-02-19|394.4|t
1005|Laurice Hill|2018-02-12|249.99|t
1005|Laurice Hill|2018-02-23|112.08|f
1005|Laurice Hill|2018-02-04|100|f
1006|Tressa Hayes|2018-03-23|10|f
1006|Tressa Hayes|2018-02-21|186.08|t
1006|Tressa Hayes|2018-02-06|100|f
1007|Orville Krajcik|2018-02-01|42.9|t
1007|Orville Krajcik|2018-02-17|10|f
1007|Orville Krajcik|2018-02-25|11|f
1007|Orville Krajcik|2018-02-19|394.4|t
1007|Orville Krajcik|2018-02-12|454.74|t
1008|Jerrod White|2018-02-07|1271.09|f
1008|Jerrod White|2018-02-06|100|f
1008|Jerrod White|2018-02-19|376.06|f
1008|Jerrod White|2018-02-26|200.34|f
1008|Jerrod White|2018-02-04|100|f
1008|Jerrod White|2018-02-21|233.03|f
1009|Xavier Wyman V|2018-02-19|103.08|f
1009|Xavier Wyman V|2018-02-21|186.08|f
1009|Xavier Wyman V|2018-02-23|112.08|f
1010|Darnell Hagenes|2018-02-24|328.4|t
1010|Darnell Hagenes|2018-02-19|117.67|t
1010|Darnell Hagenes|2018-02-03|51.33|t
1010|Darnell Hagenes|2018-02-28|11.11|f
1010|Darnell Hagenes|2018-02-16|13.99|f
\.
