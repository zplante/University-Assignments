SELECT DISTINCT st.storeName, sa.dayDate
FROM Stores AS st, Sales AS sa
WHERE sa.storeID = st.storeID;