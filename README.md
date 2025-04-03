# Python brewery

## Solution

In this project we want to help people organize a dispatch of orders to multiple bar.

We have multiple client bars and a set of distribution centers.

Each distribution center has its own capacity and can deliver bars in a given time.

Our clients want to be able to generate dispatch routes for each center to know how many kegs should be delivered at to which bar.

The location, storage capacities and provisioning schedules of the centers are actually put in a "cold storage" inside the solution as CSVs.

Each bar is considered to have an equal capacity of kegs, and need to be refilled before it runs out.

## Connector

Our client has a CSV file that allows us to know the average consumption of each bar.

The connector take that CSV and generate 2 new files :
- one listing each bar, their consuption, and their initial capacity
- one listing for each pair of bar/center the duration required for a delivery

## Run the code

To get a running version of the code and see the results run the following commands (requires `docker`)

```bash
docker build . -t my_solution
docker run my_solution
```

## Questions

For this part you will be paired with a developper of the solution and connector charged with maintaining the project.

### 1. Understand the code Organisation

Look at how the repository is constructed and ask any questions you may have

### 2. Implement a small enhancement of the Connector

Now a client want to be able to add the capacity of each bar so that they are not all fixed.

The new CSV format they want to send us is in Client/Storage/data.csv

How would you go at integrating that new csv in the process for a specific client ?

### 3. Implement a small enhancement of the Output

Another client would like his results to be sent to an external database instead of generating a local CSV.

How would you go at it ?
